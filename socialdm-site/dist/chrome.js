/* Shared header, dropdown menus and footer for every page of the draft site. Edit the menu here once and every page updates. */
(function(){
var M=[
 {t:"Solutions",items:[["LocalLift™","locallift.html","Google, Maps and AI visibility"],["Multifamily","multifamily-marketing-agency.html","Social and search for apartments"],["Real Estate","real-estate.html","Agents, teams and brokerages"],["Medical","medical.html","Visibility for practices"],["Med Spa","med-spa.html","Aesthetics and med spas"],["Hair Salons","hair-salon.html","Salons and independent stylists"],["LocalLift Signature \u2197","https://www.localliftsignature.com","Done for you posts for agents"],["Hospitality","hospitality.html","Hotels, resorts and venues"],["Portfolios","enterprise.html","Operators, groups and multi location brands"]]},
 {t:"Company",items:[["About","about.html"],["Contact","contact.html"]]},
 {t:"Research",items:[["Research & Insights","research-insights.html"],["Market Intelligence","blog.html","The blog"],["How Multifamily Visibility Works","multifamily-marketing-agency.html"],["2026 Multifamily Visibility Report","2026-multifamily-visibility-report.html"]]}
];
var R=document.documentElement.dataset,PROD=R.prod==="1",BASE=R.base||"";
function L(h){if(/^(https?:|mailto:|#)/.test(h))return h;if(PROD)return "/"+h.replace(/\.html$/,"").replace(/^index$/,"");return BASE+h}
var here=(location.pathname.split("/").pop()||"index.html");if(here.indexOf(".")<0)here+=".html";
function esc(s){return s.replace(/&/g,"&amp;").replace(/</g,"&lt;")}
var soc='<a class="soc" href="https://www.instagram.com/the.socialdm/" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg></a><a class="soc" href="https://www.facebook.com/thesocialdm" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 8h3V4h-3c-2.8 0-4 1.7-4 4.3V10H7v4h3v8h4v-8h3l1-4h-4V8.5c0-.3.2-.5.5-.5z"/></svg></a><a class="soc" href="https://www.tiktok.com/@thesocialdm" aria-label="TikTok"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 3c.4 2.3 1.9 3.9 4.2 4.1v3.3c-1.5.1-2.9-.4-4.2-1.2v6.1c0 3.6-2.9 6.2-6.3 5.9-2.9-.3-5.1-2.8-5-5.8.1-3.3 3.1-5.8 6.4-5.3v3.4c-1.5-.4-3 .6-3.2 2.1-.2 1.4.8 2.6 2.2 2.7 1.4.1 2.6-1 2.6-2.4V3z"/></svg></a><a class="soc" href="https://www.youtube.com/@thesocialdm" aria-label="YouTube"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 8.2a3 3 0 0 0-2.1-2.1C18 5.6 12 5.6 12 5.6s-6 0-7.9.5A3 3 0 0 0 2 8.2 31 31 0 0 0 1.6 12 31 31 0 0 0 2 15.8a3 3 0 0 0 2.1 2.1c1.9.5 7.9.5 7.9.5s6 0 7.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-3.8 31 31 0 0 0-.4-3.8zM10 15.1V8.9l5.2 3.1z"/></svg></a>';
var nav=M.map(function(g,i){var isHere=g.items.some(function(x){return x[1]===here});return '<div class="dd'+(isHere?' here':'')+'"><button type="button" aria-expanded="false" aria-controls="m'+i+'">'+g.t+'</button><div class="menu" id="m'+i+'">'+g.items.map(function(x){return '<a href="'+L(x[1])+'"'+(x[1]===here?' aria-current="page"':'')+'>'+esc(x[0])+(x[2]?'<small>'+x[2]+'</small>':'')+'</a>'}).join("")+'</div></div>'}).join("");
var h=document.getElementById("site-header");
if(h){h.outerHTML='<header><div class="wrap"><a class="logo" href="'+L("index.html")+'" aria-label="The SocialDM home"><img src="'+(PROD?"/":BASE)+'logo.png" alt="The SocialDM"></a><nav class="nav" aria-label="Main">'+nav+'<a class="top" href="'+L("locallift.html")+'"'+(here==='locallift.html'?' aria-current="page"':'')+'>LocalLift&trade;</a><a class="top" href="'+L("blog.html")+'"'+(here==='blog.html'?' aria-current="page"':'')+'>Insights</a></nav><div class="hright"><span class="socs">'+soc+'</span><a class="hlink" href="mailto:info@thesocialdm.com">Email us</a><a class="btn btn-light hcta" href="'+L("contact.html")+'">Get your visibility plan</a><button class="burger" type="button" aria-label="Open menu" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div></div></header>'+
 '<div class="sheet" role="dialog" aria-modal="true" aria-label="Menu"><div class="top"><a href="'+L("index.html")+'"><img src="'+(PROD?"/":BASE)+'logo.png" alt="The SocialDM"></a><button class="burger" type="button" aria-label="Close menu" style="display:grid"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div>'+
 M.map(function(g){return '<h4>'+g.t+'</h4>'+g.items.map(function(x){return '<a class="l" href="'+L(x[1])+'"'+(x[1]===here?' aria-current="page"':'')+'>'+esc(x[0])+'</a>'}).join("")}).join("")+
 '<a class="btn btn-light" href="'+L("contact.html")+'">Get your visibility plan</a></div>';}
var f=document.getElementById("site-footer");
if(f){f.outerHTML='<footer><div class="wrap"><div class="fgrid"><div><img src="'+(PROD?"/":BASE)+'logo.png" alt="The SocialDM"><p style="margin:16px 0 0;max-width:30ch">Multifamily marketing built for search, social and AI discovery.</p><p style="margin:10px 0 0"><a href="mailto:info@thesocialdm.com">info@thesocialdm.com</a></p></div>'+
 M.map(function(g){return '<div><h5>'+g.t+'</h5>'+g.items.map(function(x){return '<a href="'+L(x[1])+'">'+esc(x[0])+'</a>'}).join("")+'</div>'}).join("")+
 '</div><div class="brands"><h5>The SocialDM family</h5><div class="bgrid"><a href="'+L("index.html")+'"><b>The SocialDM&trade;</b><span>The hub. Social, search and AI visibility for multifamily.</span></a><a href="'+L("locallift.html")+'"><b>LocalLift&trade;</b><span>Google, Maps and AI visibility for apartment communities.</span></a><a href="https://www.localliftsignature.com" target="_blank" rel="noopener"><b>LocalLift Signature &#8599;</b><span>Done for you weekly posts for agents and title reps.</span></a></div></div><div class="fine"><span>The SocialDM&trade;, created in 2019. &copy; '+new Date().getFullYear()+' The SocialDM. LocalLift&trade; is a trademark of The SocialDM.</span><span><a href="https://www.instagram.com/the.socialdm/">Instagram</a> &nbsp; <a href="https://www.facebook.com/thesocialdm">Facebook</a> &nbsp; <a href="https://www.tiktok.com/@thesocialdm">TikTok</a> &nbsp; <a href="https://www.youtube.com/@thesocialdm">YouTube</a></span></div></div></footer>';}
document.querySelectorAll(".dd>button").forEach(function(b){b.addEventListener("click",function(e){var d=b.parentNode,o=!d.classList.contains("open");document.querySelectorAll(".dd.open").forEach(function(x){x.classList.remove("open");x.firstChild.setAttribute("aria-expanded","false")});if(o){d.classList.add("open");b.setAttribute("aria-expanded","true")}e.stopPropagation()})});
document.addEventListener("click",function(){document.querySelectorAll(".dd.open").forEach(function(x){x.classList.remove("open");x.firstChild.setAttribute("aria-expanded","false")})});
document.addEventListener("keydown",function(e){if(e.key==="Escape"){document.dispatchEvent(new Event("click"));var s=document.querySelector(".sheet.open");if(s){s.classList.remove("open");document.body.style.overflow=""}}});
var sh=document.querySelector(".sheet");
document.querySelectorAll(".burger").forEach(function(b){b.addEventListener("click",function(){var o=!sh.classList.contains("open");sh.classList.toggle("open",o);document.body.style.overflow=o?"hidden":""})});
})();

window.SDM_POP={"reviews": [{"q": "Working with TheSocialDM has strengthened our brand visibility and positioning across our apartment…", "n": "Katie M.", "r": "Multifamily client", "v": ["multifamily", "home"], "g": 1}, {"q": "Working with TheSocialDM has strengthened my professional visibility and brand consistency in the…", "n": "Jody S.", "r": "Broker, Arizona real estate", "v": ["real-estate", "home"], "g": 1}, {"q": "Working with TheSocialDM has strengthened my visibility and professional presence within the real…", "n": "Shari G.", "r": "Real estate client", "v": ["real-estate", "home"], "g": 1}, {"q": "Since working with Social DM, my social media has become more consistent, more professional, and…", "n": "Alex R.", "r": "Client", "v": ["real-estate", "home", "multifamily"], "g": 1}, {"q": "The SocialDM made our community look the way it feels in person.", "n": "Alissa", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "I finally have a partner who handles our online presence from start to finish.", "n": "Maria", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "Working with The SocialDM has been easy from day one.", "n": "Janelle", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "Our listing, reviews and social pages finally tell the same story.", "n": "Sara", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "The SocialDM is responsive, creative and dependable.", "n": "Lisa", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "I love how proactive this team is.", "n": "Cristy", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "Clear communication, great content and real follow through.", "n": "Jim", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "The SocialDM took a lot off my plate.", "n": "Claudia", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "From reviews to social to search, The SocialDM keeps our community front and center.", "n": "Robyn", "r": "Property Manager", "v": ["multifamily", "home"], "g": 0}, {"q": "Since working with The SocialDM, my online presence finally matches the way I do business.", "n": "Mark D.", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "The SocialDM keeps my brand consistent every single week.", "n": "Samantha", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "I finally feel confident sending people to my profiles.", "n": "Joanna", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "Working with The SocialDM has made me more visible in my market.", "n": "Pamela", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "The content is local, smart and on brand.", "n": "Jay", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "Professional, consistent and strategic.", "n": "Michael", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "I used to post when I had time, which was never.", "n": "Charlie", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "The SocialDM took the guesswork out of my marketing.", "n": "Maria", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "Great team, great communication and real results in how I show up online.", "n": "Sam", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "From listings to market updates, everything The SocialDM creates feels polished and local.", "n": "Kaley", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "The SocialDM helped me build a brand I am proud of.", "n": "Leila", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}, {"q": "Consistent, beautiful content every week without the stress.", "n": "Natalie", "r": "Real estate agent", "v": ["real-estate", "home"], "g": 0}]};
/* Social proof popup (same pattern as LocalLift Signature): rotates real activity, Google reviews and client testimonials, plus one call to action.
   Reviews come from tools/testimonials.json (injected by build.py as window.SDM_POP). Activity comes from /activity.json: real events only, city only, never names; events older than 14 days are skipped. */
(function(){
var D=window.SDM_POP;if(!D||!D.reviews||!D.reviews.length)return;
var RD=document.documentElement.dataset,PROD=RD.prod==="1",BASE=RD.base||"";
var page=(location.pathname.split("/").pop()||"index").replace(/\.html$/,"");
if(/^(contact|thank-you)$/.test(page))return;
try{if(sessionStorage.getItem("sdmPopOff")==="1")return}catch(e){}
var V=/real-estate/.test(page)?"real-estate":/multifamily|locallift|apartment/.test(page)?"multifamily":"home";
var icon=(PROD?"/":BASE)+"logo.png",go=PROD?"/contact":BASE+"contact.html";
var css=".sdmp{position:fixed;left:calc(20px + env(safe-area-inset-left,0px));bottom:calc(20px + env(safe-area-inset-bottom,0px));z-index:30;width:min(360px,calc(100vw - 32px));background:#0A0914;color:#fff;border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:14px 42px 14px 14px;display:flex;gap:12px;align-items:center;box-shadow:0 20px 50px rgba(0,0,0,.45);transition:transform .45s cubic-bezier(.2,.8,.2,1),opacity .45s;font-family:var(--body,system-ui,sans-serif)}"+
".sdmp.out{transform:translateY(24px);opacity:0;pointer-events:none}.sdmp.go{cursor:pointer}.sdmp.go small{color:#F0566A}"+
".sdmp .pin{width:64px;height:64px;border-radius:14px;flex:none;background:#14112E;box-shadow:inset 0 0 0 1px rgba(255,255,255,.12);display:grid;place-items:center;padding:7px;box-sizing:border-box}"+
".sdmp .pin img{width:100%;height:100%;display:block;object-fit:contain}"+
".sdmp b{display:block;font:600 14px/1.35 var(--body,system-ui,sans-serif)}.sdmp small{display:block;font-size:12px;color:rgba(255,255,255,.55);margin-top:3px}"+
".sdmp .st{color:#F5B83D;letter-spacing:1px;margin-right:4px}"+
".sdmp .x{position:absolute;top:8px;right:8px;width:30px;height:30px;border:0;border-radius:8px;background:transparent;color:rgba(255,255,255,.55);font-size:18px;cursor:pointer}"+
".sdmp .x:hover{color:#fff}"+
"@media (max-width:560px){.sdmp{left:50%;transform:translateX(-50%)}.sdmp.out{transform:translate(-50%,24px)}}"+
"@media (prefers-reduced-motion:reduce){.sdmp{transition:none}}";
var s=document.createElement("style");s.textContent=css;document.head.appendChild(s);
var el=document.createElement("div");el.className="sdmp out";el.setAttribute("role","status");el.setAttribute("aria-live","polite");
el.innerHTML='<div class="pin" aria-hidden="true"><img src="'+icon+'" alt=""></div><div><b></b><small></small></div><button class="x" type="button" aria-label="Hide">&times;</button>';
document.body.appendChild(el);
var M=el.querySelector("b"),T=el.querySelector("small");
function esc(x){return String(x).replace(/&/g,"&amp;").replace(/</g,"&lt;")}
var revs=D.reviews.filter(function(r){return r.v.indexOf(V)>=0});
if(revs.length<4)revs=D.reviews.filter(function(r){return r.v.indexOf("home")>=0});
revs.sort(function(a,b){return (b.g-a.g)||(Math.random()-.5)});
var REV=revs.map(function(r){return {m:"“"+r.q+"”",t:(r.g?'<span class="st">★★★★★</span>':"")+esc(r.n)+(r.r?", "+esc(r.r):"")+" · "+(r.g?"Google review":"Client testimonial")}});
var CTA={m:"Free visibility check: see where you show up on Google, Maps and AI.",t:"Get yours free →",go:1};
var EV=[];
function ago(d){var n=Math.round((Date.now()-new Date(d+"T12:00:00-07:00"))/864e5);return n<=0?"Today":n===1?"Yesterday":n<7?n+" days ago":n<14?"Last week":"Recently"}
function fresh(x){return x&&typeof x.m==="string"&&x.d&&(Date.now()-new Date(x.d+"T12:00:00-07:00"))/864e5<=14}
var Q=[];
function build(){Q=[];var r=REV.slice(),k=0;EV.slice(0,6).forEach(function(e){Q.push({m:e.m,t:ago(e.d),a:1});if(r.length)Q.push(r.shift())});
 while(r.length){Q.push(r.shift());if(++k%3===0)Q.push(CTA)}if(Q[Q.length-1]!==CTA)Q.push(CTA)}
build();
/* two real activity feeds: this site's /activity.json and the LocalLift Signature feed (same company, same rules) */
var FEEDS=[(PROD?"/":BASE)+"activity.json","https://cdn.jsdelivr.net/gh/TheSocialDM/locallift-pulses@main/signature/activity.json"],ALL=[],SEEN={};
FEEDS.forEach(function(u){try{fetch(u,{cache:"no-store"}).then(function(r){return r.ok?r.json():null}).then(function(j){if(j&&Array.isArray(j.events)){j.events.filter(fresh).forEach(function(x){if(!SEEN[x.m+x.d]){SEEN[x.m+x.d]=1;ALL.push(x)}});ALL.sort(function(a,b){return a.d<b.d?1:-1});EV=ALL;build()}}).catch(function(){})}catch(e){}});
var i=0,tm,off=false,cur=null;
function show(){if(off||!Q.length)return;var e=cur=Q[i++%Q.length];M.textContent=e.m;T.innerHTML=e.t;el.classList.toggle("go",!!e.go);el.classList.remove("out");clearTimeout(tm);tm=setTimeout(function(){el.classList.add("out");tm=setTimeout(show,6000)},e.go?7000:8000)}
el.addEventListener("click",function(ev){if(ev.target.closest(".x"))return;if(cur&&cur.go)location.href=go});
el.querySelector(".x").onclick=function(){off=true;clearTimeout(tm);el.classList.add("out");try{sessionStorage.setItem("sdmPopOff","1")}catch(e){}};
setTimeout(show,4000);
})();

/* Free AI visibility report sign up card: centered square over a dimmed page, stays until the visitor closes it.
   Shows once per visitor every 30 days (never again after they sign up), after they scroll half a page or spend 25 seconds.
   Submits into the existing Netlify "contact" form (interest = the business type, message = report request) and the same Make webhook as the contact page. */
(function(){
var RD=document.documentElement.dataset,PROD=RD.prod==="1",BASE=RD.base||"";
var page=(location.pathname.split("/").pop()||"index").replace(/\.html$/,"");
if(/^(contact|thank-you|privacy|terms)$/.test(page))return;
var KEY="sdmOffer",now=Date.now();
try{var v=localStorage.getItem(KEY);if(v==="done"||(v&&now-+v<30*864e5))return}catch(e){}
var icon=(PROD?"/":BASE)+"icon-192.png";
var pre=/real-estate/.test(page)?"Real Estate":/medical/.test(page)?"Medical":/med-spa/.test(page)?"Med Spa":/hair-salon/.test(page)?"Hair Salon":/hospitality/.test(page)?"Hospitality":/enterprise/.test(page)?"Portfolios":/multifamily|locallift|apartment/.test(page)?"Multifamily":"";
var OPTS=["Multifamily","Real Estate","Medical","Med Spa","Hair Salon","Hospitality","Portfolios","Other"];
var css=".sdmo-bg{position:fixed;inset:0;z-index:60;background:rgba(6,5,16,.62);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);display:grid;place-items:center;padding:16px;opacity:0;transition:opacity .35s}"+
".sdmo-bg.in{opacity:1}"+
".sdmo{position:relative;width:min(440px,100%);max-height:calc(100vh - 32px);overflow:auto;background:radial-gradient(90% 60% at 50% 0%,rgba(75,79,184,.45),transparent 70%),#0F0C24;color:#fff;border:1px solid rgba(255,255,255,.14);border-radius:22px;padding:34px 30px 26px;box-shadow:0 30px 80px rgba(0,0,0,.55);text-align:center;font-family:var(--body,system-ui,sans-serif);transform:translateY(18px) scale(.98);transition:transform .45s cubic-bezier(.2,.8,.2,1)}"+
".sdmo-bg.in .sdmo{transform:none}"+
".sdmo .lg{width:58px;height:58px;border-radius:50%;overflow:hidden;margin:0 auto 14px;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18)}.sdmo .lg img{width:100%;height:100%;display:block;transform:scale(1.18)}"+
".sdmo .ey{font:600 11px/1 var(--body,system-ui);letter-spacing:.18em;text-transform:uppercase;color:#7A8FE2;margin:0 0 10px}"+
".sdmo h2{font:700 27px/1.15 var(--head,system-ui);letter-spacing:-.02em;margin:0 0 10px}.sdmo h2 span{background:linear-gradient(90deg,#fff,#B4C3F0 55%,#7A8FE2);-webkit-background-clip:text;background-clip:text;color:transparent}"+
".sdmo p.sub{font-size:15px;line-height:1.5;color:rgba(255,255,255,.74);margin:0 0 20px}"+
".sdmo form{display:grid;gap:10px;text-align:left}.sdmo .two{display:grid;grid-template-columns:1fr 1fr;gap:10px}"+
".sdmo input,.sdmo select{width:100%;box-sizing:border-box;font:400 15px/1.2 var(--body,system-ui);color:#fff;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.18);border-radius:10px;padding:13px 14px;outline:none}"+
".sdmo select{appearance:none;-webkit-appearance:none;background-image:linear-gradient(45deg,transparent 50%,#B4C3F0 50%),linear-gradient(135deg,#B4C3F0 50%,transparent 50%);background-position:calc(100% - 18px) 52%,calc(100% - 13px) 52%;background-size:5px 5px;background-repeat:no-repeat}"+
".sdmo select option{color:#0A0914}.sdmo input::placeholder{color:rgba(255,255,255,.45)}.sdmo input:focus,.sdmo select:focus{border-color:#7A8FE2}"+
".sdmo .sdmo-go{margin-top:4px;font:600 13px/1 var(--body,system-ui);letter-spacing:.12em;text-transform:uppercase;width:100%;padding:17px;border:0;border-radius:8px;background:#E9E8F2;color:#0A0914;cursor:pointer}.sdmo .sdmo-go:hover{background:#fff}"+
".sdmo .no{display:inline-block;margin-top:14px;background:none;border:0;color:rgba(255,255,255,.55);font:400 13px var(--body,system-ui);text-decoration:underline;cursor:pointer}"+
".sdmo .fine{font-size:11.5px;color:rgba(255,255,255,.45);margin:10px 0 0;text-align:center}"+
".sdmo .x{position:absolute;top:12px;right:12px;width:36px;height:36px;border:0;border-radius:50%;background:rgba(255,255,255,.08);color:#fff;font-size:20px;line-height:1;cursor:pointer}.sdmo .x:hover{background:rgba(255,255,255,.16)}"+
".sdmo .hp{position:absolute;left:-9999px}"+
".sdmo .ok{width:58px;height:58px;border-radius:50%;margin:6px auto 16px;display:grid;place-items:center;background:rgba(122,143,226,.18);color:#B4C3F0;font-size:28px}"+
"body.sdmo-open{overflow:hidden}body.sdmo-open .sdmp{display:none}"+
"@media (max-width:520px){.sdmo{padding:24px 18px 16px;border-radius:18px}.sdmo .lg{width:44px;height:44px;margin-bottom:10px}.sdmo h2{font-size:22px}.sdmo p.sub{font-size:14px;margin-bottom:14px}.sdmo form{gap:8px}.sdmo input,.sdmo select{padding:11px 12px;font-size:16px}.sdmo .no{margin-top:8px}}"+
"@media (prefers-reduced-motion:reduce){.sdmo-bg,.sdmo{transition:none}}";
var shown=false,bg;
function el(h){var d=document.createElement("div");d.innerHTML=h;return d.firstChild}
function close(){if(!bg)return;bg.classList.remove("in");document.body.classList.remove("sdmo-open");setTimeout(function(){bg&&bg.remove();bg=null},350);document.removeEventListener("keydown",esc)}
function esc(e){if(e.key==="Escape")close()}
function open(){if(shown)return;shown=true;try{if(localStorage.getItem(KEY)!=="done")localStorage.setItem(KEY,String(Date.now()))}catch(e){}
 var s=document.createElement("style");s.textContent=css;document.head.appendChild(s);
 bg=el('<div class="sdmo-bg" role="dialog" aria-modal="true" aria-labelledby="sdmo-h"><div class="sdmo">'+
  '<button class="x" type="button" aria-label="Close">&times;</button>'+
  '<div class="lg" aria-hidden="true"><img src="'+icon+'" alt=""></div>'+
  '<p class="ey">Free AI visibility report</p>'+
  '<h2 id="sdmo-h">Is AI recommending <span>you</span>, or your competitor?</h2>'+
  '<p class="sub">See where your business shows up on ChatGPT, Google AI, Google Search and Maps. Free, with no obligation.</p>'+
  '<form novalidate><p class="hp" aria-hidden="true"><input name="bot-field" tabindex="-1" autocomplete="off"></p>'+
  '<div class="two"><input name="first_name" placeholder="First name" autocomplete="given-name" required aria-label="First name"><input name="city" placeholder="City" autocomplete="address-level2" required aria-label="City"></div>'+
  '<input name="email" type="email" placeholder="Email address" autocomplete="email" required aria-label="Email address">'+
  '<input name="company" placeholder="Business or property name" autocomplete="organization" aria-label="Business or property name">'+
  '<select name="interest" required aria-label="Type of business"><option value="">Type of business</option>'+OPTS.map(function(o){return '<option'+(o===pre?" selected":"")+'>'+o+'</option>'}).join("")+'</select>'+
  '<button class="sdmo-go" type="submit">Get my free report</button>'+
  '<p class="fine">We only use your details to send your report. No spam.</p></form>'+
  '<button class="no" type="button">No thanks</button></div></div>');
 document.body.appendChild(bg);document.body.classList.add("sdmo-open");
 requestAnimationFrame(function(){bg.classList.add("in")});
 var box=bg.querySelector(".sdmo"),f=bg.querySelector("form");
 bg.querySelector(".x").onclick=close;bg.querySelector(".no").onclick=close;
 bg.addEventListener("click",function(e){if(e.target===bg)close()});
 document.addEventListener("keydown",esc);
 setTimeout(function(){var i=f.querySelector("input[name=first_name]");try{i.focus({preventScroll:true})}catch(e){}},400);
 f.addEventListener("submit",function(e){e.preventDefault();
  var bad=null;["first_name","city","email","interest"].forEach(function(n){var x=f.elements[n];x.style.borderColor="";if(!bad&&(!x.value.trim()||(n==="email"&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(x.value)))){bad=x}});
  if(bad){bad.style.borderColor="#F0566A";bad.focus();return}
  var name=f.elements.first_name.value.trim(),mail=f.elements.email.value.trim();
  if(!f.elements["bot-field"].value&&PROD){
   var d={first_name:name,last_name:"",email:mail,phone:"",company:f.elements.company.value.trim(),interest:f.elements.interest.value,
    message:"Free AI visibility report request (website popup). City: "+f.elements.city.value.trim()+". Page: "+location.pathname};
   var nf=new URLSearchParams({"form-name":"contact"});Object.keys(d).forEach(function(k){nf.append(k,d[k])});
   try{fetch("/",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:nf.toString()}).catch(function(){})}catch(err){}
   var mk=new URLSearchParams(d);mk.append("source","site");mk.append("sid",Date.now()+"-"+Math.random().toString(36).slice(2,10));
   try{navigator.sendBeacon("https://hook.us2.make.com/iohhty0efvjr39dni63w6nzco3wqp3t4",mk)}catch(err){}
   try{if(window.gtag)gtag("event","generate_lead",{form:"ai_report_popup"})}catch(err){}
  }
  try{localStorage.setItem(KEY,"done")}catch(err){}
  box.innerHTML='<button class="x" type="button" aria-label="Close">&times;</button><div class="ok" aria-hidden="true">&#10003;</div>'+
   '<p class="ey">Request received</p><h2 id="sdmo-h">Thank you, <span></span>!</h2>'+
   '<p class="sub">Your free AI visibility report is on its way. We will email it to <b></b>, so keep an eye on your inbox.</p>'+
   '<button class="sdmo-go" type="button" style="width:100%">Back to the site</button>';
  box.querySelector("h2 span").textContent=name;box.querySelector(".sub b").textContent=mail;
  box.querySelector(".x").onclick=close;box.querySelector(".sdmo-go").onclick=close;
 });
}
function onScroll(){var h=document.documentElement.scrollHeight-innerHeight;if(h>0&&scrollY/h>=.5){open();off()}}
function off(){removeEventListener("scroll",onScroll);clearTimeout(t)}
addEventListener("scroll",onScroll,{passive:true});
var t=setTimeout(function(){open();off()},25000);
window.sdmOfferOpen=open;
})();
