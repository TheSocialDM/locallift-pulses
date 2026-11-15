"""Real estate demo site: Adrienne Fernwick, Fernwick Home Group, Larkspur Vale (all fictional)."""
from samples_kit import page, esc

IND = 'real-estate'
I = '/samples/real-estate/img/'
B = '/samples/real-estate/'
THEME = """:root{--serif:'Cormorant Garamond',Georgia,serif;--sans:'Jost',system-ui,sans-serif;--ink:#1d1b18;--bg:#f6f3ee;--soft:#efe9e0;--line:#ddd5c8;--acc:#b39062;--acc2:#8a6a3f;--accink:#fff;--deep:#1d1b18;--foot:#14130f;--navbg:#f6f3ee;--navink:#1d1b18;--wt:300;--hw:400;--brandls:.04em}
h1,h2{font-weight:300}.brand{font-size:27px}"""
FONTS = 'family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500'
BRAND = 'Adrienne Fernwick<small>Fernwick Home Group</small>'
MENU = [('Listings', B + 'listings/'), ('Neighborhoods', B + 'neighborhoods/'), ('Sell', B + 'sell-home-larkspur-vale/'),
        ('Market report', B + 'market-report/'), ('About', B + 'about/')]
CTA = ('Contact', B + 'contact/')
SAMPLE = 'Sample concept by LocalLift. Adrienne Fernwick, Fernwick Home Group, Larkspur Vale and every listing here are fictional.'

LISTINGS = [
    ('14-heron-point-lane', '14 Heron Point Lane', 'Heron Point', 2495000, 5, '4.5', '4,820', 'For sale', 'lake'),
    ('208-old-mill-row', '208 Old Mill Row', 'Old Mill District', 1185000, 4, '3', '3,140', 'New', 'l2'),
    ('9-larkspur-ridge-court', '9 Larkspur Ridge Court', 'Larkspur Heights', 1640000, 4, '3.5', '3,610', 'For sale', 'l4'),
    ('31-willow-bend-drive', '31 Willow Bend Drive', 'Willow Bend', 895000, 3, '2.5', '2,280', 'Coming soon', 'l1'),
    ('77-shoreline-way', '77 Shoreline Way', 'Heron Point', 3150000, 6, '5.5', '5,900', 'For sale', 'l7'),
    ('412-granary-street', '412 Granary Street', 'Old Mill District', 729000, 3, '2', '1,960', 'Pending', 'l8'),
    ('5-meadowlark-lane', '5 Meadowlark Lane', 'Willow Bend', 1045000, 4, '3', '2,950', 'For sale', 'l6'),
    ('60-summit-pass', '60 Summit Pass', 'Larkspur Heights', 1395000, 4, '3.5', '3,380', 'Sold', 'l3'),
]

HOODS = [
    ('heron-point', 'Heron Point', 'water', 'Lakefront streets, boat slips and long evening light.'),
    ('old-mill-district', 'Old Mill District', 'street', 'Brick lofts, the Saturday market and everything on foot.'),
    ('larkspur-heights', 'Larkspur Heights', 'dusk', 'Hillside homes with valley views and quiet cul-de-sacs.'),
    ('willow-bend', 'Willow Bend', 'l6', 'Tree-lined streets, big yards and the river trail.'),
]


def hood_href(s):
    return B + 'neighborhoods/' + s + '/' if s in ('heron-point', 'old-mill-district') else B + 'listings/'


def money(n):
    return '${:,}'.format(n)


def card(l, big=False):
    slug, addr, hood, price, bd, ba, sq, st, img = l
    href = B + 'listings/14-heron-point-lane/' if slug == '14-heron-point-lane' else B + 'listings/#' + slug
    return (f'<a class="card reveal" id="{slug}" href="{href}"><div class="ph"><span class="pill">{st}</span>'
            f'<button class="save" aria-label="Save {esc(addr)}">&#9825;</button>'
            f'<img src="{I}{img}.jpg" alt="Exterior of {esc(addr)}" loading="lazy"></div>'
            f'<div class="price" style="margin-top:16px">{money(price)}</div><h3 style="margin:2px 0 4px">{esc(addr)}</h3>'
            f'<div class="meta"><span style="white-space:nowrap">{hood.upper()}</span> &nbsp;|&nbsp; <span style="white-space:nowrap">{bd} BD</span> &nbsp;|&nbsp; <span style="white-space:nowrap">{ba} BA</span> &nbsp;|&nbsp; <span style="white-space:nowrap">{sq} SQ FT</span></div></a>')


