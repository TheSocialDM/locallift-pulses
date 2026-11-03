/* Free AI visibility report sign up card: centered square over a dimmed page, stays until the visitor closes it.
   Shows once per visitor every 30 days (never again after they sign up), after they scroll half a page or spend 25 seconds.
   Submits into the existing Netlify "contact" form (interest = the business type, message = report request) and the same Make webhook as the contact page. */
(function(){
var RD=document.documentElement.dataset,PROD=RD.prod==="1",BASE=RD.base||"";
var page=(location.pathname.split("/").pop()||"index").replace(/\.html$/,"");
if(/^(contact|thank-you|privacy|terms)$/.test(page))return;
var KEY="sdmOffer",now=Date.now();
try{var v=localStorage.getItem(KEY);if(v==="done"||(v&&now-+v<30*864e5))return}catch(e){}
var icon=(PROD?"/":BASE)+"logo.png";
var pre=/real-estate/.test(page)?"Real Estate":/medical/.test(page)?"Medical":/med-spa/.test(page)?"Med Spa":/hair-salon/.test(page)?"Hair Salon":/hospitality/.test(page)?"Hospitality":/enterprise/.test(page)?"Portfolios":/multifamily|locallift|apartment/.test(page)?"Multifamily":"";
var OPTS=["Multifamily","Real Estate","Medical","Med Spa","Hair Salon","Hospitality","Portfolios","Other"];
var css=".sdmo-bg{position:fixed;inset:0;z-index:60;background:rgba(6,5,16,.62);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px);display:grid;place-items:center;padding:16px;opacity:0;transition:opacity .35s}"+
".sdmo-bg.in{opacity:1}"+
".sdmo{position:relative;width:min(440px,100%);max-height:calc(100vh - 32px);overflow:auto;background:radial-gradient(90% 60% at 50% 0%,rgba(75,79,184,.45),transparent 70%),#0F0C24;color:#fff;border:1px solid rgba(255,255,255,.14);border-radius:22px;padding:34px 30px 26px;box-shadow:0 30px 80px rgba(0,0,0,.55);text-align:center;font-family:var(--body,system-ui,sans-serif);transform:translateY(18px) scale(.98);transition:transform .45s cubic-bezier(.2,.8,.2,1)}"+
".sdmo-bg.in .sdmo{transform:none}"+
".sdmo .lg{width:112px;margin:0 auto 16px}.sdmo .lg img{width:100%;height:auto;display:block}"+
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
"@media (max-width:520px){.sdmo{padding:24px 18px 16px;border-radius:18px}.sdmo .lg{width:92px;margin-bottom:12px}.sdmo h2{font-size:22px}.sdmo p.sub{font-size:14px;margin-bottom:14px}.sdmo form{gap:8px}.sdmo input,.sdmo select{padding:11px 12px;font-size:16px}.sdmo .no{margin-top:8px}}"+
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
