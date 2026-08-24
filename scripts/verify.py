#!/usr/bin/env python3
"""
One gate to run before any comp-intelligence push.

    python3 scripts/verify.py <slug>            # e.g. elevation-on-central
    python3 scripts/verify.py <slug> --no-render   # skip the browser gates

Runs, in order:
  1. preship-check.py            vendor names and cross-property leaks
  2. design-lock                 the <style> block must be byte-identical to
                                 the version currently on origin/main
  3. numeric recomputation       every derived figure in facts.json is
                                 recomputed here and diffed against the page
  4. residual scan               other property names, prior-week stat values,
                                 em dashes, Section 1 card classes
  5. headless render             zero JS and console errors, model exercised
                                 at more than one slider position
  6. 390px check                 no horizontal overflow on a phone viewport

Prints exactly one verdict: SHIP or FIX.
Exit 0 = SHIP. Exit 1 = FIX.
"""
import json, os, re, subprocess, sys, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAIL, NOTE = [], []


def fail(gate, msg):
    FAIL.append(f"[{gate}] {msg}")


def note(gate, msg):
    NOTE.append(f"[{gate}] {msg}")


def strip_b64(t):
    return re.sub(r'data:image/[a-z]+;base64,[A-Za-z0-9+/=]+', '[B64]', t)


def gate1_preship(rel):
    r = subprocess.run([sys.executable, 'preship-check.py', os.path.basename(os.path.dirname(rel))],
                       cwd=ROOT, capture_output=True, text=True)
    if r.returncode != 0:
        fail('gate1', 'preship-check returned BLOCK:\n' + r.stdout.strip())
        return False
    return True


def gate2_designlock(rel, cur):
    r = subprocess.run(['git', 'show', f'origin/main:{rel}'], cwd=ROOT,
                       capture_output=True, text=True)
    if r.returncode != 0:
        note('gate2', 'no deployed version on origin/main, design-lock skipped (first publish)')
        return
    def css(t):
        m = re.search(r'<style>(.*?)</style>', t, re.S)
        return m.group(1) if m else None
    a, b = css(r.stdout), css(cur)
    if a is None or b is None:
        fail('gate2', 'could not locate a <style> block to compare')
    elif a != b:
        fail('gate2', 'CSS drifted from the deployed template. Design-lock is enforced: swap values only.')


