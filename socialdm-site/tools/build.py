#!/usr/bin/env python3
"""Builds thesocialdm.com from the static draft pages, the Squarespace export and new post JSON files.
usage: build.py SRC EXPORT_JSON IMAGES_JSON NEW_POSTS_DIR OUT [--prod]
--prod: clean root URLs, no draft badge, indexable. Default: preview with relative .html links, noindex."""
import base64, datetime, glob, html, json, os, re, shutil, sys
from bs4 import BeautifulSoup, NavigableString

SRC, EXPORT, IMAGES, NEW, OUT = sys.argv[1:6]
PROD = '--prod' in sys.argv
SITE = 'https://www.thesocialdm.com'
d = json.load(open(EXPORT))
imgs = json.load(open(IMAGES))
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/blog'); os.makedirs(OUT + '/images/blog'); os.makedirs(OUT + '/apartment-seo-blog-hub')
report = {'unmapped_links': set(), 'used_images': set(), 'missing_images': set(), 'text_diffs': []}

def undash(s):
    """House rule: no em or en dashes in visible copy."""
    s = re.sub(r'\s*[—–]\s*', ', ', s)
    return s.replace(',,', ',')

def local_image(u):
    u = u.split('?')[0]
    if u not in imgs:
        report['missing_images'].add(u); return None
    name = re.sub(r'[^a-z0-9.-]+', '-', html.unescape(u.rsplit('/', 1)[-1]).lower()).strip('-')
    name = re.sub(r'\.[a-z0-9]+$', '', name)[:70] or 'image'
    tag = re.search(r'/(\d{10,})-', u)
    if tag: name += '-' + tag.group(1)[-5:]
    path = f'images/blog/{name}.jpg'
    if not os.path.exists(f'{OUT}/{path}'):
        open(f'{OUT}/{path}', 'wb').write(base64.b64decode(imgs[u]['jpg']))
    report['used_images'].add(u)
    return path, imgs[u]['w'], imgs[u]['h']

POST_SLUGS = {p['fullUrl'].split('/blog/')[1] for p in d['posts']}
PAGE_MAP = {'': 'index', '/': 'index', '/contact': 'contact', '/about': 'about', '/locallift': 'locallift', '/blog': 'blog',
  '/research-insights': 'research-insights', '/multifamily-marketing-agency': 'multifamily-marketing-agency',
  '/apartment-seo-for-multifamily-communities': 'apartment-seo-for-multifamily-communities', '/medical': 'medical',
  '/hospitality': 'hospitality', '/enterprise': 'enterprise', '/new-page': 'real-estate', '/real-estate': 'real-estate', '/med-spa': 'med-spa', '/hair-salon': 'hair-salon',
  '/2026-multifamily-visibility-report': '2026-multifamily-visibility-report', '/montage-tigard': 'montage-tigard',
  '/pillar-communities': 'pillar-communities', '/home': 'index'}

def link(target, depth):
    """target is a site path without .html such as 'contact' or 'blog/slug'."""
    if PROD: return '/' + ('' if target == 'index' else target)
    return '../' * depth + target + '.html'

def asset(path, depth):
    return ('/' if PROD else '../' * depth) + path

def map_href(h, depth):
    h = (h or '').strip()
    if h.startswith('file:'): return None
    m = re.match(r'https?://(?:www\.)?thesocialdm\.com(/[^?#]*)?(.*)$', h)
    if m: path, rest = (m.group(1) or '/').rstrip('/') or '/', m.group(2)
    elif h.startswith('/'):
        m2 = re.match(r'([^?#]*)(.*)$', h); path, rest = m2.group(1).rstrip('/') or '/', m2.group(2)
    else: return h
    if path.startswith('/blog/') and path[6:] in POST_SLUGS: return link('blog/' + path[6:], depth) + rest
    if path in PAGE_MAP: return link(PAGE_MAP[path], depth) + rest
    report['unmapped_links'].add(h)
    return SITE + path + rest

KEEP = {'p','h2','h3','h4','ul','ol','li','blockquote','strong','em','a','br','table','thead','tbody','tr','td','th','figure','img','figcaption','hr','b','i'}
def clean(fragment, depth, skip_image=None, strip_title=None):
    s = BeautifulSoup(fragment, 'html.parser')
    for t in s(['style','script','noscript','button','svg','form']): t.decompose()
    seen = set()
    for im in list(s('img')):
        u = (im.get('data-src') or im.get('src') or '').split('?')[0]
        alt = im.get('alt') or ''
        fig = im.find_parent('figure')
        target = fig or im
        if not u or u in seen:
            target.decompose() if target.parent else None; continue
        seen.add(u)
        got = local_image(u)
        if not got:
            target.decompose(); continue
        path, w, h = got
        new = s.new_tag('figure')
        ni = s.new_tag('img', src=asset(path, depth), alt=undash(alt.strip()), width=str(w), height=str(h), loading='lazy')
        new.append(ni)
        cap = fig.find('figcaption') if fig else None
        if cap and cap.get_text(strip=True):
            nc = s.new_tag('figcaption'); nc.string = undash(cap.get_text(' ', strip=True)); new.append(nc)
        target.replace_with(new)
    for h1 in s('h1'): h1.name = 'h2'
    for t in s.find_all(True):
        if t.name not in KEEP:
            t.unwrap(); continue
        if t.name == 'img': continue
        if t.name == 'a':
            nh = map_href(t.get('href'), depth)
            if nh is None or not t.get('href'):
                t.unwrap(); continue
            ext = nh.startswith('http') and SITE not in nh
            t.attrs = {'href': nh}
            if ext: t.attrs.update({'target': '_blank', 'rel': 'noopener'})
        else:
            t.attrs = {}
    for t in s.find_all(['p','h2','h3','h4','li','blockquote']):
        if not t.get_text(strip=True) and not t.find('img'): t.decompose()
    for n in list(s.find_all(string=True)):
        if isinstance(n, NavigableString):
            nu = undash(str(n))
            if nu != str(n): n.replace_with(nu)
    if strip_title:
        first = s.find(['h2','h3'])
        if first and re.sub(r'\W+','',first.get_text()).lower() == re.sub(r'\W+','',undash(strip_title)).lower(): first.decompose()
    out = str(s)
    out = re.sub(r'\n\s*\n+', '\n', out)
    return out.strip()

