// Page titles, descriptions and structured data for every page.
export const SITE = {name: 'LocalLift', parent: 'The SocialDM', parentUrl: 'https://www.thesocialdm.com/'};

const org = {
  '@context': 'https://schema.org', '@type': 'Organization', name: 'LocalLift',
  description: 'Local visibility intelligence across Google Search, Google Maps and AI answers, with managed execution.',
  parentOrganization: {'@type': 'Organization', name: 'The SocialDM', url: SITE.parentUrl},
  address: {'@type': 'PostalAddress', addressLocality: 'Phoenix', addressRegion: 'AZ', addressCountry: 'US'},
};

export const pageList = [
  {
    path: '', page: 'home',
    title: 'LocalLift | Local Visibility Intelligence for Google, Maps and AI',
    description: 'LocalLift shows how your business appears across Google Search, Google Maps and AI answers, then strengthens it with intelligence, content and managed execution.',
    schema: [org, {'@context': 'https://schema.org', '@type': 'WebSite', name: 'LocalLift', publisher: {'@type': 'Organization', name: 'LocalLift'}}],
  },
];
