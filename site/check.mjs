// Copy rules check for every built page. Run after build: node check.mjs
import fs from 'fs';
import path from 'path';
const OUT = new URL('./dist/', import.meta.url).pathname;
const pages = [];
(function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (f === 'index.html') pages.push(p); } })(OUT);
const BANNED = /\b(yardi|rentcafe|entrata|realpage|costar|apartments\.com|zillow|local ?falcon|semrush|ahrefs|similarweb|brightlocal|whitespark|chatgpt|openai|gemini|perplexity|claude|copilot|metricool|windsor|supermetrics|search console|google analytics|ga4|hubspot|klaviyo|canva|airtable|netlify|instagram|facebook|tiktok|linkedin)\b/i;
const REAL_CITIES = /\b(phoenix|scottsdale|tempe|mesa|chandler|gilbert|tigard|portland|seattle|denver|austin|dallas|houston|chicago|atlanta|miami|los angeles|san diego|las vegas)\b/i;
let bad = 0;
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
  for (const m of visible.matchAll(/.{0,40}\b(phoenix|tigard|oregon|arizona)\b.{0,40}/gi)) console.log('NOTE real place', path.relative(OUT, f) || 'index.html', '::', m[0].trim());
  for (const m of visible.matchAll(/(\d{1,2},\d{3})\+? ?doors/gi)) if (+m[1].replace(',', '') > 7900) flag(f, 'door count over 7,900: ' + m[0]);
  if (!/does not send yet/i.test(visible) && /id="audit"/.test(html)) flag(f, 'audit form missing does not send note');
  if (/<form[^>]*(action=|netlify|method=)/i.test(html)) flag(f, 'form has an action or Netlify attribute');
  if (/<input[^>]*\bname=/i.test(html)) flag(f, 'input has a name attribute');
  if (!/<title>[^<]{10,}<\/title>/.test(html)) flag(f, 'missing title');
  if (!/application\/ld\+json/.test(html)) flag(f, 'missing schema');
}
const js = fs.readFileSync(path.join(OUT, 'assets/app.js'), 'utf8');
if (!/const DOORS=7900;/.test(js)) flag(OUT, 'DOORS constant is not 7900');
console.log(bad ? `${bad} problem(s) in ${pages.length} page(s)` : `OK: ${pages.length} page(s) pass the copy rules`);
process.exit(bad ? 1 : 0);
