"""Social proof blocks injected into static pages at build time.
<!--proof:communities-->            scrolling row of communities and operators (tools/communities.json, logos in tools/logos/ when supplied)
<!--proof:testimonials:<group>-->   scrolling Google review quotes (tools/testimonials.json) for home, multifamily, real-estate ..."""
import html, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
STARS = '<span class="tm-stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

ICONS = {  # 24x24 stroke icons, drawn for the ticker
 'building':'<path d="M4 21V5l8-3 8 3v16"/><path d="M9 21v-4h6v4M8 8h2M14 8h2M8 12h2M14 12h2"/>',
 'star':'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
 'pin':'<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
 'trend':'<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
 'send':'<path d="M21 3L10 14"/><path d="M21 3l-7 18-4-7-7-4z"/>',
 'calendar':'<rect x="3" y="5" width="18" height="16"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 'pulse':'<path d="M3 12h4l3-7 4 14 3-7h4"/>',
 'clipboard':'<rect x="5" y="4" width="14" height="17"/><path d="M9 4V2h6v2M9 10h6M9 14h6M9 18h3"/>',
 'chart':'<path d="M3 21h18"/><rect x="5" y="11" width="3" height="7"/><rect x="11" y="7" width="3" height="11"/><rect x="17" y="3" width="3" height="15"/>',
 'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
 'spark':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
 'tag':'<path d="M3 12V3h9l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
 'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.2 3 14.8 0 18M12 3c-3 3.2-3 14.8 0 18"/>',
 'message':'<path d="M4 4h16v12H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
 'play':'<rect x="3" y="5" width="18" height="14"/><path d="M10 9l5 3-5 3z"/>',
 'key':'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M15 8l2 2"/>',
 'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 15c2.4.6 4 2.6 4 6"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 'flag':'<path d="M5 21V4M5 4h12l-2 4 2 4H5"/>',
}

def ticker(name='ticker'):
    d = json.load(open(os.path.join(HERE, name + '.json')))
    li = ''.join(f'<li><span class="tk-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="square" stroke-linejoin="miter">{ICONS.get(i["icon"], ICONS["star"])}</svg></span>{('<b>' + html.escape(i["name"]) + '</b> ') if i.get("name") else ''}{html.escape(i["text"])}</li>' for i in d['items'])
    return (f'<section class="proof-row stat-ticker" aria-label="{html.escape(d["heading"])}"><div class="wrap"><div class="eyebrow">{html.escape(d["heading"])}</div></div>'
            f'<div class="marquee"><ul class="mq-track">{li}</ul><ul class="mq-track" aria-hidden="true">{li}</ul></div></section>')

def deliverables(name='deliverables'):
    d = json.load(open(os.path.join(HERE, name + '.json')))
    tiles = ''.join(f'<div class="dl-tile"><div class="dl-top"><span class="tk-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="square" stroke-linejoin="miter">{ICONS.get(i["icon"], ICONS["star"])}</svg></span><span class="dl-cad">{html.escape(i["cadence"])}</span></div><span class="dl-brand">LocalLift&trade;</span><h3>{html.escape(i["name"])}</h3><p>{html.escape(i["text"])}</p></div>' for i in d['items'])
    return (f'<section class="block dl-sec" style="padding-top:0" aria-label="What is inside"><div class="wrap"><div class="eyebrow">{d.get("heading","What&rsquo;s inside LocalLift&trade;")}</div>'
            f'<h2 class="h2">{d.get("title","Ten reports and services. One team running them.")}</h2><div class="dl-grid">{tiles}</div></div></section>')

def communities():
    d = json.load(open(os.path.join(HERE, 'communities.json')))
    items = ''.join(f'<li>{html.escape(n)}</li>' for n in d['items'])
    return ('<section class="proof-row" aria-label="Communities and operators we have worked with"><div class="wrap"><div class="eyebrow">Trusted by communities nationwide</div></div>'
            f'<div class="marquee"><ul class="mq-track">{items}</ul><ul class="mq-track" aria-hidden="true">{items}</ul></div></section>')

def testimonials(group):
    d = json.load(open(os.path.join(HERE, 'testimonials.json')))
    rs = [r for r in d['reviews'] if group in r['vertical'] and r.get('approved', True)]
    if not rs: return ''
    card = lambda r: (f'<figure class="tm-card">{STARS}<blockquote>&ldquo;{html.escape(r["quote"])}&rdquo;</blockquote>'
                      f'<figcaption><b>{html.escape(r["name"])}</b><span>{html.escape(r["role"])} &middot; {"Google review" if r.get("source","google")=="google" else "Client testimonial"}</span></figcaption></figure>')
    cards = ''.join(card(r) for r in rs)
    head = (f'<div class="wrap tm-head"><div><div class="eyebrow">What clients say</div><h2 class="h2">Rated {d["rating"]:.1f} on Google.</h2></div>'
            f'<p class="tm-note">From <a href="https://www.google.com/maps?cid=16697970813285611247" target="_blank" rel="noopener" style="color:inherit;text-decoration:underline">{d["count"]} Google reviews of The SocialDM</a>.</p></div>')
    if len(rs) < 3:
        return f'<section class="block proof-tm" style="padding-top:0">{head}<div class="wrap tm-static">{cards}</div></section>'
    reps = max(1, -(-8 // len(rs)))            # repeat short lists so the loop never shows a gap on wide screens
    track = cards * reps
    dur = round(len(rs) * reps * 4.5)          # same speed whatever the count, about 4.5s per card
    return (f'<section class="block proof-tm" style="padding-top:0">{head}'
            f'<div class="marquee tm-marquee"><div class="mq-track" style="animation-duration:{dur}s">{track}</div><div class="mq-track" aria-hidden="true" style="animation-duration:{dur}s">{track}</div></div></section>')

def render(t):
    t = t.replace('<!--proof:communities-->', ticker())
    t = t.replace('<!--proof:deliverables-->', deliverables())
    t = re.sub(r'<!--proof:ticker:([a-z-]+)-->', lambda m: ticker('ticker-' + m.group(1)), t)
    t = re.sub(r'<!--proof:deliverables:([a-z-]+)-->', lambda m: deliverables('deliverables-' + m.group(1)), t)
    return re.sub(r'<!--proof:testimonials:([a-z-]+)-->', lambda m: testimonials(m.group(1)), t)
