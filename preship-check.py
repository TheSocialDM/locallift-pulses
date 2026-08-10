#!/usr/bin/env python3
"""
Pre-ship guard for thesocialdm/locallift-pulses.

Run from the repo root BEFORE any push or upload:

    python3 preship-check.py             # every report
    python3 preship-check.py village     # one folder

Exit 0 = SHIP.  Exit 1 = BLOCK, with the exact text and its surrounding context.

BLOCK  = never goes to a client: a tool or vendor name anywhere in the file
         (including HTML and JS comments), or another property's name inside
         a Weekly Pulse.
note   = worth fixing on the next rebuild, does not stop a ship: legacy
         em dashes, missing Section 1 card classes.

Base64 image data is stripped before scanning, so image blobs never trigger
a false alarm. That matters: raw base64 contains strings like "GA4".
"""
import re, sys, os, glob

VENDORS = (r'semrush|hello ?data|costar|metricool|yardi|google business|'
           r'business\.google|search console|\bGA4\b')

PROPERTIES = [
    'Pillar Lago', 'Soren', 'Circa on Central', 'Elevation SanTan', '2nd and John',
    'Helix Ellipse', 'Decibel', 'Reverb', 'Huxley', 'Elevation on Central', '56 North',
    'The View at Cascade', 'Cuvee', 'Village of Chandler', 'Coya', 'Fora', 'Lura',
    'Montage', 'Stillwater', 'Haven',
]

OWN = {
    'village': ['Village of Chandler'], 'coya': ['Coya'], 'fora': ['Fora'], 'lura': ['Lura'],
    'montage': ['Montage'], 'stillwater': ['Stillwater'], 'haven': ['Haven'],
    'pillar-lago': ['Pillar Lago'], 'soren': ['Soren'], 'circa-on-central': ['Circa on Central'],
    'elevation-santan': ['Elevation SanTan'], '2nd-and-john': ['2nd and John'],
    'helix-ellipse': ['Helix Ellipse'], 'decibel': ['Decibel', 'Reverb'],
    'decibel-reverb': ['Decibel', 'Reverb'], 'huxley-scottsdale': ['Huxley'],
    'elevation-on-central': ['Elevation on Central'], '56-north': ['56 North'],
    'the-view-at-cascade': ['The View at Cascade'], 'cuvee': ['Cuvee'],
}

# Comp intelligence reports legitimately name competitors in the comp set, so
# cross-property names are only a hard block in the Weekly Pulses and socials.
STRICT_PREFIXES = ('coya/', 'fora/', 'lura/', 'montage/', 'stillwater/', 'village/', 'social/')


def strip_b64(t):
    return re.sub(r'data:image/[^"\')]+', '', t)


def check(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    t = strip_b64(raw)
    rel = path.replace('./', '')
    slug = os.path.basename(os.path.dirname(path))
    problems, notes = [], []

    for m in re.finditer(VENDORS, t, re.I):
        s = max(0, m.start() - 60)
        ctx = ' '.join(t[s:m.end() + 60].split())
        problems.append(f'VENDOR NAME "{m.group(0)}"   ...{ctx[:130]}...')

    dashes = len(re.findall(r'[—–−]', t))
    if dashes:
        notes.append(f'{dashes} em/en dash(es), legacy copy, fix on next rebuild')

    own = OWN.get(slug, [])
    strict = any(rel.startswith(p) for p in STRICT_PREFIXES)
    for name in PROPERTIES:
        if name in own:
            continue
        if re.search(r'\b' + re.escape(name) + r'\b', t):
            (problems if strict else notes).append(f'OTHER PROPERTY "{name}"')

    if rel.startswith('market-intel'):
        missing = [c for c in ('wc u', 'wc w', 'wc p', 'wh') if c not in raw]
        if missing:
            notes.append(f'section 1 card classes missing {missing}, would render as flat text')

    return problems, notes


def main():
    targets = sys.argv[1:]
    files = [f for f in sorted(glob.glob('**/index.html', recursive=True))
             if not targets or any(t in f for t in targets)]
    if not files:
        print('No index.html found. Run this from the repo root.')
        return 1

    fails = 0
    for f in files:
        problems, notes = check(f)
        if problems:
            fails += 1
            print(f'\nBLOCK  {f}')
            for p in dict.fromkeys(problems):
                print('       ' + p)
        else:
            warn = '  |  ' + '; '.join(dict.fromkeys(notes)) if notes else ''
            print(f'ok     {f}{warn}')

    print('\n' + '=' * 62)
    if fails:
        print(f'BLOCK  {fails} of {len(files)} file(s) must not ship.')
        return 1
    print(f'SHIP   all {len(files)} file(s) clear of vendor names and cross-property leaks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
