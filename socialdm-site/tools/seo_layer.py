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
       'logo': SITE + '/icon-512.png', 'foundingDate': '2019', 'telephone': '+1-602-753-6807',
       'address': {'@type': 'PostalAddress', 'streetAddress': '3104 E Camelback Rd #2161', 'addressLocality': 'Phoenix',
                   'addressRegion': 'AZ', 'postalCode': '85016', 'addressCountry': 'US'},
       'areaServed': {'@type': 'Country', 'name': 'United States'},
       'description': 'The SocialDM is a multifamily marketing agency, headquartered in Phoenix, that helps apartment communities nationwide get found on Google Search, Google Maps, social media and AI answers.',
       'knowsAbout': ['Multifamily marketing', 'Apartment SEO', 'Google Business Profile', 'Google Maps visibility', 'AI search visibility', 'Social media marketing'],
       'sameAs': SOCIAL}

# path stem -> (title, description, schema kind, service name)
META = {
 'index': ('Multifamily Marketing for Search, Maps and AI | The SocialDM',
           'The SocialDM is a multifamily marketing agency helping apartment communities nationwide get found on Google Search, Google Maps, social and AI answers.', 'home', None),
 'about': ('About The SocialDM | National Multifamily Marketing Agency',
           'Founded in 2019, The SocialDM helps apartment communities nationwide get found on Google, Maps and AI answers before renters choose.', 'about', None),
 'contact': ('Contact The SocialDM | Get Your Visibility Plan',
             'Tell us about your community, practice or business. A real person reads every message and replies within one business day.', 'contact', None),
 'locallift': ('LocalLift: Google, Maps and AI Visibility for Apartments',
               'LocalLift by The SocialDM checks how apartment communities show up on Google Search, Google Maps and AI answers every week, and reports what changed.', 'service', 'LocalLift apartment visibility program'),
 'multifamily-marketing-agency': ('Multifamily Marketing Agency | Apartment SEO | The SocialDM',
               'A multifamily marketing agency focused on apartment SEO, Google Maps, reviews, social and AI visibility, so renters find your community before they compare.', 'service', 'Multifamily marketing and apartment SEO'),
 'apartment-google-business-profile-management': ('Google Business Profile Management for Apartments | The SocialDM',
               'Google Business Profile management for apartment communities nationwide: an active profile, every review answered and a listing that stays accurate.', 'service', 'Google Business Profile management for apartment communities'),
 'phoenix-multifamily-marketing-agency': ('Phoenix Multifamily Marketing Agency | The SocialDM',
               'Apartment marketing for the Valley from a national agency headquartered in Phoenix and Scottsdale. Google, reviews, social and AI, reported weekly.', 'service', 'Phoenix multifamily marketing'),
 'medical': ('Medical Practice Marketing and SEO | The SocialDM',
             'AI ready SEO, Google Business Profile care, careful review management and clear service pages that help medical practices become the trusted local choice.', 'service', 'Medical practice marketing and SEO'),
 'real-estate': ('Real Estate Marketing for Agents and Teams | The SocialDM',
                 'Social, Google and AI visibility for real estate agents, teams and brokerages. Individual agents start with LocalLift Signature at $199 a month, no contract.', 'service', 'Real estate agent marketing'),
 'med-spa': ('Med Spa Marketing and Local SEO | The SocialDM',
              'Social, Google and AI visibility for med spas and aesthetic practices, so new clients find you, trust you and book. Client privacy first.', 'service', 'Med spa marketing and local SEO'),
 'hair-salon': ('Hair Salon Marketing for Salons and Stylists | The SocialDM',
              'Social, Google and AI visibility for hair salons, suite owners and independent stylists, so new guests find your work and book.', 'service', 'Hair salon marketing and local SEO'),
 'hospitality': ('Hotel and Resort Marketing | AI and Local Visibility | The SocialDM',
                 'Help travelers find and book your resort, hotel or venue first. AI trip planner visibility, Google Hotels and Maps, reviews and comp set reporting.', 'service', 'Hotel and resort marketing and AI visibility'),
 'enterprise': ('Portfolio and Multi Location Marketing | The SocialDM',
                'Social, Google, Maps and AI visibility for apartment operators, management companies and multi location brands, with one weekly view of every location.', 'service', 'Portfolio and multi location marketing'),
 'research-insights': ('Multifamily Research and Insights | The SocialDM',
                       'Research from The SocialDM on how renters find apartment communities across social media, Google Search, Google Maps and AI answers.', 'page', None),
 '2026-multifamily-visibility-report': ('The 2026 Multifamily Visibility Report | The SocialDM',
                       'How apartment communities and lease ups are discovered across social media, Google Search, Google Maps and AI search in 2026, from The SocialDM.', 'article', None),
 'results': ('Results and Case Studies | Apartment Lease Ups | The SocialDM',
             'Real apartment lease up results from The SocialDM: Montage in Tigard, Oregon and Huxley Scottsdale, with leasing, Google Maps and AI visibility numbers.', 'results', None),
 'montage-case-study': ('Montage Lease Up Case Study | Tigard, OR | The SocialDM',
             'How The SocialDM marketed Montage, a new 183 home community in Tigard, Oregon, from the planning stage: 82.5% leased seven months after opening.', 'casestudy', 'montage'),
 'huxley-case-study': ('Huxley Scottsdale Lease Up Case Study | The SocialDM',
             'How The SocialDM took over marketing for Huxley Scottsdale mid lease up after its sale to Pillar Communities: 52% leased at takeover, 88% by Nov 2026.', 'casestudy', 'huxley'),
}