def foot():
    return f"""<footer><div class="cols">
<div><div class="brand" style="color:#fff">{BRAND}</div><p style="margin-top:16px;max-width:340px;opacity:.8">Homes in Larkspur Vale and the lake towns around it. Brokerage name, office address and license number go here.</p></div>
<div><h4>Explore</h4><a href="{B}listings/">Listings</a><a href="{B}neighborhoods/">Neighborhoods</a><a href="{B}market-report/">Market report</a></div>
<div><h4>Sellers</h4><a href="{B}sell-home-larkspur-vale/">Selling in Larkspur Vale</a><a href="{B}sell-home-larkspur-vale/#value">Home value</a></div>
<div><h4>Contact</h4><a href="{B}contact/">Send a note</a><a href="{B}about/">About Adrienne</a></div></div>
<div class="legal"><span>Equal Housing Opportunity. We follow fair housing laws and serve every buyer and seller equally.</span><span>Sample site concept by LocalLift, a SocialDM company. Not a real brokerage.</span></div></footer>"""


def agent_schema():
    return {"@context": "https://schema.org", "@type": "RealEstateAgent", "name": "Adrienne Fernwick (sample)",
            "description": "Fictional sample agent site built by LocalLift to show the format.",
            "areaServed": "Larkspur Vale (fictional)", "url": "https://www.thesocialdm.com/samples/real-estate/"}


def faq_schema(qs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}