def gate3_numbers(facts, txt):
    """Recompute, do not trust. Then confirm each figure is actually on the page."""
    p = facts['plans']
    units = sum(x['u'] for x in p)
    if units != facts['units']:
        fail('gate3', f"plan units sum to {units}, header says {facts['units']}")

    exposed = sum(round(x['u'] * x['expo'] / 100) for x in p)
    if exposed != facts['exposed_homes']:
        fail('gate3', f"plan exposure sums to {exposed} homes, page says {facts['exposed_homes']}")

    # blended renewal and the homes that turn in a year. Rule 13: every recovery
    # figure is applied to the homes that turn, never to the full unit count.
    ren_rows = [x for x in p if x.get('renew') is not None]
    ru = sum(x['u'] for x in ren_rows)
    renew = sum(x['u'] * x['renew'] for x in ren_rows) / ru
    if abs(renew - facts['renew_blend']) > 0.15:
        fail('gate3', f"blended renewal recomputes to {renew:.1f}, page says {facts['renew_blend']}")

    # optional stabilized / hold split
    if 'stabilized' in facts:
        stab = [x for x in p if x['name'] in facts['stabilized']]
        hold = [x for x in p if x['name'] not in facts['stabilized']]
        su, hu = sum(x['u'] for x in stab), sum(x['u'] for x in hold)
        if su != facts['stab_units'] or hu != facts['hold_units']:
            fail('gate3', f"stabilized/hold split recomputes to {su}/{hu}, page says "
                          f"{facts['stab_units']}/{facts['hold_units']}")
        if su + hu != units:
            fail('gate3', f"{su} + {hu} != {units}")
        se = sum(round(x['u'] * x['expo'] / 100) for x in stab)
        he = sum(round(x['u'] * x['expo'] / 100) for x in hold)
        if se + he != exposed:
            fail('gate3', f"exposure split {se}+{he} != {exposed}")
        for got, want, lab in ((se / su * 100, facts['stab_expo_pct'], 'stabilized exposure %'),
                               (he / hu * 100, facts['hold_expo_pct'], 'hold-group exposure %')):
            if abs(got - want) > 0.15:
                fail('gate3', f"{lab} recomputes to {got:.1f}, page says {want}")

    # the recovery model, recomputed end to end from the plan rows
    m = facts['recovery']
    scope = [x for x in p if x['name'] in m['scope']] if m.get('scope') else p
    su = sum(x['u'] for x in scope)
    sren = sum(x['u'] * x['renew'] for x in scope) / su
    if abs(sren - m['scope_renew']) > 0.15:
        fail('gate3', f"recovery-scope renewal recomputes to {sren:.1f}, page says {m['scope_renew']}")
    turn = su * (1 - sren / 100)
    if abs(turn - m['turn']) > 0.6:
        fail('gate3', f"homes turning recomputes to {turn:.1f}, page says {m['turn']}")
    if m['turn'] >= units:
        fail('gate3', 'rule 13: the recovery base is not smaller than the full unit count')
    if m.get('turn_weighted_ask'):
        twa = (sum(x['u'] * (1 - x['renew'] / 100) * x['rent'] for x in scope)
               / sum(x['u'] * (1 - x['renew'] / 100) for x in scope))
        if abs(twa - m['ask']) > 3:
            fail('gate3', f"turn-weighted asking recomputes to ${twa:,.0f}, page says ${m['ask']:,}")
    rec = m['trim_weeks'] * (m['ask'] * 12 / 52) * m['turn']
    if abs(rec - m['recovery']) / m['recovery'] > 0.012:
        fail('gate3', f"recovery recomputes to ${rec:,.0f}, page says ${m['recovery']:,}")
    if m.get('blend_after') is not None:
        after = ((m['scope_units'] * m['target_weeks']
                  + (units - m['scope_units']) * m['cur_weeks']) / units / 52 * 100)
        if abs(after - m['blend_after']) > 0.1:
            fail('gate3', f"blended depth after trim recomputes to {after:.1f}%, "
                          f"page says {m['blend_after']}%")

    comps = facts['comps']
    for key, want, tol in (('leased', facts['comp_leased'], 0.06),
                           ('ner', facts['comp_ner'], 0.6),
                           ('ask', facts['comp_ask'], 0.6),
                           ('conc', facts['comp_conc'], 0.06)):
        got = sum(c[key] for c in comps) / len(comps)
        if abs(got - want) > tol:
            fail('gate3', f"comp {key} average recomputes to {got:.2f}, page says {want}")
    if any(c.get('subj') for c in comps):
        fail('gate3', 'the subject is inside the peer group it is being judged against')
    for c in comps:
        if c.get('tag') in ('INCOME RESTRICTED',):
            fail('gate3', f"{c['n']} is income restricted and must not sit inside a pricing average")

    for s in facts['must_appear']:
        if s not in txt:
            fail('gate3', f'figure not found on the page: {s}')


def gate4_residual(facts, txt, slug):
    others = ['Pillar Lago', 'Soren', 'Circa on Central', 'Elevation SanTan', '2nd and John',
              'Helix Ellipse', 'Decibel', 'Reverb', 'Huxley', '56 North', 'The View at Cascade',
              'Cuvee', 'Village of Chandler', 'Coya', 'Fora', 'Lura', 'Montage', 'Stillwater']
    for o in others:
        if o.lower() in txt.lower() and o.lower() not in facts['subject'].lower():
            fail('gate4', f'another property leaked into the report: {o}')
    for stale in facts.get('must_not_appear', []):
        if stale in txt:
            fail('gate4', f'prior-week value still on the page: {stale}')
    # A retired figure may appear ONLY inside an explicit correction. Gate 4 of the
    # verification standard requires a changed read to be stated, not silently dropped,
    # so the test is that every occurrence sits inside a sentence that names last week.
    for item in facts.get('retracted', []):
        val, marker = item['value'], item['marker']
        for m in re.finditer(re.escape(val), txt):
            window = txt[max(0, m.start() - 260):m.end() + 140]
            if marker.lower() not in window.lower():
                fail('gate4', f'retired figure "{val}" appears outside a correction '
                              f'(no "{marker}" in the surrounding sentence)')
    if '\u2014' in txt:
        fail('gate4', 'em dash found')
    if 'watch' not in txt or 'class="wc ' not in txt or 'class="wh"' not in txt:
        fail('gate4', 'Section 1 is missing the watch / wc / wh card classes and will render as flat text')
    allowed = set(facts.get('allowed_cities', [facts['city']]))
    if facts['city'] not in allowed:
        fail('gate4', f"the subject's own city {facts['city']} is not in allowed_cities")
    bad = [f"{c['n']} ({c.get('city')})" for c in facts['comps']
           if c.get('city', facts['city']) not in allowed]
    if bad:
        fail('gate4', f'comps outside the declared submarket: {bad}')
    for c in facts['comps']:
        if c.get('city') and c['city'] not in txt:
            note('gate4', f"{c['city']} is a comp city but never named on the page")
    # Applications, cancellations and cancel % are internal signal only. They are
    # inferred from listing turnover and are not a 30-day count, so a COUNT of them
    # must never reach the page. The words alone are fine (application fee,
    # tour-to-application); a number attached to them is not.
    for m in re.finditer(r'(application|cancellation|cancel)s?\b', txt, re.I):
        seg = txt[max(0, m.start() - 40):m.end() + 40]
        if re.search(r'fee', seg, re.I):
            continue
        if re.search(r'\d+\s*(/|per|,)?\s*(applications?|cancels?|cancellations?)', seg, re.I) \
           or re.search(r'(applications?|cancels?|cancellations?)[^.]{0,20}\d', seg, re.I):
            fail('gate4', 'a modelled application or cancellation count reached the page: '
                          f'...{seg.strip()}...')
            break