def plain(h):
    s = BeautifulSoup(h, 'html.parser')
    for t in s(['style','script','noscript','button']): t.decompose()
    return re.sub(r'\W+', ' ', undash(s.get_text(' '))).lower().split()

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&family=Inter+Tight:wght@300;500;700;800&display=swap">'
def shell(title, desc, canon, depth, body, extra_head='', og_image=None, og_type='website'):
    e = html.escape
    robots = '' if PROD else '<meta name="robots" content="noindex">'
    draft = '' if PROD else '<div class="draft">Draft</div>'
    og = f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{SITE}{canon}"><meta property="og:site_name" content="The SocialDM"><meta property="og:type" content="{og_type}"><meta name="twitter:card" content="summary_large_image">'
    if og_image: og += f'<meta property="og:image" content="{SITE}/{og_image}">'
    return f'''<!doctype html><html lang="en" data-base="{'/' if PROD else '../'*depth}" data-prod="{1 if PROD else 0}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><link rel="canonical" href="{SITE}{canon}">{robots}{og}
<meta name="claude:viewport-fit-sides" content="cover">{FONTS}
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#140F3A"><link rel="stylesheet" href="{asset('site.css',depth)}"><link rel="stylesheet" href="{asset('blog.css',depth)}">{extra_head}
</head><body>{draft}<div id="site-header"></div>
{body}
<div id="site-footer"></div><script src="{asset('chrome.js',depth)}"></script></body></html>
'''

def fmt(ms_or_date):
    if isinstance(ms_or_date, (int, float)):
        dt = datetime.datetime.fromtimestamp(ms_or_date / 1000, datetime.timezone(datetime.timedelta(hours=-7)))
    else:
        dt = datetime.datetime.strptime(ms_or_date, '%Y-%m-%d')
    return dt.strftime('%Y-%m-%d'), dt.strftime('%b ') + str(dt.day) + dt.strftime(', %Y'), dt.year

CTA = lambda depth: f'''<section class="wrap"><div class="cta"><div class="eyebrow">Get your visibility plan</div><h2 style="margin-top:16px">See where your community shows up, and where it doesn&rsquo;t.</h2><p>We check Google Search, Google Maps and AI answers for your community and send a clear plan to close the gaps.</p><a class="btn btn-light" href="{link('contact',depth)}">Get your visibility plan</a></div></section>'''

CTA_HUB = lambda depth: f'''<section class="wrap"><div class="cta"><div class="eyebrow">Get your visibility plan</div><h2 style="margin-top:16px">See where you show up, and where you don&rsquo;t.</h2><p>We check Google Search, Google Maps and AI answers for your business and send a clear plan to close the gaps.</p><a class="btn btn-light" href="{link('contact',depth)}">Get your visibility plan</a></div></section>'''

# ---------- collect posts ----------
posts = []
for p in d['posts']:
    slug = p['fullUrl'].split('/blog/')[1]
    sd = p.get('seoData') or {}
    body = clean(p['body'], 1, strip_title=p['title'])
    a, b = plain(p['body']), plain(body)
    if abs(len(a) - len(b)) > max(14, len(p['title'].split()) + 8):
        report['text_diffs'].append((slug, len(a), len(b)))
    ex = BeautifulSoup(p.get('excerpt') or '', 'html.parser').get_text(' ', strip=True)
    if not ex:
        fp = BeautifulSoup(body, 'html.parser').find('p')
        ex = fp.get_text(' ', strip=True) if fp else ''
    iso, nice, yr = fmt(p['publishOn'])
    hero = local_image(p['assetUrl']) if p.get('assetUrl') else None
    posts.append(dict(slug=slug, title=undash(html.unescape(p['title']).replace('\xa0',' ')), seoTitle=undash(sd.get('seoTitle') or ''), seoDesc=undash(sd.get('seoDescription') or ''),
        excerpt=undash(ex), body=body, iso=iso, nice=nice, year=yr, hero=hero, author=p.get('author') or 'The SocialDM', updated=fmt(p['updatedOn'])[0], new=False, faq=[], alt=undash(p['title'])))
