// Builds the LocalLift preview site into dist/. Run: node build.mjs
import fs from 'fs';
import path from 'path';
import React from 'react';
import {renderToString} from 'react-dom/server';
import htm from 'htm';
import {transformSync} from 'esbuild';
import {buildPages, SITE} from './src/meta.mjs';

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const OUT = path.join(ROOT, 'dist');
const read = f => fs.readFileSync(path.join(ROOT, f), 'utf8');
const PREVIEW = process.env.LIVE !== '1'; // preview builds are always noindex

const body = read('src/proto.js') + '\n' + read('src/pages.js');
const prelude = 'const {useState,useEffect,useRef,useMemo}=React;const html=htm.bind(React.createElement);\n';
const factory = new Function('React', 'htm', 'window', prelude + body + '\nreturn {PAGES,IND,IND_SLUG,IND_COPY,FAQS};');
const data = factory(React, htm, undefined);
const {PAGES} = data;
const pageList = buildPages(data);

fs.rmSync(OUT, {recursive: true, force: true});
fs.mkdirSync(path.join(OUT, 'assets/vendor'), {recursive: true});
fs.cpSync(path.join(ROOT, 'public'), OUT, {recursive: true});
for (const f of ['react/umd/react.production.min.js', 'react-dom/umd/react-dom.production.min.js', 'htm/dist/htm.umd.js'])
  fs.copyFileSync(path.join(ROOT, 'node_modules', f), path.join(OUT, 'assets/vendor', path.basename(f)));
fs.writeFileSync(path.join(OUT, 'assets/site.css'), read('src/site.css') + '\n' + read('src/extra.css'));
fs.writeFileSync(path.join(OUT, 'assets/app.js'), transformSync(
  '(function(){' + prelude + body +
  '\nvar P=PAGES[window.__PAGE__],R=document.getElementById("root");if(P){if(REDUCED)ReactDOM.createRoot(R).render(React.createElement(P));else ReactDOM.hydrateRoot(R,React.createElement(P));}})();', {minify: true, legalComments: 'none'}).code);

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
for (const p of pageList) {
  const Comp = PAGES[p.page];
  if (!Comp) throw new Error('No component for ' + p.page);
  const app = renderToString(React.createElement(Comp));
  const ld = p.schema.map(o => `<script type="application/ld+json">${JSON.stringify(o).replace(/</g, '\\u003c')}</script>`).join('\n');
  const doc = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>${esc(p.title)}</title>
<meta name="description" content="${esc(p.description)}">
${PREVIEW ? '<meta name="robots" content="noindex,nofollow">' : ''}
${SITE.url ? `<link rel="canonical" href="${SITE.url}/${p.path ? p.path + '/' : ''}">` : ''}
<meta property="og:type" content="website">
<meta property="og:site_name" content="LocalLift">
<meta property="og:title" content="${esc(p.title)}">
<meta property="og:description" content="${esc(p.description)}">
${SITE.url ? `<meta property="og:url" content="${SITE.url}/${p.path ? p.path + '/' : ''}">` : ''}
<meta property="og:image" content="${SITE.url}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="LocalLift. Your next customer is searching. Will they find you?">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="${SITE.url}/assets/og-image.png">
<meta name="theme-color" content="#000000">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@300..700&family=Geist+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap">
<link rel="stylesheet" href="/assets/site.css">
${ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div id="root">${app}</div>
<noscript><p style="padding:16px;background:#fff;color:#000">To request a Visibility Audit without JavaScript, email <a href="mailto:info@thesocialdm.com">info@thesocialdm.com</a>.</p></noscript>
<script>window.__PAGE__=${JSON.stringify(p.page)};</script>
<script src="/assets/vendor/react.production.min.js" defer></script>
<script src="/assets/vendor/react-dom.production.min.js" defer></script>
<script src="/assets/vendor/htm.umd.js" defer></script>
<script src="/assets/app.js" defer></script>
</body>
</html>
`;
  const file = path.join(OUT, p.path, 'index.html');
  fs.mkdirSync(path.dirname(file), {recursive: true});
  fs.writeFileSync(file, doc);
  console.log('built', p.path || '/');
}
fs.writeFileSync(path.join(OUT, 'robots.txt'), PREVIEW ? 'User-agent: *\nDisallow: /\n' : `User-agent: *\nAllow: /\nSitemap: ${SITE.url}/sitemap.xml\n`);
if (!PREVIEW && SITE.url) fs.writeFileSync(path.join(OUT, 'sitemap.xml'), `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${pageList.map(p => `<url><loc>${SITE.url}/${p.path ? p.path + '/' : ''}</loc></url>`).join('\n')}\n</urlset>\n`);
fs.writeFileSync(path.join(OUT, '_headers'), PREVIEW ? '/*\n  X-Robots-Tag: noindex, nofollow\n' : '');