def gate56_render(path, facts):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        note('gate5', 'playwright unavailable, render gates skipped')
        return
    errs, logs = [], []
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        pg = b.new_page(viewport={'width': 1280, 'height': 900})
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.on('console', lambda m: logs.append(m.text) if m.type == 'error' else None)
        pg.goto('file://' + os.path.abspath(path), wait_until='load')
        pg.wait_for_timeout(1400)
        if errs:
            fail('gate5', 'JS errors on load: ' + '; '.join(errs[:3]))
        if logs:
            fail('gate5', 'console errors on load: ' + '; '.join(logs[:3]))

        cards = pg.eval_on_selector_all('.watch .wc', 'e=>e.map(x=>x.getBoundingClientRect().width)')
        if len(cards) != 3 or min(cards) < 120:
            fail('gate5', f'Section 1 did not render as three cards (widths {cards})')

        cur = str(facts['recovery']['cur_weeks'])
        tgt = str(facts['recovery']['target_weeks'])
        seen = {}
        for wk in (cur, tgt, '0'):
            pg.eval_on_selector('#wk', f"e=>{{e.value={wk};e.dispatchEvent(new Event('input'))}}")
            pg.wait_for_timeout(250)
            seen[wk] = pg.eval_on_selector('#recbig', 'e=>e.textContent')
        if len(set(seen.values())) < 3:
            fail('gate5', f'recovery model did not respond across slider positions: {seen}')
        if seen[cur].strip().lstrip('+-') not in ('$0', '$0K'):
            fail('gate5', f"at the current {cur}-week offer the model should recover $0, "
                          f"it shows {seen[cur]}")

        pg.set_viewport_size({'width': 390, 'height': 844})
        pg.wait_for_timeout(500)
        over = pg.evaluate("()=>{const d=document.documentElement;"
                           "return [d.scrollWidth, d.clientWidth];}")
        if over[0] > over[1] + 1:
            wide = pg.evaluate("()=>Array.from(document.querySelectorAll('body *'))"
                               ".filter(e=>e.getBoundingClientRect().right>391)"
                               ".slice(0,4).map(e=>e.className||e.tagName)")
            fail('gate6', f'horizontal overflow at 390px ({over[0]}px wide). First offenders: {wide}')
        b.close()


def main():
    if len(sys.argv) < 2:
        print('usage: python3 scripts/verify.py <slug> [--no-render]')
        return 2
    slug = sys.argv[1]
    rel = f'market-intel/{slug}/index.html'
    path = os.path.join(ROOT, rel)
    facts_path = os.path.join(ROOT, f'market-intel/{slug}/facts.json')
    if not os.path.exists(path):
        print(f'FIX    {rel} does not exist')
        return 1
    if not os.path.exists(facts_path):
        print(f'FIX    {facts_path} does not exist. Gate 3 cannot recompute without it.')
        return 1

    raw = io.open(path, encoding='utf-8').read()
    txt = strip_b64(raw)
    facts = json.load(io.open(facts_path, encoding='utf-8'))

    if gate1_preship(rel):
        gate2_designlock(rel, raw)
        gate3_numbers(facts, txt)
        gate4_residual(facts, txt, slug)
        if '--no-render' not in sys.argv:
            gate56_render(path, facts)

    print()
    for n in NOTE:
        print('note  ', n)
    if FAIL:
        for f in FAIL:
            print('  ->  ', f)
        print(f'\nFIX    {len(FAIL)} defect(s). Nothing ships until these are clear.')
        return 1
    print(f'SHIP   {rel} cleared every gate.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
