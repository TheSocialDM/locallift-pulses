// Page titles, descriptions and structured data for every page.
export const SITE = {name: 'LocalLift', parent: 'The SocialDM', parentUrl: 'https://www.thesocialdm.com/'};

const org = {
  '@context': 'https://schema.org', '@type': 'Organization', name: 'LocalLift',
  description: 'Local visibility intelligence across Google Search, Google Maps and AI answers, with managed execution.',
  parentOrganization: {'@type': 'Organization', name: 'The SocialDM', url: SITE.parentUrl},
  address: {'@type': 'PostalAddress', addressLocality: 'Phoenix', addressRegion: 'AZ', addressCountry: 'US'},
};

const IND_META = {
  'Multifamily': ['Multifamily Visibility for Apartment Communities', 'Help renters find, understand and tour your apartment communities across Google Search, Google Maps and AI answers, with weekly market and visibility intelligence.'],
  'Build to rent': ['Build to Rent Marketing and Local Visibility', 'Make your build to rent community the one families find and understand on Google, Google Maps and AI answers, from first phase through lease up.'],
  'Medical': ['Local Visibility for Medical Practices', 'Keep your practice hours, locations and reputation accurate on Google, Google Maps and AI answers, so referred patients call you with confidence.'],
  'Med Spa': ['Med Spa Marketing and Local Visibility', 'Help first time clients find and trust your med spa across Google Search, Google Maps and AI answers, with daily posts and review responses in your voice.'],
  'Real Estate': ['Local Visibility for Real Estate Agents', 'Be the agent sellers find and AI assistants name for your neighborhoods, with map rank tracking, daily Google posts and review responses.'],
  'Hair Salons': ['Hair Salon Marketing and Local Visibility', 'Keep your salon in the first look on Google Maps and AI answers, with accurate hours, fresh posts and review responses in your voice.'],
  'Hospitality': ['Hotel and Hospitality Local Visibility', 'Get your hotel named in AI travel answers and seen on Google Maps, with guest review responses and daily posts that keep your property current.'],
  'Portfolios': ['Portfolio Visibility Reporting for Owners', 'See every property side by side on the same measures, with a weekly score and one recommended move for each property in your portfolio.'],
};

export function buildPages({IND, IND_SLUG}) {
  const pages = [{
    path: '', page: 'home',
    title: 'LocalLift | Local Visibility Intelligence for Google, Maps and AI',
    description: 'LocalLift shows how your business appears across Google Search, Google Maps and AI answers, then strengthens it with intelligence, content and managed execution.',
    schema: [org, {'@context': 'https://schema.org', '@type': 'WebSite', name: 'LocalLift', publisher: {'@type': 'Organization', name: 'LocalLift'}}],
  }, {
    path: 'industries', page: 'industries',
    title: 'Industries | LocalLift Local Visibility by Industry',
    description: 'LocalLift for multifamily, build to rent, medical, med spa, real estate, hair salons, hospitality and portfolios. See how customers find each kind of business.',
    schema: [org],
  }];
  for (const x of IND) {
    const [t, d] = IND_META[x.t];
    pages.push({path: 'industries/' + IND_SLUG[x.t], page: 'ind:' + x.t, name: x.t, title: `${t} | LocalLift`, description: d, schema: [org]});
  }
  return pages;
}