TODAY = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=7)).strftime('%Y-%m-%d')   # Phoenix date, no DST
VERTICALS = {'ai-search': ('AI Search', 'AI Search Insights', 'How local businesses get named in ChatGPT, Gemini and Google AI answers.'),
             'multifamily': ('Multifamily', 'Multifamily Marketing Insights', 'How apartment communities get found on Google Search, Google Maps, social and AI answers.'),
             'real-estate': ('Real Estate', 'Real Estate Marketing Insights', 'How agents and teams build visibility and trust on Google, social and AI answers.'),
             'medical': ('Medical', 'Medical Practice Marketing Insights', 'How practices become the trusted local choice on Google, Maps and AI answers.'),
             'med-spa': ('Med Spa', 'Med Spa Marketing Insights', 'How med spas and aesthetic practices get found, trusted and booked on Google, social and AI answers.'),
             'salon': ('Hair Salons', 'Salon Marketing Insights', 'How salons and stylists fill their chairs through Google, social and AI answers.'),
             'hospitality': ('Hospitality', 'Hospitality Marketing Insights', 'How hotels, restaurants and venues get found and booked through search, Maps and AI.'),
             'enterprise': ('Enterprise', 'Multi Location Marketing Insights', 'How multi location brands stay consistent and visible in every market.')}
for _p in posts:
    _p['vertical'] = 'real-estate' if re.search(r'realtor|real estate', _p['title'], re.I) else 'multifamily'
for f in sorted(glob.glob(NEW + '/*.json')):
    n = json.load(open(f))
    if PROD and not n.get('approved'):   # unapproved drafts appear only in the preview
        continue
    if PROD and n['date'] > TODAY:      # scheduled: goes live on its date (Netlify rebuilds daily)
        continue
    iso, nice, yr = fmt(n['date'])
    hero = None
    if n.get('image'):
        try:
            from PIL import Image as _I
            _w,_h = _I.open(os.path.dirname(os.path.abspath(__file__)) + '/images-new/' + os.path.basename(n['image'])).size
        except Exception:
            _w,_h = 1400, 933
        hero = (n['image'], _w, _h)
    posts.append(dict(slug=n['slug'], title=n['title'], seoTitle=n['seoTitle'], seoDesc=n['seoDescription'], excerpt=n['excerpt'], body=n['bodyHtml'], iso=iso, nice=nice, year=yr, hero=hero,
        author='Michael Shad', updated=iso, new=True, faq=n.get('faq', []), alt=n.get('imageAlt', n['title']), takeaways=n.get('takeaways', []), vertical=n.get('vertical', 'multifamily')))
    POST_SLUGS.add(n['slug'])
posts.sort(key=lambda x: x['iso'], reverse=True)

def fix_internal(h, depth):
    def rep(m):
        nh = map_href(m.group(1), depth)
        return f'href="{nh}"' if nh else 'href="#"'
    return re.sub(r'href="(/[^"]*)"', rep, h)

def card(p, depth, feat=False):
    im = f'<div class="pimg"><img src="{asset(p["hero"][0],depth)}" alt="" loading="lazy"></div>' if p['hero'] else ''
    ex = html.escape(p['excerpt'][:170].rsplit(' ', 1)[0] + '...' if len(p['excerpt']) > 170 else p['excerpt'])
    return f'<a class="post{" feat" if feat else ""}" href="{link("blog/"+p["slug"],depth)}">{im}<time datetime="{p["iso"]}">{p["nice"]}</time><h3>{html.escape(p["title"])}</h3><p>{ex}</p><span class="more">Read the article</span></a>'


AUTHOR_BIO = ('Michael Shad is the founder of The SocialDM, a Phoenix based marketing agency started in 2019, '
              'and leads LocalLift&trade;, its weekly Google, Maps and AI visibility program for apartment communities.')
def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', BeautifulSoup(s, 'html.parser').get_text().lower()).strip('-')[:60]
def enrich(p, body):
    """New posts: anchor ids on H2s, key takeaways from the answer-first sentences, table of contents."""
    toc, takeaways, used = [], [], set()
    def h2rep(m):
        inner = m.group(2); sid = slugify(inner) or 'section'
        while sid in used: sid += '-2'
        used.add(sid); toc.append((sid, BeautifulSoup(inner, 'html.parser').get_text(' ', strip=True)))
        return f'<h2{m.group(1)} id="{sid}">{inner}</h2>'
    body = re.sub(r'<h2([^>]*)>(.*?)</h2>', h2rep, body, flags=re.S)
    for m in re.finditer(r'<h2[^>]*>(.*?)</h2>\s*<p>(.*?)</p>', body, flags=re.S):
        q = BeautifulSoup(m.group(1), 'html.parser').get_text(' ', strip=True)
        if not q.endswith('?'): continue
        txt = BeautifulSoup(m.group(2), 'html.parser').get_text(' ', strip=True)
        first = re.split(r'(?<=[.!?])\s+(?=[A-Z])', txt)[0]
        if 40 <= len(first) <= 260: takeaways.append(first)
        if len(takeaways) == 4: break
    toc = [t for t in toc if not t[1].lower().startswith('questions')]
    if p.get('takeaways'): takeaways = p['takeaways']
    box = ''
    if takeaways:
        box += '<aside class="takeaways" aria-label="Key takeaways"><div class="tk-label">Key takeaways</div><ul>' + ''.join(f'<li>{html.escape(t)}</li>' for t in takeaways) + '</ul></aside>'
    if len(toc) >= 3:
        box += '<nav class="toc" aria-label="In this article"><div class="tk-label">In this article</div><ol>' + ''.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in toc) + '</ol></nav>'
    return body, box
