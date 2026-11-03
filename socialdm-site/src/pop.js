/* Social proof popup (same pattern as LocalLift Signature): rotates real activity, Google reviews and client testimonials, plus one call to action.
   Reviews come from tools/testimonials.json (injected by build.py as window.SDM_POP). Activity comes from /activity.json: real events only, city only, never names; events older than 14 days are skipped. */
(function(){
var D=window.SDM_POP;if(!D||!D.reviews||!D.reviews.length)return;
var RD=document.documentElement.dataset,PROD=RD.prod==="1",BASE=RD.base||"";
var page=(location.pathname.split("/").pop()||"index").replace(/\.html$/,"");
if(/^(contact|thank-you)$/.test(page))return;
try{if(sessionStorage.getItem("sdmPopOff")==="1")return}catch(e){}
var V=/real-estate/.test(page)?"real-estate":/multifamily|locallift|apartment/.test(page)?"multifamily":"home";
var icon=(PROD?"/":BASE)+"icon-192.png",go=PROD?"/contact":BASE+"contact.html";
var css=".sdmp{position:fixed;left:calc(20px + env(safe-area-inset-left,0px));bottom:calc(20px + env(safe-area-inset-bottom,0px));z-index:30;width:min(360px,calc(100vw - 32px));background:#0A0914;color:#fff;border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:14px 42px 14px 14px;display:flex;gap:12px;align-items:center;box-shadow:0 20px 50px rgba(0,0,0,.45);transition:transform .45s cubic-bezier(.2,.8,.2,1),opacity .45s;font-family:var(--body,system-ui,sans-serif)}"+
".sdmp.out{transform:translateY(24px);opacity:0;pointer-events:none}.sdmp.go{cursor:pointer}.sdmp.go small{color:#F0566A}"+
".sdmp .pin{width:44px;height:44px;border-radius:50%;overflow:hidden;flex:none;box-shadow:inset 0 0 0 1px rgba(255,255,255,.18);background:#1B1740}"+
".sdmp .pin img{width:100%;height:100%;display:block;transform:scale(1.18)}"+
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
