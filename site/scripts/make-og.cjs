// Renders public/assets/og-image.png (1200x630) from the existing brand assets: the white logo,
// the red pin, the site fonts and the hero headline. Run by hand when the brand changes:
//   node scripts/make-og.cjs
// Needs Playwright with Chromium. Not part of the Netlify build; the PNG is committed.
const fs = require('fs'), path = require('path');
const {chromium} = require('playwright');
const root = path.join(__dirname, '..');
const logo = 'data:image/png;base64,' + fs.readFileSync(path.join(root, 'public/assets/logo-white.png')).toString('base64');
const pin = '<path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319"/><circle cx="12" cy="12" r="4.6" fill="#fff"/>';
let roads = '';
for (let i = 0; i < 16; i++) roads += `<path d="M${i * 80 + 20} 0 C ${i * 80 + 50} 210, ${i * 80 - 10} 420, ${i * 80 + 30} 630" stroke="rgba(255,255,255,${i % 5 ? .06 : .14})" fill="none"/>`;
for (let j = 0; j < 9; j++) roads += `<path d="M0 ${j * 80 + 15} C 400 ${j * 80 + 45}, 800 ${j * 80 - 15}, 1200 ${j * 80 + 25}" stroke="rgba(255,255,255,${j % 4 ? .06 : .14})" fill="none"/>`;
const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@500;600&family=Geist+Mono:wght@400&family=Instrument+Serif:ital@1&display=block">
<style>
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;background:#000;color:#fff;font-family:Geist,Arial,sans-serif;overflow:hidden;position:relative}
.map{position:absolute;inset:0}
.shade{position:absolute;inset:0;background:linear-gradient(90deg,#000 0%,rgba(0,0,0,.9) 46%,rgba(0,0,0,0) 78%)}
.ring{position:absolute;left:930px;top:315px;border:2px solid #E22319;border-radius:50%;transform:translate(-50%,-50%)}
.pin{position:absolute;left:930px;top:315px;transform:translate(-50%,-92%)}
.in{position:absolute;left:72px;top:64px;right:72px}
.logo{height:56px;display:block}
.eye{margin-top:62px;font-family:"Geist Mono",monospace;font-size:20px;letter-spacing:.09em;text-transform:uppercase;color:rgba(255,255,255,.72);display:flex;align-items:center;gap:14px}
.eye i{width:10px;height:10px;border-radius:50%;background:#E22319;display:block}
h1{margin-top:22px;font-size:84px;line-height:.98;letter-spacing:-.05em;font-weight:600;max-width:760px}
h1 em{font-family:"Instrument Serif",Georgia,serif;font-style:italic;font-weight:400;letter-spacing:-.02em}
.url{position:absolute;left:72px;bottom:52px;font-family:"Geist Mono",monospace;font-size:22px;color:rgba(255,255,255,.72)}
</style></head><body>
<svg class="map" viewBox="0 0 1200 630" width="1200" height="630">${roads}</svg>
${[120, 240, 360, 480].map((d, i) => `<div class="ring" style="width:${d}px;height:${d}px;opacity:${.6 - i * .13}"></div>`).join('')}
<div class="shade"></div>
<svg class="pin" width="60" height="85" viewBox="0 0 24 34">${pin}</svg>
<div class="in"><img class="logo" src="${logo}" alt="">
<div class="eye"><i></i>Local visibility intelligence</div>
<h1>Your next customer is searching. <em>Will they find you?</em></h1></div>
<div class="url">localliftnow.com</div>
</body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1200, height: 630}, deviceScaleFactor: 1});
  await p.setContent(html, {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({path: path.join(root, 'public/assets/og-image.png')});
  await b.close();
  console.log('wrote public/assets/og-image.png');
})();
