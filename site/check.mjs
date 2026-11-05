// Copy rules check for every built page. Run after build: node check.mjs
import fs from 'fs';
import path from 'path';
const OUT = new URL('./dist/', import.meta.url).pathname;
const pages = [];
(function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (f === 'index.html') pages.push(p); } })(OUT);
const BANNED = /\b(yardi|rentcafe|entrata|realpage|costar|apartments\.com|zillow|local ?falcon|semrush|ahrefs|similarweb|brightlocal|whitespark|chatgpt|openai|gemini|perplexity|claude|copilot|metricool|windsor|supermetrics|search console|google analytics|ga4|hubspot|google business profile|realtor|klaviyo|canva|airtable|netlify|instagram|facebook|tiktok|linkedin)\b/i;
const REAL_CITIES = /\b(phoenix|scottsdale|tempe|mesa|chandler|gilbert|tigard|portland|seattle|denver|austin|dallas|houston|chicago|atlanta|miami|los angeles|san diego|las vegas)\b/i;
let bad = 0;
const titles = new Set();
const flag = (f, m) => { bad++; console.log('FAIL', path.relative(OUT, f) || 'index.html', m); };
for (const f of pages) {
  const html = fs.readFileSync(f, 'utf8');
  const ld = [...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)].map(m => m[1]).join(' ');
  const head = html.slice(0, html.indexOf('</head>'));
  const visible = html.slice(html.indexOf('<div id="root">')).replace(/<script[\s\S]*?<\/script>/g, ' ').replace(/<style[\s\S]*?<\/style>/g, ' ')
    .replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/&#x27;|&#39;/g, "'").replace(/&quot;/g, '"').replace(/\s+/g, ' ');
  const meta = [...head.matchAll(/<title>([^<]*)<\/title>|content="([^"]*)"/g)].map(m => m[1] || m[2]).filter(s => !/^(width|noindex|website|summary|#)/.test(s)).join(' | ');
  const copy = visible + ' | ' + meta + ' | ' + ld.replace(/"(@context|@type|url|item|@id)":"[^"]*"/g, '');
  for (const m of copy.matchAll(/.{0,30}[‐-―−].{0,30}/g)) flag(f, 'dash: ' + m[0]);
  for (const m of copy.matchAll(/.{0,30}[A-Za-z0-9] ?- ?[A-Za-z0-9].{0,30}/g)) if (!/https?:|www\.|@|\.com/.test(m[0])) flag(f, 'hyphen: ' + m[0]);
  const b = copy.match(BANNED); if (b) flag(f, 'named tool or source: ' + b[0]);
  const sampleText = visible.replace('The SocialDM™. Phoenix, Arizona.', '').replace('Montage, Tigard, Oregon', '');
  const rc = sampleText.match(REAL_CITIES); if (rc) flag(f, 'real city in sample copy: ' + rc[0]);
  for (const m of html.matchAll(/href="(\/[^"#]*)/g)) { const t = path.join(OUT, m[1], m[1].endsWith('/') || !path.extname(m[1]) ? 'index.html' : ''); if (!fs.existsSync(t)) flag(f, 'broken internal link: ' + m[1]); }
  for (const m of visible.replace('The SocialDM™. Phoenix, Arizona.', '').matchAll(/.{0,40}\b(phoenix|tigard|oregon|arizona)\b.{0,40}/gi)) console.log('NOTE real place', path.relative(OUT, f) || 'index.html', '::', m[0].trim());
  for (const m of visible.matchAll(/(\d{1,2},\d{3})\+? ?doors/gi)) if (+m[1].replace(',', '') > 7900) flag(f, 'door count over 7,900: ' + m[0]);
  if (/does not send|switched off/i.test(visible)) flag(f, 'old form switched off copy still present');
  if (/id="audit"/.test(html) && !/name="email"/.test(html)) flag(f, 'audit form is missing its email field');
  if (!/<title>[^<]{10,}<\/title>/.test(html)) flag(f, 'missing title');
  if (!/application\/ld\+json/.test(html)) flag(f, 'missing schema');
  let graph = [];
  try { for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) { const o = JSON.parse(m[1]); graph.push(...(o['@graph'] || [o])); } } catch (e) { flag(f, 'schema is not valid JSON'); }
  const fq = graph.find(o => o['@type'] === 'FAQPage');
  if (!fq) flag(f, 'missing FAQPage schema');
  if (!/id="faq"/.test(html)) flag(f, 'missing visible FAQ section');
  if (fq) for (const q of fq.mainEntity) if (!visible.includes(q.name)) flag(f, 'FAQ in schema but not on page: ' + q.name);
  if (!graph.some(o => o['@type'] === 'WebPage')) flag(f, 'missing WebPage schema');
  const t = (html.match(/<title>([^<]*)<\/title>/) || [])[1]; if (titles.has(t)) flag(f, 'duplicate title'); titles.add(t);
  if (!/<meta name="description" content="[^"]{50,}"/.test(html)) flag(f, 'missing meta description');
}
const js = fs.readFileSync(path.join(OUT, 'assets/app.js'), 'utf8');
if (!/const DOORS=7900;/.test(fs.readFileSync(path.join(path.dirname(new URL(import.meta.url).pathname), 'src/proto.js'), 'utf8'))) flag(OUT, 'DOORS constant is not 7900');
// interactive copy lives in the script bundle: check its string literals too
const strs = [...js.matchAll(/"([^"\\]{3,})"|`([^`]{3,})`/g)].map(m => m[1] || m[2]).join(' \n ');
const jb = strs.match(BANNED); if (jb) flag(OUT, 'named tool or source in script copy: ' + jb[0]);
for (const m of strs.matchAll(/.{0,30}[\u2010-\u2015\u2212].{0,30}/g)) flag(OUT, 'dash in script copy: ' + m[0]);
const jc = strs.replace('Montage, Tigard, Oregon', '').replace('Phoenix, Arizona', '').match(REAL_CITIES); if (jc) flag(OUT, 'real city in script copy: ' + jc[0]);
if (/realtor/i.test(strs)) flag(OUT, 'trademarked term in script copy: realtor');
for (const m of js.matchAll(/(\d,\d{3})\+/g)) if (+m[1].replace(',', '') > 7900) flag(OUT, 'door figure over 7,900 in script: ' + m[0]);
console.log(bad ? `${bad} problem(s) in ${pages.length} page(s)` : `OK: ${pages.length} page(s) pass the copy rules`);
process.exit(bad ? 1 : 0);
