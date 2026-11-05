// Page titles, descriptions and structured data for every page.
// SITE_URL is empty until a launch domain is chosen; schema links stay relative until then.
export const SITE = {name: 'LocalLift', url: (process.env.SITE_URL || '').replace(/\/$/, ''), parentUrl: 'https://www.thesocialdm.com/'};
const u = p => SITE.url + '/' + (p ? p + '/' : '');

const org = {
  '@type': 'Organization', '@id': u('') + '#org', name: 'LocalLift',
  description: 'Local visibility intelligence across Google Search, Google Maps and AI answers, with managed execution.',
  parentOrganization: {'@type': 'Organization', name: 'The SocialDM', url: SITE.parentUrl},
  address: {'@type': 'PostalAddress', addressLocality: 'Phoenix', addressRegion: 'AZ', addressCountry: 'US'},
};
const graph = items => ({'@context': 'https://schema.org', '@graph': items});
const faqPage = list => ({'@type': 'FAQPage', mainEntity: list.map(([q, a]) => ({'@type': 'Question', name: q, acceptedAnswer: {'@type': 'Answer', text: a}}))});
const crumbs = list => ({'@type': 'BreadcrumbList', itemListElement: list.map(([name, p], i) => ({'@type': 'ListItem', position: i + 1, name, item: u(p)}))});
const webPage = (p, title, description) => ({'@type': 'WebPage', '@id': u(p) + '#page', url: u(p), name: title, description, isPartOf: {'@type': 'WebSite', name: 'LocalLift'}, publisher: {'@id': u('') + '#org'}, inLanguage: 'en'});

const IND_META = {
  'Multifamily': ['Multifamily Visibility for Apartment Communities', 'Help renters find, understand and tour your apartment communities across Google Search, Google Maps and AI answers, with weekly market and visibility intelligence.', 'Apartment owners and operators'],
  'Build to Rent': ['Build to Rent Marketing and Local Visibility', 'Make your build to rent community the one renters find and understand on Google, Google Maps and AI answers, from first phase through lease up.', 'Build to rent owners and operators'],
  'Medical': ['Local Visibility for Medical Practices', 'Help keep your practice hours and locations accurate on Google, Google Maps and AI answers, and see what referred patients find before they call.', 'Medical practices'],
  'Med Spa': ['Med Spa Marketing and Local Visibility', 'Help first time clients find and trust your med spa across Google Search, Google Maps and AI answers, with daily posts and review responses in your voice.', 'Med spas'],
  'Real Estate': ['Local Visibility for Real Estate Agents', 'Be the agent sellers find and AI assistants name for your neighborhoods, with map rank tracking, daily Google posts and review responses.', 'Real estate agents and teams'],
  'Hair Salons': ['Hair Salon Marketing and Local Visibility', 'Work to keep your salon in the first look on Google Maps and AI answers, with accurate hours, fresh posts and review responses in your voice.', 'Hair salons'],
  'Hospitality': ['Hotel and Hospitality Local Visibility', 'Help your hotel get named in AI travel answers and seen on Google Maps, with guest review responses and daily posts that keep your property current.', 'Hotels and hospitality businesses'],
  'Portfolios': ['Portfolio Visibility Reporting for Owners', 'See every property side by side on the same measures, with a weekly score and one recommended move for each property in your portfolio.', 'Property owners and asset managers'],
};

export function buildPages({IND, IND_SLUG, FAQS}) {
  const homeT = 'LocalLift | Local Visibility Intelligence for Google, Maps and AI';
  const homeD = 'LocalLift shows how your business appears across Google Search, Google Maps and AI answers, then strengthens it with intelligence, content and managed execution.';
  const indT = 'Industries | LocalLift Local Visibility by Industry';
  const indD = 'LocalLift for multifamily, build to rent, medical, med spa, real estate, hair salons, hospitality and portfolios. See how customers find each kind of business.';
  const pages = [
    {path: '', page: 'home', title: homeT, description: homeD,
     schema: [graph([org, {'@type': 'WebSite', '@id': u('') + '#site', url: u(''), name: 'LocalLift', publisher: {'@id': u('') + '#org'}}, webPage('', homeT, homeD), faqPage(FAQS.Home)])]},
    {path: 'industries', page: 'industries', title: indT, description: indD,
     schema: [graph([org, webPage('industries', indT, indD), crumbs([['LocalLift', ''], ['Industries', 'industries']]), faqPage(FAQS.Industries)])]},
  ];
  for (const x of IND) {
    const [t, d, aud] = IND_META[x.t], p = 'industries/' + IND_SLUG[x.t], title = `${t} | LocalLift`;
    pages.push({path: p, page: 'ind:' + x.t, title, description: d, schema: [graph([
      org, webPage(p, title, d),
      {'@type': 'Service', name: `LocalLift for ${x.t}`, serviceType: 'Local visibility management', description: d, provider: {'@id': u('') + '#org'}, areaServed: {'@type': 'Country', name: 'United States'}, audience: {'@type': 'BusinessAudience', name: aud}},
      crumbs([['LocalLift', ''], ['Industries', 'industries'], [x.t, p]]),
      faqPage(FAQS[x.t]),
    ])]});
  }
  for (const p of pages) if (p.title.length > 65 || p.description.length > 165) console.warn('long meta', p.path, p.title.length, p.description.length);
  return pages;
}