AUTHOR_BOX = ('<aside class="author-box"><div class="ab-mark" aria-hidden="true">MS</div><div><div class="tk-label">About the author</div>'
              '<b>Michael Shad</b><span class="ab-role">Founder, The SocialDM</span><p>' + AUTHOR_BIO + '</p>'
              '<a href="{about}">More about The SocialDM</a></div></aside>')

for i, p in enumerate(posts):
    related = [q for q in posts if q is not p][:0]
    STOP = {'apartment','apartments','multifamily','communities','community','about','their','there','which','where','while','still','should','would','could','2025','2026','renters','renter'}
    def kw(q): return set(w for w in re.findall(r'[a-z]{4,}', (q['title'] + ' ' + (q['seoDesc'] or '') + ' ' + q['excerpt'][:200]).lower()) if w not in STOP)
    def tw(q): return set(w.rstrip('s') for w in re.findall(r'[a-z]{4,}', q['title'].lower()) if w not in STOP)
    mine, mt = kw(p), tw(p)
    scored = sorted((q for q in posts if q is not p), key=lambda q: (3 * len(mt & tw(q)) + len(mine & kw(q)) + (1 if q['iso'] >= '2026' else 0), q['iso']), reverse=True)
    related = scored[:3]
    body = fix_internal(p['body'], 1)
    nwords = len(BeautifulSoup(body, 'html.parser').get_text(' ', strip=True).split())
    mins = max(1, round(nwords / 230))
    extras = ''
    if p['new']:
        body, extras = enrich(p, body)
    has_body_img = '<img' in body[:600]
    heroimg = ''
    if p['hero'] and not has_body_img:
        heroimg = f'<figure class="art-hero"><img src="{asset(p["hero"][0],1)}" alt="{html.escape(p["alt"])}" width="{p["hero"][1]}" height="{p["hero"][2]}"></figure>'
    ld = {'@context':'https://schema.org','@type':'BlogPosting','headline':p['title'],'datePublished':p['iso'],'dateModified':p['updated'],
          'mainEntityOfPage':f'{SITE}/blog/{p["slug"]}','wordCount':nwords,'inLanguage':'en-US',
          'author':({'@type':'Person','name':'Michael Shad','jobTitle':'Founder','url':SITE+'/about','worksFor':{'@type':'Organization','name':'The SocialDM','url':SITE}} if p['author']=='Michael Shad' else {'@type':'Organization','name':'The SocialDM','url':SITE}),
          'publisher':{'@type':'Organization','name':'The SocialDM','logo':{'@type':'ImageObject','url':SITE+'/logo.png'}},'description':p['seoDesc'] or p['excerpt'][:155]}
    if p['hero']: ld['image'] = f'{SITE}/{p["hero"][0]}'
    head = f'<script type="application/ld+json">{json.dumps(ld)}</script>'
    head += '<script type="application/ld+json">' + json.dumps({'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[
        {'@type':'ListItem','position':1,'name':'Home','item':SITE+'/'},{'@type':'ListItem','position':2,'name':'Market Intelligence','item':SITE+'/blog'},
        {'@type':'ListItem','position':3,'name':p['title'],'item':f'{SITE}/blog/{p["slug"]}'}]}) + '</script>'
    if p['faq']:
        head += '<script type="application/ld+json">' + json.dumps({'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q['q'],'acceptedAnswer':{'@type':'Answer','text':q['a']}} for q in p['faq']]}) + '</script>'
    by = 'Michael Shad, Founder of The SocialDM' if p['author']=='Michael Shad' else 'The SocialDM'
    upd = f'<span>Updated {fmt(p["updated"])[1]}</span>' if p['updated'] and p['updated'] > p['iso'] else ''
    abox = AUTHOR_BOX.replace('{about}', link('about', 1)) if p['author']=='Michael Shad' else ''
    main = f'''<main class="paper"><article class="art"><div class="art-head wrap"><a class="back" href="{link('blog',1)}">Market Intelligence</a><h1>{html.escape(p['title'])}</h1><div class="meta"><time datetime="{p['iso']}">{p['nice']}</time><span>{by}</span><span>{mins} min read</span>{upd}</div></div>
<div class="art-body wrap">{heroimg}{extras}{body}{abox}</div></article>
<section class="wrap related"><div class="eyebrow">Keep reading</div><div class="posts">{''.join(card(q,1) for q in related)}</div></section>{CTA(1)}</main>'''
    title = (p['seoTitle'] or p['title'])
    if 'The SocialDM' not in title: title += ' | The SocialDM'
    desc = (p['seoDesc'] or p['excerpt'])[:158]
    open(f'{OUT}/blog/{p["slug"]}.html','w').write(shell(title, desc, f'/blog/{p["slug"]}', 1, main, head, p['hero'][0] if p['hero'] else None, 'article'))

# ---------- blog index ----------
years = sorted({p['year'] for p in posts}, reverse=True)
grp = ''.join(f'<h2 class="yr" id="y{y}">{y}</h2><div class="posts">' + ''.join(card(p,0) for p in posts[1:] if p['year']==y) + '</div>' for y in years)
jump = ''.join(f'<a href="#y{y}">{y}</a>' for y in years)
main = f'''<main class="listing"><section class="hero pg-hero bl-hero"><div class="wrap"><div class="eyebrow">Market Intelligence</div><h1>How customers find <span>you now.</span></h1><p>Research and field notes on how apartment communities, agents, practices, spas, salons and resorts get found and chosen across Google Search, Google Maps, social and AI answers.</p><div class="jump" aria-label="Jump to year">{jump}</div></div></section>
<section class="wrap bl" aria-label="All articles"><div class="featwrap">{card(posts[0],0,True)}<div class="report"><div><div class="eyebrow">Research</div><h3>The 2026 Multifamily Visibility Report</h3><p>How apartment communities and lease ups are being discovered across social media, Google Search, Google Maps, and AI search.</p></div><a class="btn btn-line" href="{link('2026-multifamily-visibility-report',0)}">Read the report</a></div></div>{grp}</section>{CTA(0)}</main>'''
topics_present = [v for v in VERTICALS if any(p.get('vertical') == v for p in posts)]
chips = ''.join(f'<a href="{link("blog/topics/" + v, 0)}">{VERTICALS[v][0]}</a>' for v in topics_present)
main = main.replace('<div class="jump" aria-label="Jump to year">', '<div class="jump" aria-label="Topics">' + chips + '</div><div class="jump" aria-label="Jump to year">', 1)
os.makedirs(OUT + '/blog/topics', exist_ok=True)
for v in topics_present:
    name, h, sub = VERTICALS[v]
    vp = [p for p in posts if p.get('vertical') == v]
    others = ''.join(f'<a href="{link("blog/topics/" + o, 2)}">{VERTICALS[o][0]}</a>' for o in topics_present if o != v)
    allchips = f'<a href="{link("blog", 2)}">All</a>' + ''.join(f'<a href="{link("blog/topics/" + o, 2)}"' + (' class="on" aria-current="page"' if o == v else '') + f'>{VERTICALS[o][0]}</a>' for o in topics_present)
    words = h.rsplit(' ', 1)
    hub = (f'<main class="listing"><section class="hero pg-hero bl-hero"><div class="wrap"><a class="back" href="{link("blog", 2)}">All articles</a>'
           f'<div class="eyebrow" style="margin-top:18px">{name} &middot; {len(vp)} article{"s" if len(vp) != 1 else ""}</div><h1>{words[0]} <span>{words[1]}.</span></h1><p>{sub}</p>'
           f'<div class="jump topics" aria-label="Topics">{allchips}</div></div></section>'
           f'<section class="wrap bl"><div class="posts">{"".join(card(p, 2) for p in vp)}</div></section>{CTA_HUB(2)}</main>')
    open(f'{OUT}/blog/topics/{v}.html', 'w').write(shell(f'{h.title()} | The SocialDM', f'{sub} Articles from The SocialDM.', f'/blog/topics/{v}', 2, hub))
open(f'{OUT}/blog.html','w').write(shell('Market Intelligence Blog | The SocialDM','Research and field notes from The SocialDM on how renters find apartment communities across Google Search, Google Maps and AI search.','/blog',0,main))

# ---------- carried over pages ----------
def carry(path, title_fallback=None):
    raw = d['extra'][path]
    s = BeautifulSoup(raw, 'html.parser')
    title = (s.title.get_text(strip=True) if s.title else title_fallback)
    md = s.find('meta', attrs={'name':'description'}); desc = md.get('content','') if md else ''
    m = s.find('main') or s.find(id='page') or s
    depth = path.count('/') - 1
    h1 = m.find('h1'); head = h1.get_text(' ', strip=True) if h1 else title
    for x in m.select('.blog-item-top-wrapper, .blog-item-comments, .item-pagination, .blog-meta-section, .blog-item-author-profile-wrapper'): x.decompose()
    body = clean(str(m), depth, strip_title=head)
    if not desc:
        fp = BeautifulSoup(body,'html.parser').find('p'); desc = fp.get_text(' ',strip=True)[:155] if fp else title
    main = f'<main class="paper"><article class="art"><div class="art-head wrap"><h1>{html.escape(undash(head))}</h1></div><div class="art-body wrap">{fix_internal(body,depth)}</div></article>{CTA(depth)}</main>'
    open(f'{OUT}{path}.html','w').write(shell(undash(title), undash(desc), path, depth, main))
for pth in ['/apartment-seo-for-multifamily-communities','/montage-tigard','/pillar-communities','/apartment-seo-blog-hub/cuvee-apartments-westgate-glendale']:
    carry(pth)

# ---------- static draft pages ----------
for f in glob.glob(SRC + '/*.html'):
    n = os.path.basename(f)
    if n == 'blog.html': continue
    t = open(f).read()
    if t.count('<!doctype') > 1:           # artifact wrapper around index
        t = t[t.rfind('<!doctype'):]
        t = re.sub(r'</body></html>\s*</body></html>\s*$', '</body></html>\n', t)
    stem = n[:-5]
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import proof; t = proof.render(t)
    def _latest(m):
        vp = [p for p in posts if p.get('vertical') == m.group(1)][:3]
        if not vp: return ''
        return (f'<section class="block paper-strip" style="padding-top:0"><div class="wrap"><div class="eyebrow">Latest insights</div>'
                f'<h2 class="h2">Field notes for {VERTICALS[m.group(1)][0].lower()} teams.</h2><div class="posts">{"".join(card(p, 0) for p in vp)}</div>'
                f'<p style="margin-top:22px"><a class="btn btn-line" href="{link("blog/topics/" + m.group(1), 0)}">All {VERTICALS[m.group(1)][0].lower()} articles</a></p></div></section>')
    t = re.sub(r'<!--posts:([a-z-]+)-->', _latest, t)
    if 'class="posts"' in t and 'blog.css' not in t:
        t = t.replace('<link rel="stylesheet" href="site.css">', '<link rel="stylesheet" href="site.css"><link rel="stylesheet" href="blog.css">', 1)
    canon = '/' if stem == 'index' else '/' + stem
    if '<link rel="canonical"' not in t:
        t = t.replace('</head>', f'<link rel="canonical" href="{SITE}{canon}"><link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png"><link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#140F3A"></head>', 1)
    t = t.replace('<html lang="en">', f'<html lang="en" data-base="{"/" if PROD else ""}" data-prod="{1 if PROD else 0}">', 1)
    if PROD:
        t = t.replace('<div class="draft">Draft</div>', '')
        t = re.sub(r'href="(?!https?:|mailto:|#|/)([^"#]+?)\.html', lambda m: 'href="/' + ('' if m.group(1)=='index' else m.group(1)), t)
        t = re.sub(r'(src|href)="((?:p\d+\.jpg|logo\.png|locallift-white\.png|site\.css|fx\.css|fx\.js|chrome\.js))"', r'\1="/\2"', t)
    else:
        t = t.replace('</head>', '<meta name="robots" content="noindex"></head>', 1)
        t = t.replace('data-netlify="true"', 'data-netlify="true" onsubmit="return false"')  # preview never submits
    open(f'{OUT}/{n}', 'w').write(t)
for a in ['site.css','fx.css','fx.js','logo.png','locallift-white.png','favicon.ico','favicon-32.png','favicon-48.png','icon-192.png','icon-512.png','apple-touch-icon.png','site.webmanifest','og-image.png'] + [os.path.basename(x) for x in glob.glob(SRC+'/p*.jpg')]:
    shutil.copy(f'{SRC}/{a}', f'{OUT}/{a}')
shutil.copy(os.path.dirname(os.path.abspath(__file__)) + '/blog.css', OUT + '/blog.css')
if os.path.isdir(SRC + '/reels'):
    shutil.copytree(SRC + '/reels', OUT + '/reels', dirs_exist_ok=True)
if os.path.isdir(SRC + '/email'):
    shutil.copytree(SRC + '/email', OUT + '/email', dirs_exist_ok=True)
if os.path.isdir(os.path.dirname(os.path.abspath(__file__)) + '/images-new'):
    shutil.copytree(os.path.dirname(os.path.abspath(__file__)) + '/images-new', OUT + '/images/new', dirs_exist_ok=True)

# shared header and footer script: all menu links resolve through one function
c = open(SRC + '/chrome.js').read()
c = c.replace('var here=(location.pathname.split("/").pop()||"index.html");',
 '''var R=document.documentElement.dataset,PROD=R.prod==="1",BASE=R.base||"";
function L(h){if(/^(https?:|mailto:|#)/.test(h))return h;if(PROD)return "/"+h.replace(/\\.html$/,"").replace(/^index$/,"");return BASE+h}
var here=(location.pathname.split("/").pop()||"index.html");if(here.indexOf(".")<0)here+=".html";''')
c = re.sub(r'href="\'\+x\[1\]\+\'"', 'href="\'+L(x[1])+\'"', c)
for pg in ['index.html','contact.html','locallift.html','blog.html']:
    c = c.replace(f'href="{pg}"', f'href="\'+L("{pg}")+\'"')
c = c.replace('src="logo.png"', 'src="\'+(PROD?"/":BASE)+\'logo.png"')
c = c.replace('new Date().getFullYear()+\' The SocialDM. LocalLift', 'new Date().getFullYear()+\' The SocialDM. LocalLift')
# social proof popup: approved reviews from testimonials.json, appended to chrome.js so every page gets it
def _first(q, lim=100):
    m = re.match(r'(.+?[.!?])(\s|$)', q.strip())
    s = m.group(1) if m else q.strip()
    if len(s) > lim:
        s = s[:lim].rsplit(' ', 1)[0].rstrip(',;:') + '\u2026'
    return s
_tj = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/testimonials.json'))
_pop = [dict(q=_first(r['quote']), n=r['name'], r=r.get('role', ''), v=r.get('vertical', ['home']), g=1 if r.get('source') == 'google' else 0)
        for r in _tj['reviews'] if r.get('approved')]
c += '\nwindow.SDM_POP=' + json.dumps({'reviews': _pop}, ensure_ascii=False) + ';\n' + open(SRC + '/pop.js').read() + '\n' + open(SRC + '/offer.js').read()
open(OUT + '/chrome.js', 'w').write(c)
if os.path.exists(SRC + '/activity.json'):
    shutil.copy(SRC + '/activity.json', OUT + '/activity.json')

# ---------- answer pages (/answers/<slug>): approved Q and A copy in tools/answers.json ----------
ANSWERS = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/answers.json'))['pages']
os.makedirs(OUT + '/answers', exist_ok=True)
ANS_CSS = ('<style>.ans-pg .pg-hero .eyebrow{text-decoration:none}.ans-pg .pg-hero h1{max-width:20ch}'
           '.ans-short{max-width:760px;margin-top:10px;padding:26px 28px;border-radius:24px;background:linear-gradient(160deg,rgba(75,79,184,.32),rgba(30,26,77,.5));border:1px solid var(--line);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}'
           '.ans-short p{margin:12px 0 0;color:#fff;font-size:clamp(18px,1.7vw,21px);line-height:1.55;max-width:none}'
           '.ans-meta{color:var(--dim);font-size:14px}.ans-sec{padding-block:70px 0}.ans-pg .cta{margin-top:90px}'
           '.ans-causes b{font:700 15px/1 var(--body);letter-spacing:.14em;color:var(--sky)}.ans-causes span{color:#fff;font-size:17px;margin-top:14px}'
           '.cards.two span{font-size:16.5px}.ans-pg .cta .btn{white-space:normal;text-align:center;line-height:1.3}'
           '.ans-hub .cards a{transition:border-color .2s,transform .2s}.ans-hub .cards a:hover{border-color:var(--sky);transform:translateY(-2px)}'
           '.ans-hub .cards b{font-size:21px}.ans-hub .more{display:inline-block;margin-top:16px;font:600 12px/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--sky)}'
           '@media (max-width:860px){.ans-sec{padding-block:50px 0}.ans-short{padding:22px}}</style>')
def _ans_desc(t, lim=154):
    if len(t) <= lim: return t
    first = re.split(r'(?<=[.!?])\s+', t)[0]
    if len(first) <= lim: return first
    return t[:lim].rsplit(' ', 1)[0].rstrip(',;:') + '.'
for a in ANSWERS:
    e = html.escape
    url = f'{SITE}/answers/{a["slug"]}'
    title = a['q'] + ' | The SocialDM' if len(a['q']) <= 60 else a['q']
    desc = a.get('desc') or _ans_desc(a['short'])
    faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': ans}} for q, ans in a['faq']]}
    crumbs = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': 'Answers', 'item': SITE + '/answers'},
        {'@type': 'ListItem', 'position': 3, 'name': a['q'], 'item': url}]}
    head = ('<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">'
            + ''.join('<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + '</script>' for b in (faq_ld, crumbs)) + ANS_CSS)
    iso, nice, _ = fmt(a['date'])
    _w = a['q'].split(); _cut = max(1, len(_w) - 3)
    h1 = e(' '.join(_w[:_cut])) + ' <span>' + e(' '.join(_w[_cut:])) + '</span>'
    causes = ''.join(f'<div><b>{i:02d}</b><span>{e(x)}</span></div>' for i, x in enumerate(a['list'], 1))
    faq = ''.join(f'<details><summary>{e(q)}</summary><p>{e(ans)}</p></details>' for q, ans in a['faq'])
    href = a.get('cta_href') or link('contact', 1)
    main = (f'<main class="ans-pg"><section class="hero pg-hero"><div class="wrap">'
            f'<a class="eyebrow" href="{link("answers", 1)}">&larr; Answers</a><h1>{h1}</h1>'
            f'<div class="ans-short"><div class="eyebrow">Short answer</div><p>{e(a["short"])}</p></div>'
            f'<div class="ans-meta">The SocialDM &middot; <time datetime="{iso}">{nice}</time></div></div></section>'
            f'<section class="block ans-sec"><div class="wrap"><div class="eyebrow">The problem</div><h2 class="h2">{e(a["list_title"])}</h2>'
            f'<div class="cards ans-causes">{causes}</div></div></section>'
            f'<section class="block ans-sec"><div class="wrap"><div class="cards two">'
            f'<div><b>What it costs you</b><span>{e(a["cost"][:1].upper() + a["cost"][1:])}</span></div>'
            f'<div><b>{e(a["help_label"].rstrip(":"))}</b><span>{e(a["help"])}</span></div></div></div></section>'
            f'<section class="block ans-sec"><div class="wrap"><div class="eyebrow">FAQ</div><h2 class="h2">Questions we hear</h2><div class="faq">{faq}</div></div></section>'
            f'<section class="wrap"><div class="cta"><div class="eyebrow">Next step</div><h2 style="margin-top:16px">{"See what a week of posts looks like" if a.get("cta_href") else e(a["cta"])}</h2>'
            f'<a class="btn btn-light" href="{href}">{"See a sample week" if a.get("cta_href") else "Get your visibility plan"}</a></div></section></main>')
    open(f'{OUT}/answers/{a["slug"]}.html', 'w').write(shell(title, desc, f'/answers/{a["slug"]}', 1, main, head, 'og-image.png'))
_items = ''.join(f'<a href="{link("answers/" + a["slug"], 0)}"><b>{html.escape(a["q"])}</b><span>{html.escape(a["short"])}</span><span class="more">Read the answer</span></a>' for a in ANSWERS)
_crumbs0 = {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
    {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'}, {'@type': 'ListItem', 'position': 2, 'name': 'Answers', 'item': SITE + '/answers'}]}
_main0 = (f'<main class="ans-pg ans-hub"><section class="hero pg-hero"><div class="wrap"><div class="eyebrow">Answers</div><h1>Straight answers, <span>no runaround.</span></h1>'
          f'<p>Short, direct answers from The SocialDM on getting found on Google, Maps and AI search.</p></div></section>'
          f'<section class="block ans-sec" style="padding-top:0"><div class="wrap"><div class="cards two">{_items}</div></div></section>{CTA_HUB(0)}</main>')
open(f'{OUT}/answers.html', 'w').write(shell('Answers | The SocialDM', 'Short, direct answers from The SocialDM on getting apartment communities and local practices found on Google, Maps and AI search.',
     '/answers', 0, _main0, '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><script type="application/ld+json">' + json.dumps(_crumbs0) + '</script>' + ANS_CSS, 'og-image.png'))

ANS = ANSWERS

# ---------- production plumbing ----------
if PROD:
    open(OUT + '/_redirects', 'w').write('''/new-page /real-estate 301
/home / 301
/apartment-seo-blog-hub /blog 301
/services-1 /multifamily-marketing-agency 301
/multifamily /multifamily-marketing-agency 301
/research /research-insights 301
/company /about 301
/about-us /about 301
/contact-us /contact 301
/services /multifamily-marketing-agency 301
/real-estate-1 /real-estate 301
/medical-1 /medical 301
/hospitality-1 /hospitality 301
/enterprise-1 /enterprise 301
/cuvee /apartment-seo-blog-hub/cuvee-apartments-westgate-glendale 301
/cuvee-blog/* /blog 301
/cuvee-blog /blog 301
/blog/tag/* /blog 301
/blog/category/* /blog 301
''')
    urls = ['/'] + ['/' + os.path.basename(f)[:-5] for f in glob.glob(OUT + '/*.html') if os.path.basename(f) not in ('index.html','404.html','thank-you.html')]
    urls += ['/blog/topics/' + os.path.basename(x)[:-5] for x in glob.glob(OUT + '/blog/topics/*.html')]
    urls += [f'/answers/{a["slug"]}' for a in ANS]
    urls += ['/apartment-seo-blog-hub/cuvee-apartments-westgate-glendale'] + [f'/blog/{p["slug"]}' for p in posts]
    open(OUT + '/sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}{u}</loc></url>\n' for u in sorted(set(urls))) + '</urlset>\n')
    open(OUT + '/robots.txt', 'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    items = ''.join(f'<item><title>{html.escape(p["title"])}</title><link>{SITE}/blog/{p["slug"]}</link><guid>{SITE}/blog/{p["slug"]}</guid><pubDate>{datetime.datetime.strptime(p["iso"],"%Y-%m-%d").strftime("%a, %d %b %Y 12:00:00 -0700")}</pubDate><description>{html.escape(p["excerpt"][:300])}</description></item>' for p in posts[:50])
    open(OUT + '/blog/rss.xml', 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>The SocialDM Market Intelligence</title><link>{SITE}/blog</link><description>How renters find apartments now.</description>{items}</channel></rss>\n')
main404 = f'<main><section class="hero pg-hero"><div class="wrap"><div class="eyebrow">Page not found</div><h1>This page <span>moved.</span></h1><div class="ctas"><a class="btn btn-light" href="{link("blog",0)}">Read the latest</a><a class="btn btn-line" href="{link("index",0)}">Back home</a></div></div></section></main>'
open(OUT + '/404.html', 'w').write(shell('Page not found | The SocialDM', 'This page moved.', '/404', 0, main404))

if PROD:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import seo_layer; seo_layer.run(OUT)

print(json.dumps({'posts': len(posts), 'new': sum(p['new'] for p in posts), 'images_used': len(report['used_images']), 'images_missing': sorted(report['missing_images']), 'unmapped_links': sorted(report['unmapped_links']), 'text_diffs': report['text_diffs']}, indent=1))

# guard: every old URL Google knows (tools/known-urls.txt) must have a page or a redirect, or the deploy fails and the live site stays as it was
if PROD:
    import check_urls
    _miss = check_urls.check(OUT, os.path.dirname(os.path.abspath(__file__)) + '/known-urls.txt')
    if _miss:
        sys.exit('BUILD STOPPED: these old URLs would land on the 404 page. Add a redirect in build.py:\n' + '\n'.join(_miss))
