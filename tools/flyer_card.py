import re
p='live/montage-r8x2/v3/index.html';s=open(p).read()
old="more:()=>'<div class=\"lt\">More</div>'+helpSec()+V.updates()+V.score()+V.rivals()+deskCard(),"
assert s.count(old)==1
s=s.replace(old,"more:()=>'<div class=\"lt\">More</div>'+V.updates()+V.score()+V.rivals()+deskCard()+flyCard()+helpSec(),")
card=r'''const FLYURL='https://live.thesocialdm.com/montage-r8x2/flyer/LocalLift-Live-Montage-flyer.pdf';
const flyCard=()=>`<section class="w fly"><div class="flyh"><img src="../flyer/cover.jpg" alt="LocalLift Live flyer cover"><div><b>The LocalLift Live flyer</b><small>5 pages: what it is, your assistant, your card, every feature and setup. Print it, pin it or share it.</small></div></div><div class="flyb"><a href="../flyer/LocalLift-Live-Montage-flyer.pdf" target="_blank" rel="noopener" data-fly="open">Open the flyer</a><button data-fly="share">Share</button><a href="../flyer/LocalLift-Live-Montage-flyer.pdf" download data-fly="dl">Download PDF</a></div></section>`;
document.addEventListener('click',e=>{const b=e.target.closest('[data-fly]');if(!b)return;const k=b.dataset.fly;try{if(typeof gtag==='function')gtag('event','flyer_'+k,{app:'live_montage'})}catch(x){}
 if(k==='share'){e.preventDefault();if(navigator.share){navigator.share({title:'LocalLift Live flyer',url:FLYURL}).catch(()=>{})}else{(navigator.clipboard?navigator.clipboard.writeText(FLYURL):Promise.reject()).then(()=>{b.textContent='Link copied'},()=>{prompt('Copy this link',FLYURL)});setTimeout(()=>b.textContent='Share',2000)}}});
(()=>{const st=document.createElement('style');st.textContent=`.fly{background:#fff}.flyh{display:flex;gap:14px;align-items:center}.flyh img{width:64px;height:83px;flex:none;border-radius:8px;object-fit:cover;box-shadow:0 4px 14px rgba(0,0,0,.18)}.flyh b{display:block;font:700 17px -apple-system,system-ui,sans-serif}.flyh small{display:block;margin-top:3px;font:400 14px/1.4 -apple-system,system-ui,sans-serif;color:#6e6e73}.flyb{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}.flyb a,.flyb button{display:flex;align-items:center;justify-content:center;border:0;border-radius:12px;min-height:46px;font:700 15px -apple-system,system-ui,sans-serif;background:#f2f2f7;color:#1c1c1e;text-decoration:none;cursor:pointer}.flyb a:first-child{grid-column:1/-1;background:#111;color:#fff}@media(prefers-color-scheme:dark){.fly{background:#1c1c1e}.flyh b{color:#fff}.flyh small{color:#98989f}.flyb a,.flyb button{background:#2c2c2e;color:#fff}.flyb a:first-child{background:#fff;color:#000}}@media print{.fly{display:none}}`;document.head.appendChild(st)})();
'''
a="const deskCard=()=>"
assert s.count(a)==1
s=s.replace(a,card+a,1)
s=re.sub(r"const APPV='[^']*'","const APPV='2026-11-24e'",s)
open(p,'w').write(s);open('live/montage-r8x2/v3/version.txt','w').write('2026-11-24e\n');print('ok')
