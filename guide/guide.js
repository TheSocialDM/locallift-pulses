/* LocalLift Tour Guide bubble. One file for every property.
   Usage: <script src="https://thesocialdm.github.io/locallift-pulses/guide/guide.js"
     data-name="Ava" data-property="Huxley Scottsdale" data-pro="Melanie"
     data-video="(mp4 url, optional)" data-poster="(image url, optional)"
     data-tour="url" data-offer="url" data-call="tel:+1..." data-color="#C8241D" defer></script> */
(function(){
var s=document.currentScript;if(!s)return;var d=s.dataset;
var ROLE=d.role||'your tour guide',SUB=d.sub||'';var C=d.color||'#C8241D',N=d.name||'Ava',P=d.property||'',PRO=d.pro||'your leasing pro',V=d.video||'',POS=d.poster||'',FACE=d.face||POS;
var css='.llg{position:fixed;right:14px;bottom:14px;z-index:9999;font:15px/1.45 Inter,system-ui,sans-serif;color:#111}'+
'.llg-b{width:92px;height:92px;border-radius:50%;border:3px solid '+C+';background:#111 center/cover;box-shadow:0 10px 30px rgba(0,0,0,.3);cursor:pointer;position:relative;overflow:hidden;padding:0;display:grid;place-items:center;color:#fff;font:700 28px Montserrat,Inter,sans-serif}'+
'.llg-b video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 30%;transform:scale(1.5);transform-origin:50% 30%}'+
'.llg-b::after{content:"";position:absolute;inset:-3px;border-radius:50%;border:3px solid '+C+';animation:llgp 2.2s ease-out infinite}'+
'@keyframes llgp{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.35);opacity:0}}'+
'@media(prefers-reduced-motion:reduce){.llg-b::after{animation:none}}'+
'.llg-tip{position:absolute;right:102px;bottom:28px;background:#fff;border-radius:14px;padding:8px 12px;box-shadow:0 8px 24px rgba(0,0,0,.18);white-space:nowrap;font-size:13px;transition:opacity .25s}'+
'.llg-tip.cap{white-space:normal;width:max-content;max-width:min(250px,calc(100vw - 132px))}.llg-tip.fade{opacity:0}'+
'.llg-tip b{color:'+C+'}'+
'.llg-p{position:absolute;right:0;bottom:104px;width:min(320px,calc(100vw - 28px));max-height:calc(100vh - 124px);max-height:calc(100dvh - 124px);overflow-y:auto;overflow-x:hidden;overscroll-behavior:contain;background:#fff;border-radius:20px;box-shadow:0 18px 50px rgba(0,0,0,.3);display:none}'+
'.llg.on .llg-p{display:block}@media(max-width:640px){.llg-p{position:fixed;left:8px;right:8px;bottom:8px;top:auto;width:auto;max-height:calc(100vh - 16px);max-height:calc(100dvh - 16px);z-index:5}.llg-v{height:min(46vh,calc(100vh - 300px));height:min(46dvh,calc(100dvh - 300px));min-height:150px}}.llg.on .llg-tip{display:none}'+
'.llg-v{position:relative;overflow:hidden;width:100%;height:min(400px,calc(100vh - 380px));height:min(400px,calc(100dvh - 380px));min-height:140px;background:#111 center/cover;display:grid;place-items:center;color:#fff;text-align:center}'+
'.llg-v video{width:100%;height:100%;object-fit:cover;object-position:50% 25%;display:block}'+
'.llg-v .ph{padding:20px}.llg-v .ph b{display:block;font:700 40px Montserrat,Inter,sans-serif;width:84px;height:84px;line-height:84px;border-radius:50%;background:'+C+';margin:0 auto 12px}'+
'.llg-h{padding:12px 14px 4px;font-size:14px}.llg-h small{display:block;color:#6a6e75;font-size:11.5px}'+
'.llg-a{display:grid;gap:6px;padding:8px 14px 14px}.llg-a a{display:block;text-align:center;text-decoration:none;font-weight:600;border-radius:999px;padding:10px;border:1px solid #e5e5e5;color:#111}'+
'.llg-a a.m{background:'+C+';border-color:'+C+';color:#fff}'+
'.llg-x{position:absolute;top:8px;right:8px;z-index:2;width:30px;height:30px;border-radius:50%;border:0;background:rgba(0,0,0,.55);color:#fff;font-size:16px;cursor:pointer}';
var SZ=parseInt(d.size||0,10);if(SZ)css+='.llg-b{width:'+SZ+'px;height:'+SZ+'px}.llg-tip{right:'+(SZ+10)+'px;bottom:'+Math.round(SZ/2-16)+'px}.llg-p{bottom:'+(SZ+12)+'px}';
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
/* data-intro: the bubble's first line, e.g. "Hi! I'm Mia. I'll get you to {pro}." {pro} becomes the agent's name (window.llBy) or data-pro. */
var PRO1=(window.llBy||PRO),INT=d.intro?d.intro.split('{pro}').join(PRO1):'';
function esc0(t){return String(t).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
var TIP0=INT?esc0(INT).split(N).join('<b>'+N+'</b>'):'Hi! I\'m <b>'+N+'</b>, '+ROLE;
var PREV=/[?&]src=preview\b/.test(location.search);
var w=document.createElement('div');w.className='llg';
var vid=V?'<video src="'+V+'" playsinline'+(POS?' poster="'+POS+'"':'')+'></video>':POS?'<img src="'+POS+'" alt="'+N+', your tour guide" style="width:100%;height:100%;object-fit:cover;object-position:50% 25%;display:block">':'<div class="ph"><b>'+N.charAt(0)+'</b>Hi, I\'m '+N+', your AI tour guide'+(P?' for '+P:'')+'.</div>';
var links='';if(d.tour)links+='<a class="m" href="'+d.tour+'" target="_blank" rel="noopener">'+(d.l1||'Book my tour')+'</a>';if(d.offer)links+='<a href="'+d.offer+'" target="_blank" rel="noopener">'+(d.l2||'Today\'s offer')+'</a>';if(d.call)links+='<a href="'+d.call+'">'+(d.l3||('Call '+PRO))+'</a>';
w.innerHTML='<div class="llg-p" role="dialog" aria-label="'+N+', AI tour guide"><button class="llg-x" aria-label="Close">×</button><div class="llg-v">'+vid+'</div><div class="llg-h"><b>'+N+'</b>, '+ROLE+(P?' at '+P:'')+'<small>'+(SUB||('AI guide. Your leasing pro is '+PRO+'.'))+'</small></div><div class="llg-a">'+links+'</div></div>'+
'<div class="llg-tip">'+TIP0+'</div>'+
'<button class="llg-b" aria-label="Open '+N+', your AI tour guide"'+(FACE?' style="background-image:url(\''+FACE+'\');background-size:cover;background-position:center;'+(d.facecss||'')+'"':'')+'>'+(V?'<video src="'+V+'" muted playsinline autoplay loop'+(POS?' poster="'+POS+'"':'')+'></video>':(FACE?'':N.charAt(0)))+'</button>';
document.body.appendChild(w);
var pv=w.querySelector('.llg-v video');
w.querySelector('.llg-b').addEventListener('click',function(){var on=w.classList.toggle('on');if(pv){if(on){pv.currentTime=0;pv.muted=false;pv.play().catch(function(){})}else pv.pause()}});
w.querySelector('.llg-x').addEventListener('click',function(){w.classList.remove('on');if(pv)pv.pause()});

/* data-vw: width share of the video frame that holds the person (e.g. 0.42 for a portrait framed inside a 16:9 file). Zooms just enough to hide side bars, never more. */
var VW=parseFloat(d.vw||0);
function fit(v,box,base){if(!VW||!v.videoWidth)return;var A=v.videoWidth/v.videoHeight,C=box.clientWidth/Math.max(1,box.clientHeight),sc=Math.max(1,(C/A)/VW)*(base||1);v.style.transform='scale('+sc.toFixed(3)+')';v.style.transformOrigin='50% 35%';v.style.objectPosition='50% 50%'}
if(VW){var bvv=w.querySelector('.llg-b video'),bbx=w.querySelector('.llg-b'),pbx=w.querySelector('.llg-v');
function fitP(v,box){if(!v.videoWidth)return;var A=v.videoWidth/v.videoHeight,P=A*(VW||1),H=box.clientHeight,Wt=Math.min(box.clientWidth,Math.round(H*P));v.style.width=Wt+'px';v.style.height=H+'px';v.style.transform='none';v.style.objectFit='cover';v.style.objectPosition='50% 50%'}
function refit(){if(bvv)fit(bvv,bbx,1.02);if(pv)fitP(pv,pbx)}
[bvv,pv].forEach(function(x){if(x)x.addEventListener('loadedmetadata',refit)});addEventListener('resize',refit);w.querySelector('.llg-b').addEventListener('click',function(){setTimeout(refit,30)});refit()}
var tip=w.querySelector('.llg-tip'),INTRO=tip.innerHTML,bv=w.querySelector('.llg-b video');
var CAP=(d.captions||'').split('|').map(function(x){return x.trim()}).filter(Boolean);
if(INT&&CAP.length)CAP[0]=INT;
if(PREV)tip.style.display='none';
/* data-tiphide: seconds before the speech bubble goes away for good, so it never sits over page text. data-size: bubble size in px. */
var TH=parseFloat(d.tiphide||0),TIPOFF=false;if(TH>0)setTimeout(function(){TIPOFF=true;tip.style.display='none'},TH*1000);
var scr=function(){if((window.scrollY||0)>60){tip.style.display='none';removeEventListener('scroll',scr)}};addEventListener('scroll',scr,{passive:true});
function esc(t){return t.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function fmt(t){t=esc(t);return N?t.split(N).join('<b>'+N+'</b>'):t}
var wts=CAP.map(function(c){return c.length+(/[.!?]$/.test(c)?10:/[,;:]$/.test(c)?4:1)}),tot=wts.reduce(function(a,b){return a+b},0),cur=-1;
function capAt(t,dur){if(!CAP.length||!dur)return -1;var x=t/dur*tot,a=0;for(var i=0;i<CAP.length;i++){a+=wts[i];if(x<a)return i}return CAP.length-1}
function show(i){if(TIPOFF||i===cur)return;cur=i;tip.classList.add('fade');setTimeout(function(){tip.innerHTML=i<0?INTRO:fmt(CAP[i]);tip.classList.toggle('cap',i>=0);tip.classList.remove('fade')},180)}
if(bv&&CAP.length){bv.addEventListener('timeupdate',function(){if(!w.classList.contains('on'))show(capAt(bv.currentTime,bv.duration))})}
else setTimeout(function(){if(!w.classList.contains('on'))tip.style.display='none'},9000);
function mini(){if(bv){bv.currentTime=0;cur=-2;show(-1);var p=bv.play();if(p&&p.catch)p.catch(function(){})}}
w.querySelector('.llg-x').addEventListener('click',mini);
w.querySelector('.llg-b').addEventListener('click',function(){if(bv){if(w.classList.contains('on'))bv.pause();else mini()}});
if(pv)pv.addEventListener('ended',function(){w.classList.remove('on');mini()});
})();
