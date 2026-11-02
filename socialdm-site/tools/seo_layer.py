"""Production SEO layer, run by build.py after the site is written:
titles and descriptions for static pages, Open Graph tags, Organization / WebSite / Service / FAQ / Article schema,
a crawler-readable copy of the menu and footer links (Bing and AI crawlers do not run chrome.js), and llms.txt."""
import glob, html, json, os, re
from bs4 import BeautifulSoup

SITE = 'https://www.thesocialdm.com'
GA4_ID = 'G-WJ6LRXJV21'  # same GA4 tag the Squarespace site used (property: TheSocial DM)
INDEXNOW_KEY = '7c2f9e41b85a4d6e9f03a1d2c4b6e8f0'
ORG_ID = SITE + '/#organization'
SOCIAL = ['https://www.instagram.com/the.socialdm/', 'https://www.facebook.com/thesocialdm',
          'https://www.tiktok.com/@thesocialdm', 'https://www.youtube.com/@thesocialdm']
ORG = {'@context': 'https://schema.org', '@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'url': SITE + '/',
       'logo': SITE + '/logo.png', 'email': 'info@thesocialdm.com', 'foundingDate': '2019',
       'founder': {'@type': 'Person', 'name': 'Michael Shad', 'jobTitle': 'Founder'},
       'address': {'@type': 'PostalAddress', 'streetAddress': '3104 E Camelback Rd #2161', 'addressLocality': 'Phoenix',
                   'addressRegion': 'AZ', 'postalCode': '85016', 'addressCountry': 'US'},
       'areaServed': {'@type': 'Country', 'name': 'United States'},
       'description': 'The SocialDM is a Phoenix based multifamily marketing agency that helps apartment communities get found on Google Search, Google Maps, social media and AI answers.',
       'knowsAbout': ['Multifamily marketing', 'Apartment SEO', 'Google Business Profile', 'Google Maps visibility', 'AI search visibility', 'Social media marketing'],
       'sameAs': SOCIAL}

# path stem -> (title, description, schema kind, service name)
META = {
 'index': ('Multifamily Marketing for Search, Maps and AI | The SocialDM',
           'The SocialDM is a Phoenix based multifamily marketing agency helping apartment communities get found on Google Search, Google Maps, social and AI answers.', 'home', None),
 'about': ('About The SocialDM | Multifamily Marketing Agency in Phoenix',
           'Founded in 2019 by Michael Shad, The SocialDM helps apartment communities nationwide get found on Google, Maps and AI answers before renters choose.', 'about', None),
 'contact': ('Contact The SocialDM | Get Your Visibility Plan',
             'Tell us about your community, practice or business. A real person reads every message and replies within one business day from info@thesocialdm.com.', 'contact', None),
 'locallift': ('LocalLift: Google, Maps and AI Visibility for Apartments',
               'LocalLift by The SocialDM checks how apartment communities show up on Google Search, Google Maps and AI answers every week, and reports what changed.', 'service', 'LocalLift apartment visibility program'),
 'multifamily-marketing-agency': ('Multifamily Marketing Agency | Apartment SEO | The SocialDM',
               'A multifamily marketing agency focused on apartment SEO, Google Maps, reviews, social and AI visibility, so renters find your community before they compare.', 'service', 'Multifamily marketing and apartment SEO'),
 'medical': ('Medical Practice Marketing and SEO | The SocialDM',
             'AI ready SEO, Google Business Profile care, careful review management and clear service pages that help medical practices become the trusted local choice.', 'service', 'Medical practice marketing and SEO'),
 'real-estate': ('Real Estate Agent Marketing and SEO | The SocialDM',
                 'Social, search and Google Business Profile work that makes real estate agents and teams the name people already trust before the first conversation.', 'service', 'Real estate agent marketing'),
 'hospitality': ('Hospitality Marketing and Local SEO | The SocialDM',
                 'Story led social, Google Maps and search visibility that helps hotels, restaurants, venues and retail brands get found and booked.', 'service', 'Hospitality marketing and local SEO'),
 'enterprise': ('Multi Location Marketing and SEO | The SocialDM',
                'One standard for Google Business Profiles, location pages and AI visibility across every market, with reporting market by market.', 'service', 'Multi location marketing and SEO'),
 'research-insights': ('Multifamily Research and Insights | The SocialDM',
                       'Research from The SocialDM on how renters find apartment communities across social media, Google Search, Google Maps and AI answers.', 'page', None),
 '2026-multifamily-visibility-report': ('The 2026 Multifamily Visibility Report | The SocialDM',
                       'How apartment communities and lease ups are discovered across social media, Google Search, Google Maps and AI search in 2026, from The SocialDM.', 'article', None),
}

