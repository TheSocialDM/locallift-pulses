const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
for(const f of process.argv.slice(2)){const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});
await p.goto('file://'+f);await p.waitForTimeout(800);await p.screenshot({path:f.replace('.html','.png')});
const o=await p.evaluate(()=>[...document.querySelectorAll('*')].filter(e=>{const r=e.getBoundingClientRect();return r.right>1081||r.bottom>1351}).map(e=>e.className).slice(0,5));console.log(f,o);}
await b.close();})();