# service pages with a local area instead of the default United States
AREA = {'phoenix-multifamily-marketing-agency': [{'@type': 'City', 'name': c} for c in ('Phoenix', 'Scottsdale', 'Chandler', 'Tempe', 'Glendale')] + [{'@type': 'State', 'name': 'Arizona'}]}

LINKS = [('/', 'Home'), ('/multifamily-marketing-agency', 'Multifamily marketing'), ('/apartment-google-business-profile-management', 'Google Business Profile management'), ('/phoenix-multifamily-marketing-agency', 'Phoenix multifamily marketing agency'), ('https://www.localliftnow.com/', 'LocalLift'),
         ('/medical', 'Medical'), ('/real-estate', 'Real Estate'), ('/med-spa', 'Med Spa'), ('/hair-salon', 'Hair Salons'), ('/hospitality', 'Hospitality'), ('/enterprise', 'Portfolios'),
         ('/blog', 'Market Intelligence blog'), ('/research-insights', 'Research and Insights'),
         ('/2026-multifamily-visibility-report', '2026 Multifamily Visibility Report'), ('/answers', 'Answers'), ('/results', 'Results'), ('/montage-case-study', 'Montage case study'), ('/huxley-case-study', 'Huxley Scottsdale case study'), ('/about', 'About'), ('/contact', 'Contact')]


# case study pages: Article (case study) about the community, plus the client reviews on the page
CASES = {
 'montage': {'headline': 'Montage: found before the doors opened', 'date': '2026-11-13', 'image': '/case-studies/montage/og.jpg',
             'about': {'@type': 'ApartmentComplex', 'name': 'Montage', 'numberOfAccommodationUnits': 183,
                       'address': {'@type': 'PostalAddress', 'addressLocality': 'Tigard', 'addressRegion': 'OR', 'addressCountry': 'US'}},
             'client': 'FORE Property Company'},
 'huxley': {'headline': 'Huxley Scottsdale: new owner, half leased, our move', 'date': '2026-11-13', 'image': '/case-studies/huxley/og.jpg',
            'about': {'@type': 'ApartmentComplex', 'name': 'Huxley Scottsdale', 'numberOfAccommodationUnits': 192,
                      'address': {'@type': 'PostalAddress', 'addressLocality': 'Scottsdale', 'addressRegion': 'AZ', 'addressCountry': 'US'}},
            'client': 'Pillar Communities'},
}