def faq_html(qs):
    return ''.join(f'<details{" open" if i == 0 else ""}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for i, (q, a) in enumerate(qs))


def P(path, title, desc, body, schema=None, over=False, extra_css='', extra_js=''):
    page(IND, path, title=title + ' | Sample concept by LocalLift', desc=desc, theme_css=THEME, fonts=FONTS,
         brand_html=BRAND, menu=MENU, cta=CTA, body=body, footer_html=foot(), schema=schema, over=over,
         extra_css=extra_css, extra_js=extra_js, sample_line=SAMPLE)


SEARCH_CSS = """
.search{display:grid;grid-template-columns:2fr 1fr 1fr auto;gap:0;background:#fff;max-width:880px;box-shadow:0 20px 50px rgba(0,0,0,.25)}
.search input,.search select{border:0;border-right:1px solid #e5ded3;padding:20px 18px;font:400 15px var(--sans);color:#222;background:#fff;width:100%}
.search .btn{border-radius:0}
.hood{position:relative;display:block;aspect-ratio:3/4;overflow:hidden;color:#fff}
.hood img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.4s}
.hood:hover img{transform:scale(1.06)}
.hood:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.7))}
.hood>div{position:absolute;left:24px;right:24px;bottom:24px;z-index:2}
.hood h3{font-size:30px}.hood p{font-size:14px;opacity:.9;margin-top:6px}
.post .ph{aspect-ratio:16/11}.post h3{font-size:24px;margin:14px 0 6px}
.gram{display:grid;grid-template-columns:repeat(6,1fr);gap:4px}.gram .ph{aspect-ratio:1}
@media(max-width:900px){.search{grid-template-columns:1fr}.search input,.search select{border-right:0;border-bottom:1px solid #e5ded3}.gram{grid-template-columns:repeat(3,1fr)}}
"""


def home():
    feat = ''.join(card(l) for l in LISTINGS[:4])
    hoods = ''.join(f'<a class="hood reveal" href="{hood_href(s)}"><img src="{I}{im}.jpg" alt="{n} in Larkspur Vale" loading="lazy"><div><div class="eyebrow" style="color:#fff;opacity:.8">Neighborhood</div><h3>{n}</h3><p>{t}</p></div></a>' for s, n, im, t in HOODS)
    posts = [('market-report/', 'dusk', 'Market report', 'What sold in Larkspur Vale this month, and what it means for your price'),
             ('sell-home-larkspur-vale/', 'in1', 'Selling', 'How to sell a home in Larkspur Vale, step by step'),
             ('neighborhoods/heron-point/', 'water', 'Neighborhoods', 'Living on the lake in Heron Point: docks, trails and what homes cost')]
    ph = ''.join(f'<a class="post reveal" href="{B}{h}"><div class="ph"><img src="{I}{im}.jpg" alt="" loading="lazy"></div><div class="eyebrow" style="margin-top:16px">{e}</div><h3>{t}</h3><span class="meta">READ &rarr;</span></a>' for h, im, e, t in posts)
    gram = ''.join(f'<div class="ph"><img src="{I}{k}.jpg" alt="" loading="lazy"></div>' for k in ['in2', 'resort', 'in3', 'l7', 'in4', 'sunset'])
    body = f"""
<section class="hero" style="padding:0"><div class="bg" style="background-image:url({I}hero.jpg)"></div>
<div class="in"><div class="eyebrow" style="color:#fff;opacity:.85">Larkspur Vale &nbsp;&middot;&nbsp; Lake towns &nbsp;&middot;&nbsp; Luxury homes</div>
<h1>Homes with a <i>sense of place.</i></h1><p>Adrienne Fernwick and Fernwick Home Group represent buyers and sellers across Larkspur Vale, from lakefront estates to Old Mill lofts.</p>
<form class="search" data-demo onsubmit="location.href='{B}listings/';return false"><input aria-label="City, neighborhood or address" placeholder="City, neighborhood or address"><select aria-label="Price"><option>Any price</option><option>$750K+</option><option>$1M+</option><option>$2M+</option></select><select aria-label="Beds"><option>Any beds</option><option>3+</option><option>4+</option><option>5+</option></select><button class="btn">Search</button></form></div>
<span class="tag">Stock photo. Client photos go here.</span></section>

<section><div class="wrap split">
<div class="ph reveal" style="aspect-ratio:4/5"><img src="{I}agent.jpg" alt="Portrait of the agent (stock photo stand in)" loading="lazy"></div>
<div class="reveal"><div class="eyebrow">Meet Adrienne</div><h2>Twenty years of Larkspur Vale, <i>street by street.</i></h2>
<p class="lead">Adrienne grew up three blocks from the lake and has sold homes in every corner of the valley. Clients hire her for two things: a price she can explain, and a plan that gets a home seen by serious buyers from day one.</p>
<p style="margin:26px 0 30px"><a class="btn dark" href="{B}about/">Her story</a> &nbsp; <a class="btn line" href="{B}contact/">Start a conversation</a></p></div></div></section>

<div class="stats wrap"><div><b>$412M</b><span>Sold, career</span></div><div><b>640+</b><span>Homes closed</span></div><div><b>21</b><span>Days on market, median</span></div><div><b>101%</b><span>Of list price, average</span></div></div>
<p class="note wrap" style="padding:10px 5vw 0">Sample figures for a fictional agent. Real numbers come from the client's own records.</p>

<section><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><div><div class="eyebrow">Featured properties</div><h2>On the market now</h2></div><a class="btn line" href="{B}listings/">All listings</a></div>
<div class="grid g4" style="margin-top:30px">{feat}</div></div></section>

<div class="marquee"><span>Heron Point &nbsp;&middot;&nbsp; Old Mill District &nbsp;&middot;&nbsp; Larkspur Heights &nbsp;&middot;&nbsp; Willow Bend &nbsp;&middot;&nbsp; Lakefront &nbsp;&middot;&nbsp; Historic lofts &nbsp;&middot;&nbsp; Hillside views &nbsp;&middot;&nbsp; New construction</span></div>

<section><div class="wrap"><div class="eyebrow">Neighborhood guides</div><h2>Find your corner of the valley</h2><p class="lead">Every neighborhood gets its own guide with what it costs, what it feels like and what is selling right now. These are the pages search engines and AI assistants quote.</p>
<div class="grid g4" style="margin-top:36px">{hoods}</div></div></section>

<section class="band" style="padding:0"><div class="split" style="gap:0"><div class="ph" style="min-height:520px"><img src="{I}in1.jpg" alt="Bright living room" loading="lazy"></div>
<div style="padding:clamp(48px,7vw,100px)"><div class="eyebrow">For sellers</div><h2 style="color:#fff">What is your home <i>really</i> worth?</h2><p class="lead" style="opacity:.85">Not an automated guess. A written value from Adrienne with the recent sales behind it, usually within one business day.</p>
<form class="form" data-demo style="margin-top:26px;max-width:460px"><input placeholder="Home address" aria-label="Home address"><div class="row"><input placeholder="Name" aria-label="Name"><input placeholder="Email" aria-label="Email"></div><button class="btn">Request my home value</button><p class="ok note" hidden>Sample form. On a live site this goes to the agent's own system.</p></form></div></div></section>

<section><div class="wrap"><div class="eyebrow">Insights</div><h2>Straight answers about this market</h2><div class="grid g3" style="margin-top:30px">{ph}</div></div></section>

<section style="padding-top:0"><div class="wrap"><div style="display:flex;justify-content:space-between;align-items:end;margin-bottom:18px"><div><div class="eyebrow">Follow along</div><h3 style="margin-top:8px">@adriennefernwick (sample)</h3></div></div><div class="gram">{gram}</div></div></section>

<section class="band" style="text-align:center"><div class="wrap"><div class="eyebrow">Let's talk</div><h2 style="color:#fff;max-width:800px;margin:12px auto 18px">Thinking about a move in the next year?</h2><p class="lead" style="margin:0 auto 30px">A no-pressure conversation about timing, price and what to fix first.</p><a class="btn" href="{B}contact/">Schedule a call</a></div></section>"""
    P('', 'Adrienne Fernwick | Larkspur Vale Luxury Homes', 'Sample agent website concept: luxury homes, neighborhood guides and home values in Larkspur Vale (fictional).',
      body, schema=[agent_schema()], over=True, extra_css=SEARCH_CSS)


def listings():
    allc = ''.join(card(l) for l in LISTINGS)
    body = f"""<section style="padding-bottom:30px"><div class="wrap"><div class="crumbs"><a href="{B}">Home</a> / Listings</div><div class="eyebrow">Properties</div><h2>Homes for sale in Larkspur Vale</h2>
<p class="lead">On a live site this page connects to the agent's IDX feed so visitors can filter, save and share. These eight are samples.</p>
<form class="search" data-demo style="margin-top:28px;box-shadow:none;border:1px solid var(--line)"><input placeholder="Neighborhood or address" aria-label="Neighborhood or address"><select aria-label="Price"><option>Any price</option><option>$750K+</option><option>$1M+</option><option>$2M+</option></select><select aria-label="Beds"><option>Any beds</option><option>3+</option><option>4+</option></select><button class="btn">Filter</button></form></div></section>
<section style="padding-top:20px"><div class="wrap grid g4">{allc}</div></section>"""
    P('listings', 'Homes for sale in Larkspur Vale', 'Sample listings page for a fictional luxury real estate agent.', body, extra_css=SEARCH_CSS)


def listing_detail():
    l = LISTINGS[0]
    gal = ''.join(f'<div class="ph"><img src="{I}{k}.jpg" alt="Interior photo {i+1}" loading="lazy"></div>' for i, k in enumerate(['in1', 'in2', 'in3', 'in5']))
    feats = ['Infinity edge pool and spa', 'Private dock with boat lift', 'Chef kitchen with butler pantry', 'Primary suite with lake views',
             'Three car garage', 'Whole home generator', 'Wine room', 'Guest suite with private entry', 'Smart lighting and shades', 'Built 2019']
    fl = ''.join(f'<li>{f}</li>' for f in feats)
    css = """.gal{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:260px 260px;gap:6px}
.gal .ph:first-child{grid-row:span 2}.gal img{height:100%}
.facts{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line);margin:26px 0}
.facts div{padding:18px;border-right:1px solid var(--line)}.facts div:last-child{border:0}.facts b{display:block;font-family:var(--serif);font-size:28px;font-weight:400}
.side{position:sticky;top:96px;background:#fff;border:1px solid var(--line);padding:30px}
.calc label{font-size:12px;letter-spacing:.14em;text-transform:uppercase;opacity:.7}
.pay{font-family:var(--serif);font-size:40px;margin:8px 0}
.lay{display:grid;grid-template-columns:1.6fr 1fr;gap:56px;align-items:start}
@media(max-width:900px){.gal{grid-template-columns:1fr 1fr;grid-template-rows:200px 140px 140px}.gal .ph:first-child{grid-column:span 2;grid-row:auto}.facts{grid-template-columns:1fr 1fr}.lay{grid-template-columns:1fr}.side{position:static}}"""
    js = """var f=document.getElementById('calc');if(f){var go=function(){var p=+f.price.value,d=+f.down.value/100,r=+f.rate.value/100/12,n=360,L=p*(1-d);var m=r?L*r/(1-Math.pow(1+r,-n)):L/n;document.getElementById('pay').textContent='$'+Math.round(m).toLocaleString();};f.addEventListener('input',go);go();}"""
    body = f"""<section style="padding-bottom:24px"><div class="wrap"><div class="crumbs"><a href="{B}">Home</a> / <a href="{B}listings/">Listings</a> / {l[1]}</div>
<div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><div><div class="eyebrow">{l[2]} &nbsp;&middot;&nbsp; For sale</div><h2 style="margin-bottom:0">{l[1]}</h2></div><div class="price" style="font-size:42px">{money(l[3])}</div></div></div></section>
<div class="wrap" style="padding:0 5vw"><div class="gal"><div class="ph"><img src="{I}lake.jpg" alt="{l[1]} from the lake"></div>{gal}</div></div>
<section style="padding-top:40px"><div class="wrap lay"><div>
<div class="facts"><div><b>5</b>Bedrooms</div><div><b>4.5</b>Baths</div><div><b>4,820</b>Sq ft</div><div><b>0.9</b>Acres</div></div>
<div class="short"><b>The short answer</b>A 2019 lakefront home in Heron Point with a private dock, pool and five bedrooms, listed at {money(l[3])}. Tours by appointment.</div>
<p class="lead" style="max-width:none">Set on almost an acre at the quiet end of Heron Point, this home opens straight onto the water. Walls of glass slide away to a terrace and infinity pool, and the dock sits a short walk across the lawn. Inside, the kitchen, family room and dining room share one long view of the lake.</p>
<h3 style="margin:40px 0 14px">Features</h3><ul class="list">{fl}</ul>
<h3 style="margin:40px 0 14px">Questions buyers ask</h3>{faq_html([('What are the HOA dues?','Heron Point has an optional lake association. The amount on a live listing comes straight from the MLS record.'),('Can the dock fit a wake boat?','The lift is rated for most ski and wake boats. Exact capacity is listed in the seller disclosures.'),('Which schools serve this address?','School boundaries change. Confirm with the school district before you buy.')])}
</div>
<aside class="side"><div class="eyebrow">Schedule a private tour</div><form class="form" data-demo style="margin:16px 0 28px"><input placeholder="Name" aria-label="Name"><input placeholder="Email or phone" aria-label="Email or phone"><select aria-label="Preferred day"><option>This week</option><option>Next week</option></select><button class="btn dark">Request a tour</button><p class="ok note" hidden>Sample form. On a live site this goes to the agent's own system.</p></form>
<form id="calc" class="calc"><div class="eyebrow">Monthly payment estimate</div><div class="pay" id="pay">$0</div><p class="note" style="margin:0 0 14px">Principal and interest only, 30 year fixed. For illustration.</p>
<label>Price<input class="form" style="display:block;width:100%;padding:12px;border:1px solid var(--line);margin:6px 0 12px" name="price" type="number" value="{l[3]}"></label>
<label>Down payment %<input style="display:block;width:100%;padding:12px;border:1px solid var(--line);margin:6px 0 12px" name="down" type="number" value="20"></label>
<label>Rate %<input style="display:block;width:100%;padding:12px;border:1px solid var(--line);margin:6px 0 0" name="rate" type="number" step="0.05" value="6.5"></label></form></aside></div></section>
<section style="padding-top:0"><div class="wrap"><div class="eyebrow">More from Fernwick Home Group</div><h2>You may also like</h2><div class="grid g4" style="margin-top:24px">{card(LISTINGS[4])}{card(LISTINGS[2])}{card(LISTINGS[1])}{card(LISTINGS[6])}</div></div></section>"""
    sch = {"@context": "https://schema.org", "@type": "SingleFamilyResidence", "name": l[1] + " (sample)", "numberOfRooms": 5,
           "floorSize": {"@type": "QuantitativeValue", "value": 4820, "unitCode": "FTK"}}
    P('listings/14-heron-point-lane', l[1] + ', Heron Point', 'Sample listing page with gallery, tour request and payment estimate.', body,
      schema=[sch], extra_css=css, extra_js=js)


HOOD_DETAIL = {
    'heron-point': dict(img='water', lede='Heron Point wraps the north shore of Larkspur Lake. Most homes sit on half acre lots with private docks or deeded lake access, and evenings here are about the water.',
        glance=[('Median sale price', '$2.1M'), ('Days on market', '24'), ('Homes sold, 12 months', '38'), ('Lake access', 'Most lots')],
        life=['Two public boat launches and a marina with fuel', 'Lakeshore trail that runs 6 miles to the Old Mill District', 'Sunset Point park with a swim beach', 'About 12 minutes to downtown Larkspur Vale'],
        faqs=[('How much do homes in Heron Point cost?', 'Over the last 12 months the median sale was about $2.1M in this sample. Waterfront homes with docks sell at the top of that range.'),
              ('Do all Heron Point homes have lake access?', 'Most lots have a private dock or deeded access. Interior streets may not, so check each listing.'),
              ('Are there rules about docks and boats?', 'The lake association sets dock and wake rules. Ask for the current rules before you make an offer.')]),
    'old-mill-district': dict(img='street', lede='The Old Mill District is the historic heart of Larkspur Vale. Brick mill buildings became lofts, the granary became a market hall, and almost everything is a short walk.',
        glance=[('Median sale price', '$840K'), ('Days on market', '17'), ('Homes sold, 12 months', '71'), ('Walk to market', 'Yes')],
        life=['Saturday farmers market in the Granary Hall', 'Restaurants, coffee and galleries along Mill Street', 'Riverfront park and amphitheater', 'Lofts, townhomes and restored 1920s homes'],
        faqs=[('What kinds of homes are in the Old Mill District?', 'Converted lofts, newer townhomes and restored older homes on small lots.'),
              ('Is parking an issue?', 'Many lofts include one deeded space. Street parking is limited on market days.'),
              ('Are there historic rules for renovations?', 'Parts of the district have design guidelines. Check with the city before planning exterior changes.')]),
}


def neighborhoods():
    tiles = ''.join(f'<a class="hood reveal" href="{hood_href(s)}"><img src="{I}{im}.jpg" alt="{n}" loading="lazy"><div><h3>{n}</h3><p>{t}</p></div></a>' for s, n, im, t in HOODS)
    body = f"""<section><div class="wrap"><div class="crumbs"><a href="{B}">Home</a> / Neighborhoods</div><div class="eyebrow">Guides</div><h2>Larkspur Vale neighborhoods</h2><p class="lead">One honest guide per neighborhood: what homes cost, how fast they sell and what living there is actually like.</p><div class="grid g4" style="margin-top:36px">{tiles}</div>
<p class="note" style="margin-top:18px">On this sample, Heron Point and Old Mill District have full guides.</p></div></section>"""
    P('neighborhoods', 'Larkspur Vale neighborhood guides', 'Sample neighborhood guide hub for a fictional luxury agent.', body, extra_css=SEARCH_CSS)
    for s, n, im, t in HOODS:
        if s not in HOOD_DETAIL:
            continue
        d = HOOD_DETAIL[s]
        nm = 'the ' + n if s == 'old-mill-district' else n
        gl = ''.join(f'<div><b>{v}</b><span>{k}</span></div>' for k, v in d['glance'])
        lf = ''.join(f'<li>{x}</li>' for x in d['life'])
        hl = ''.join(card(l) for l in LISTINGS if l[2] == n)
        body = f"""<section class="hero" style="padding:0;min-height:70vh"><div class="bg" style="background-image:url({I}{d['img']}.jpg)"></div><div class="in"><div class="crumbs" style="opacity:.9"><a href="{B}">Home</a> / <a href="{B}neighborhoods/">Neighborhoods</a> / {n}</div><div class="eyebrow" style="color:#fff;opacity:.85">Neighborhood guide</div><h1>Living in {nm}</h1></div><span class="tag">Stock photo</span></section>
<section><div class="wrap"><div class="short"><b>The short answer</b>{d['lede']}</div></div>
<div class="stats wrap" style="margin-top:30px">{gl}</div><p class="note wrap">Sample figures for a fictional town. A live guide updates these from the MLS each month.</p></section>
<section style="padding-top:0"><div class="wrap split"><div class="reveal"><div class="eyebrow">Everyday life</div><h2>What it is like</h2><ul class="list" style="columns:1">{lf}</ul></div><div class="ph reveal" style="aspect-ratio:4/5"><img src="{I}{'resort' if s=='heron-point' else 'in5'}.jpg" alt="" loading="lazy"></div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="eyebrow">Homes in {n}</div><h2>On the market</h2><div class="grid g4" style="margin-top:24px">{hl}</div></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>Buying in {nm}</h2></div><div>{faq_html(d['faqs'])}<p class="note" style="margin-top:18px">School boundaries change. Confirm with the school district before you buy.</p></div></div></section>"""
        P('neighborhoods/' + s, f'Living in {nm}, Larkspur Vale', f'Sample neighborhood guide for {n} (fictional).', body, schema=[faq_schema(d['faqs'])], over=False, extra_css=SEARCH_CSS)


def sell():
    faqs = [('How do you price a home in Larkspur Vale?', 'Adrienne compares the most recent sales near you, adjusts for size, condition and view, and walks you through every home she used so the number makes sense.'),
            ('How long does it take to sell?', 'In this sample market the median home sold in 21 days. Price, condition and season move that number, and you see the recent comparisons before you list.'),
            ('Do I need to stage my home?', 'Not always. You get a room-by-room list of what is worth doing and what is not.'),
            ('What does it cost to sell?', 'Commission and closing costs are explained in writing before you sign anything. Commissions are negotiable.'),
            ('Can you sell my home privately?', 'Yes, where MLS rules allow. Some sellers prefer a quiet, off-market sale to a short list of qualified buyers first.')]
    steps = [('Value and plan', 'A written price range with the sales behind it, plus a prep list and timeline.'), ('Prepare', 'Repairs, styling and cleaning coordinated with trusted local vendors.'),
             ('Photograph and film', 'Twilight photos, video and a floor plan that make the home stand out online.'), ('Launch', 'Private preview to buyer agents, then the open market, search and social.'),
             ('Negotiate and close', 'Offers compared side by side, then every deadline handled to closing day.')]
    st = ''.join(f'<li><div><b>{a}</b>{b}</div></li>' for a, b in steps)
    body = f"""<section class="hero" style="padding:0;min-height:76vh"><div class="bg" style="background-image:url({I}l4.jpg)"></div><div class="in"><div class="crumbs"><a href="{B}">Home</a> / Sell</div><div class="eyebrow" style="color:#fff;opacity:.85">Selling in Larkspur Vale</div><h1>Sell for the right price, <i>with a plan you can see.</i></h1><p>How Adrienne prices, prepares and markets homes in Larkspur Vale, and what you can expect at every step.</p><a class="btn" href="#value">Get my home value</a></div><span class="tag">Stock photo</span></section>
<section><div class="wrap"><div class="short"><b>The short answer</b>To sell a home in Larkspur Vale, start with a written value based on recent nearby sales, fix only what buyers will pay for, and launch with strong photos and a private preview. In this sample market, homes sold in a median of 21 days.</div></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">The process</div><h2>Five steps, start to close</h2><p class="lead">You always know what happens next and who is doing it.</p></div><ol class="steps">{st}</ol></div></section>
<section class="band" style="padding:0"><div class="split" style="gap:0"><div class="ph" style="min-height:460px"><img src="{I}in3.jpg" alt="Styled living room" loading="lazy"></div><div style="padding:clamp(48px,7vw,100px)"><div class="eyebrow">Marketing</div><h2 style="color:#fff">Seen by serious buyers first</h2><ul class="list" style="columns:1;border-color:rgba(255,255,255,.2)"><li>Twilight photography and video</li><li>Private preview to local buyer agents</li><li>Listing pages ready for search and AI</li><li>Social campaigns that reach active buyers</li><li>Weekly showing and feedback report</li></ul></div></div></section>
<section id="value"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Home value</div><h2>Request a written value</h2><p class="lead">A real person, not an algorithm. Usually within one business day.</p></div>
<form class="form" data-demo><input placeholder="Home address" aria-label="Home address"><div class="row"><input placeholder="Name" aria-label="Name"><input placeholder="Email" aria-label="Email"></div><div class="row"><select aria-label="Timing"><option>Selling in 0 to 3 months</option><option>3 to 12 months</option><option>Just curious</option></select><input placeholder="Phone (optional)" aria-label="Phone"></div><button class="btn dark">Send my request</button><p class="ok note" hidden>Sample form. On a live site this goes to the agent's own system.</p></form></div></section>
<section style="padding-top:0"><div class="wrap split" style="align-items:start"><div><div class="eyebrow">Questions</div><h2>What sellers ask first</h2></div><div>{faq_html(faqs)}</div></div></section>"""
    P('sell-home-larkspur-vale', 'Selling a home in Larkspur Vale', 'Sample seller landing page: pricing, process, marketing and FAQs (fictional).', body, schema=[faq_schema(faqs)])


def market():
    months = ['Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
    vals = [912, 898, 905, 931, 958, 984, 1002, 996, 981, 973, 968, 979]
    mx = 1050
    w, h = 720, 260
    bw = w / len(vals)
    bars = ''
    for i, v in enumerate(vals):
        bh = (v - 800) / (mx - 800) * (h - 30)
        x = i * bw + 8
        bars += f'<rect x="{x:.0f}" y="{h-20-bh:.0f}" width="{bw-16:.0f}" height="{bh:.0f}" fill="{"#b39062" if i==11 else "#d9cbb5"}"/>{'<text x="%.0f" y="%.0f" font-size="12" text-anchor="middle" fill="#1d1b18">$979K</text>' % (x+(bw-16)/2, h-26-bh) if i==11 else ''}<text x="{x+(bw-16)/2:.0f}" y="{h-4}" font-size="11" text-anchor="middle" fill="#6d655a">{months[i]}</text>'
    svg = f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Median sale price by month, sample figures" style="width:100%;height:auto">{bars}</svg>'
    rows = [('Heron Point', '$2.10M', '24', '38'), ('Old Mill District', '$840K', '17', '71'), ('Larkspur Heights', '$1.38M', '22', '44'), ('Willow Bend', '$965K', '19', '57')]
    tr = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in rows)
    css = """table{width:100%;border-collapse:collapse;font-size:15px}th,td{text-align:left;padding:14px 10px;border-bottom:1px solid var(--line)}th{font:500 11px var(--sans);letter-spacing:.18em;text-transform:uppercase;opacity:.7}"""
    body = f"""<section style="padding-bottom:20px"><div class="wrap"><div class="crumbs"><a href="{B}">Home</a> / Market report</div><div class="eyebrow">October market report</div><h2>The Larkspur Vale market, in one page</h2>
<div class="short"><b>The short answer</b>The median home in Larkspur Vale sold for about $979K in October, up 7 percent from a year ago, and homes sold in a median of 21 days.</div>
<p class="note">Sample figures for a fictional town. A live report is refreshed every month from local MLS data.</p></div></section>
<div class="stats wrap"><div><b>$979K</b><span>Median sale price</span></div><div><b>+7%</b><span>Year over year</span></div><div><b>21</b><span>Median days on market</span></div><div><b>2.4</b><span>Months of supply</span></div></div>
<section><div class="wrap"><h3>Median sale price, last 12 months (thousands)</h3><div style="margin-top:20px">{svg}</div></div></section>
<section style="padding-top:0"><div class="wrap"><h3 style="margin-bottom:14px">By neighborhood</h3><table><tr><th>Neighborhood</th><th>Median price</th><th>Days on market</th><th>Sold, 12 months</th></tr>{tr}</table>
<p style="margin-top:34px"><a class="btn dark" href="{B}sell-home-larkspur-vale/#value">What does this mean for my home?</a></p></div></section>"""
    P('market-report', 'Larkspur Vale real estate market report', 'Sample monthly market report page with chart and neighborhood table (fictional figures).', body, extra_css=css)


def about():
    body = f"""<section><div class="wrap split"><div class="ph reveal" style="aspect-ratio:4/5"><img src="{I}agent.jpg" alt="Portrait (stock photo stand in)"></div>
<div><div class="crumbs"><a href="{B}">Home</a> / About</div><div class="eyebrow">About</div><h2>Adrienne Fernwick</h2><p class="lead">Adrienne started selling homes in Larkspur Vale in 2006 after a decade in architecture. She still reads a floor plan before a price sheet, and her clients say it shows.</p>
<p style="margin-top:18px;opacity:.88">Today she leads Fernwick Home Group, a small team that handles every detail of a sale or purchase, from pre-listing repairs to the final walkthrough. She serves on the Larkspur Lake Trust board and spends Saturdays at the Granary market.</p>
<p style="margin-top:28px"><a class="btn dark" href="{B}contact/">Work with Adrienne</a></p></div></div></section>
<section class="band"><div class="wrap grid g3"><div><div class="eyebrow">Approach</div><h3 style="margin-top:12px">Prices you can follow</h3><p style="opacity:.8;margin-top:10px">Every value comes with the sales behind it.</p></div><div><div class="eyebrow">Marketing</div><h3 style="margin-top:12px">Built for how buyers search</h3><p style="opacity:.8;margin-top:10px">Search, AI assistants, social and the agent network.</p></div><div><div class="eyebrow">Service</div><h3 style="margin-top:12px">One team, start to close</h3><p style="opacity:.8;margin-top:10px">Same people from the first call to closing day.</p></div></div></section>
<p class="note wrap" style="padding:16px 5vw 40px">Adrienne Fernwick is a fictional agent created to show the format. Real bios, credentials and reviews come from the client.</p>"""
    P('about', 'About Adrienne Fernwick', 'Sample agent bio page (fictional).', body, schema=[agent_schema()])


def contact():
    body = f"""<section><div class="wrap split" style="align-items:start"><div><div class="crumbs"><a href="{B}">Home</a> / Contact</div><div class="eyebrow">Contact</div><h2>Start a conversation</h2><p class="lead">Buying, selling or just curious about your home's value. Adrienne replies personally, usually the same day.</p>
<p style="margin-top:26px;line-height:2">Office address goes here<br>Phone goes here<br>Email goes here</p></div>
<form class="form" data-demo><div class="row"><input placeholder="First name" aria-label="First name"><input placeholder="Last name" aria-label="Last name"></div><input placeholder="Email" aria-label="Email"><select aria-label="Topic"><option>I am buying</option><option>I am selling</option><option>Both</option><option>Something else</option></select><textarea rows="5" placeholder="Message" aria-label="Message"></textarea><button class="btn dark">Send</button><p class="ok note" hidden>Sample form. On a live site this goes to the agent's own system.</p></form></div></section>
<div class="ph" style="height:420px"><img src="{I}lake.jpg" alt="Lakeside homes at sunrise" loading="lazy"></div>"""
    P('contact', 'Contact Adrienne Fernwick', 'Sample contact page (fictional).', body)


if __name__ == '__main__':
    home(); listings(); listing_detail(); neighborhoods(); sell(); market(); about(); contact()
    print('real estate done')