LINKS = [('/', 'Home'), ('/multifamily-marketing-agency', 'Multifamily marketing'), ('/locallift', 'LocalLift'),
         ('/medical', 'Medical'), ('/real-estate', 'Real Estate'), ('/hospitality', 'Hospitality'), ('/enterprise', 'Enterprise'),
         ('/blog', 'Market Intelligence blog'), ('/research-insights', 'Research and Insights'),
         ('/2026-multifamily-visibility-report', '2026 Multifamily Visibility Report'), ('/about', 'About'), ('/contact', 'Contact')]

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def run(out):
    static_nav = ('<nav class="crawl-nav" aria-label="Site links">' +
                  ''.join(f'<a href="{h}">{html.escape(t)}</a>' for h, t in LINKS) + '</nav>')
    static_foot = ('<div class="crawl-nav"><p>The SocialDM, 3104 E Camelback Rd #2161, Phoenix AZ 85016. info@thesocialdm.com</p>' +
                   ''.join(f'<a href="{u}">{u.split("/")[2]}</a>' for u in SOCIAL) + '</div>')
    for f in glob.glob(out + '/**/*.html', recursive=True):
        rel = os.path.relpath(f, out)[:-5]
        t = open(f).read()
        if GA4_ID not in t:
            ga = (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>'
                  f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA4_ID}');"
                  + ("gtag('event','generate_lead',{form_name:'contact'});" if rel == 'thank-you' else '') + '</script>')
            t = t.replace('<head>', '<head>' + ga, 1) if '<head>' in t else t.replace('</head>', ga + '</head>', 1)
        t = t.replace('<div id="site-header"></div>', f'<div id="site-header">{static_nav}</div>', 1)
        t = t.replace('<div id="site-footer"></div>', f'<div id="site-footer">{static_foot}</div>', 1)
        if rel in META:
            title, desc, kind, svc = META[rel]
            canon = SITE + ('/' if rel == 'index' else '/' + rel)
            t = re.sub(r'<title>.*?</title>', f'<title>{html.escape(title)}</title>', t, count=1, flags=re.S)
            t = re.sub(r'<meta name="description"[^>]*>\s*', '', t)
            head = f'<meta name="description" content="{html.escape(desc)}">'
            if 'property="og:title"' not in t:
                head += (f'<meta property="og:type" content="{"article" if kind == "article" else "website"}"><meta property="og:site_name" content="The SocialDM">'
                         f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">'
                         f'<meta property="og:url" content="{canon}"><meta property="og:image" content="{SITE}/logo.png"><meta name="twitter:card" content="summary">')
            blocks = []
            if kind in ('home', 'about', 'contact'):
                blocks.append(ORG)
            if kind == 'home':
                blocks.append({'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'The SocialDM', 'publisher': {'@id': ORG_ID}})
            if kind == 'service':
                blocks.append({'@context': 'https://schema.org', '@type': 'Service', 'name': svc, 'serviceType': svc, 'url': canon,
                               'description': desc, 'provider': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'url': SITE + '/'},
                               'areaServed': {'@type': 'Country', 'name': 'United States'}})
            if kind == 'article':
                blocks.append({'@context': 'https://schema.org', '@type': 'Article', 'headline': 'The 2026 Multifamily Visibility Report', 'url': canon,
                               'description': desc, 'author': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM'},
                               'publisher': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'logo': {'@type': 'ImageObject', 'url': SITE + '/logo.png'}}})
            soup = BeautifulSoup(t, 'html.parser')
            qa = [(d.find('summary').get_text(' ', strip=True), d.find('p').get_text(' ', strip=True))
                  for d in soup.select('.faq details') if d.find('summary') and d.find('p')]
            if qa:
                blocks.append({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
                    {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in qa]})
            head += ''.join(ld(b) for b in blocks)
            t = t.replace('</head>', head + '</head>', 1)
        open(f, 'w').write(t)
    write_llms(out)
    # IndexNow key (Bing, Yandex, Seznam): lets us notify Bing instantly when pages change, after launch
    open(out + '/' + INDEXNOW_KEY + '.txt', 'w').write(INDEXNOW_KEY)

def write_llms(out):
    posts = []
    for f in sorted(glob.glob(out + '/blog/*.html')):
        s = BeautifulSoup(open(f).read(), 'html.parser')
        h1 = s.find('h1'); d = s.find('meta', attrs={'name': 'description'})
        if h1: posts.append((os.path.basename(f)[:-5], h1.get_text(' ', strip=True), d.get('content', '') if d else ''))
    posts.sort(key=lambda p: p[0])
    lines = ['# The SocialDM', '',
             '> The SocialDM is a Phoenix based multifamily marketing agency, founded in 2019 by Michael Shad. It helps apartment communities nationwide, more than 7,900 apartment homes, get found on Google Search, Google Maps, social media and AI answers. LocalLift is its weekly visibility program for apartment communities.', '',
             'Contact: info@thesocialdm.com, 3104 E Camelback Rd #2161, Phoenix AZ 85016.', '', '## Services']
    for stem in ['multifamily-marketing-agency', 'locallift', 'medical', 'real-estate', 'hospitality', 'enterprise']:
        title, desc = META[stem][0], META[stem][1]
        lines.append(f'- [{title.split(" | ")[0]}]({SITE}/{stem}): {desc}')
    lines += ['', '## Research', f'- [The 2026 Multifamily Visibility Report]({SITE}/2026-multifamily-visibility-report): {META["2026-multifamily-visibility-report"][1]}',
              f'- [Market Intelligence blog]({SITE}/blog): Research and field notes on how renters find apartments.', '', '## Articles']
    for slug, title, desc in posts:
        lines.append(f'- [{title}]({SITE}/blog/{slug})' + (f': {desc}' if desc else ''))
    lines += ['', '## Company', f'- [About]({SITE}/about)', f'- [Contact]({SITE}/contact)', '']
    open(out + '/llms.txt', 'w').write('\n'.join(lines))