def case_blocks(key, canon, desc, soup):
    c = CASES[key]
    img = SITE + c['image']
    reviews = []
    for fig in soup.select('.kc figure.kc-tq, .kc blockquote'):
        bq = fig if fig.name == 'blockquote' else fig.find('blockquote')
        cap = fig.find('figcaption') if fig.name == 'figure' else fig.find_next_sibling('p')
        if not bq or not cap: continue
        if fig.name == 'figure' and fig.get('aria-hidden'): continue
        if fig.name == 'blockquote' and fig.find_parent('figure'): continue
        who = cap.get_text(' ', strip=True)
        name, _, role = who.partition(', ')
        body = bq.get_text(' ', strip=True).strip('\u201c\u201d"')
        reviews.append({'@type': 'Review', 'reviewBody': body,
                        'author': {'@type': 'Person', 'name': name, 'jobTitle': role.rsplit(', ', 1)[0] if ', ' in role else role,
                                   'worksFor': {'@type': 'Organization', 'name': role.rsplit(', ', 1)[-1]}},
                        'itemReviewed': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM'}})
    art = {'@context': 'https://schema.org', '@type': 'Article', 'articleSection': 'Case study', 'genre': 'Case study',
           'headline': c['headline'], 'description': desc, 'url': canon, 'mainEntityOfPage': canon, 'image': img,
           'datePublished': c['date'], 'dateModified': c['date'], 'about': c['about'],
           'mentions': {'@type': 'Organization', 'name': c['client']},
           'author': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM'},
           'publisher': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'logo': {'@type': 'ImageObject', 'url': SITE + '/icon-512.png'}}}
    blocks = [art]
    if reviews:
        blocks.append({'@context': 'https://schema.org', '@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'url': SITE + '/', 'review': reviews})
    return blocks, img

def ld(obj): return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def run(out):
    static_nav = ('<nav class="crawl-nav" aria-label="Site links">' +
                  ''.join(f'<a href="{h}"' + (' target="_blank" rel="noopener"' if 'localliftnow.com' in h else '') + f'>{html.escape(t)}</a>' for h, t in LINKS) + '</nav>')
    static_foot = ('<div class="crawl-nav"><p>The SocialDM, 3104 E Camelback Rd #2161, Phoenix AZ 85016. (602) 753-6807.</p>' +
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
            soup0 = BeautifulSoup(t, 'html.parser')
            cs_blocks, og_img = (case_blocks(svc, canon, desc, soup0) if kind == 'casestudy' else ([], SITE + '/og-image.png'))
            if kind == 'results':
                og_img = SITE + '/case-studies/montage/og.jpg'
            if 'property="og:title"' not in t:
                head += (f'<meta property="og:type" content="{"article" if kind in ("article", "casestudy") else "website"}"><meta property="og:site_name" content="The SocialDM">'
                         f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">'
                         f'<meta property="og:url" content="{canon}"><meta property="og:image" content="{og_img}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">')
            blocks = []
            if kind in ('home', 'about', 'contact'):
                blocks.append(ORG)
            if kind == 'home':
                blocks.append({'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/', 'name': 'The SocialDM', 'publisher': {'@id': ORG_ID}})
            if kind == 'service':
                blocks.append({'@context': 'https://schema.org', '@type': 'Service', 'name': svc, 'serviceType': svc, 'url': canon,
                               'description': desc, 'provider': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'url': SITE + '/'},
                               'areaServed': AREA.get(rel, {'@type': 'Country', 'name': 'United States'})})
            if kind == 'article':
                blocks.append({'@context': 'https://schema.org', '@type': 'Article', 'headline': 'The 2026 Multifamily Visibility Report', 'url': canon,
                               'description': desc, 'author': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM'},
                               'publisher': {'@type': 'Organization', '@id': ORG_ID, 'name': 'The SocialDM', 'logo': {'@type': 'ImageObject', 'url': SITE + '/icon-512.png'}}})
            blocks += cs_blocks
            if kind == 'results':
                blocks.append({'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': 'Results and case studies', 'url': canon, 'description': desc,
                               'publisher': {'@id': ORG_ID}, 'mainEntity': {'@type': 'ItemList', 'itemListElement': [
                                   {'@type': 'ListItem', 'position': 1, 'url': SITE + '/montage-case-study', 'name': 'Montage lease up case study'},
                                   {'@type': 'ListItem', 'position': 2, 'url': SITE + '/huxley-case-study', 'name': 'Huxley Scottsdale lease up case study'}]}})
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
             '> The SocialDM is a multifamily marketing agency founded in 2019 and headquartered in Phoenix. It markets more than 7,900 apartment homes across the country and helps apartment communities get found on Google Search, Google Maps, social media and AI answers. LocalLift is its weekly visibility program for apartment communities.', '',
             'Contact: thesocialdm.com/contact, (602) 753-6807, 3104 E Camelback Rd #2161, Phoenix AZ 85016.', '', '## Services']
    for stem in ['multifamily-marketing-agency', 'apartment-google-business-profile-management', 'phoenix-multifamily-marketing-agency', 'locallift', 'medical', 'real-estate', 'med-spa', 'hair-salon', 'hospitality', 'enterprise']:
        title, desc = META[stem][0], META[stem][1]
        lines.append(f'- [{title.split(" | ")[0]}]({SITE}/{stem}): {desc}')
    lines += ['', '## Results and case studies', f'- [Results]({SITE}/results): {META["results"][1]}']
    for stem in ['montage-case-study', 'huxley-case-study']:
        lines.append(f'- [{META[stem][0].split(" | ")[0]}]({SITE}/{stem}): {META[stem][1]}')
    lines += ['', '## Research', f'- [The 2026 Multifamily Visibility Report]({SITE}/2026-multifamily-visibility-report): {META["2026-multifamily-visibility-report"][1]}',
              f'- [Market Intelligence blog]({SITE}/blog): Research and field notes on how renters find apartments.', '', '## Articles']
    answers = []
    for f in sorted(glob.glob(out + '/answers/*.html')):
        s2 = BeautifulSoup(open(f).read(), 'html.parser'); h1 = s2.find('h1'); d2 = s2.find('meta', attrs={'name': 'description'})
        if h1: answers.append(f'- [{h1.get_text(" ", strip=True)}]({SITE}/answers/{os.path.basename(f)[:-5]})' + (f': {d2.get("content", "")}' if d2 else ''))
    if answers:
        lines = lines[:-2] + ['', '## Answers'] + answers + lines[-2:]
    for slug, title, desc in posts:
        lines.append(f'- [{title}]({SITE}/blog/{slug})' + (f': {desc}' if desc else ''))
    lines += ['', '## Company', f'- [About]({SITE}/about)', f'- [Contact]({SITE}/contact)', '']
    open(out + '/llms.txt', 'w').write('\n'.join(lines))
