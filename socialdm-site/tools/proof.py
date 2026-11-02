"""Social proof blocks injected into static pages at build time.
<!--proof:communities-->            scrolling row of communities and operators (tools/communities.json, logos in tools/logos/ when supplied)
<!--proof:testimonials:<group>-->   scrolling Google review quotes (tools/testimonials.json) for home, multifamily, real-estate ..."""
import html, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
STARS = '<span class="tm-stars" aria-label="5 out of 5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span>'

def communities():
    d = json.load(open(os.path.join(HERE, 'communities.json')))
    items = ''.join(f'<li>{html.escape(n)}</li>' for n in d['items'])
    return ('<section class="proof-row" aria-label="Communities and operators we have worked with"><div class="wrap"><div class="eyebrow">Trusted by communities across five states</div></div>'
            f'<div class="marquee"><ul class="mq-track">{items}</ul><ul class="mq-track" aria-hidden="true">{items}</ul></div></section>')

def testimonials(group):
    d = json.load(open(os.path.join(HERE, 'testimonials.json')))
    rs = [r for r in d['reviews'] if group in r['vertical']]
    if not rs: return ''
    card = lambda r: (f'<figure class="tm-card">{STARS}<blockquote>&ldquo;{html.escape(r["quote"])}&rdquo;</blockquote>'
                      f'<figcaption><b>{html.escape(r["name"])}</b><span>{html.escape(r["role"])} &middot; Google review</span></figcaption></figure>')
    cards = ''.join(card(r) for r in rs)
    head = (f'<div class="wrap tm-head"><div><div class="eyebrow">What clients say</div><h2 class="h2">Rated {d["rating"]:.1f} on Google.</h2></div>'
            f'<p class="tm-note">From {d["count"]} Google reviews of The SocialDM.</p></div>')
    if len(rs) < 3:
        return f'<section class="block proof-tm" style="padding-top:0">{head}<div class="wrap tm-static">{cards}</div></section>'
    return (f'<section class="block proof-tm" style="padding-top:0">{head}'
            f'<div class="marquee tm-marquee"><div class="mq-track">{cards}</div><div class="mq-track" aria-hidden="true">{cards}</div></div></section>')

def render(t):
    t = t.replace('<!--proof:communities-->', communities())
    return re.sub(r'<!--proof:testimonials:([a-z-]+)-->', lambda m: testimonials(m.group(1)), t)
