/* LocalLift Tour Guide bubble. One file for every property.
   Usage: <script src="https://thesocialdm.github.io/locallift-pulses/guide/guide.js"
     data-name="Ava" data-property="Huxley Scottsdale" data-pro="Melanie"
     data-video="(mp4 url, optional)" data-poster="(image url, optional)"
     data-tour="url" data-offer="url" data-call="tel:+1..." data-color="#C8241D" defer></script> */
(function(){
var s=document.currentScript;if(!s)return;var d=s.dataset;
var C=d.color||'#C8241D',N=d.name||'Ava',P=d.property||'',PRO=d.pro||'your leasing pro',V=d.video||'',POS=d.poster||'',FACE=d.face||POS;
var css='.llg{position:fixed;right:14px;bottom:14px;z-index:9999;font:15px/1.45 Inter,system-ui,sans-serif;color:#111}'+
'.llg-b{width:92px;height:92px;border-radius:50%;border:3px solid '+C+';background:#111 center/cover;box-shadow:0 10px 30px rgba(0,0,0,.3);cursor:pointer;position:relative;overflow:hidden;padding:0;display:grid;place-items:center;color:#fff;font:700 28px Montserrat,Inter,sans-serif}'+
'.llg-b video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}'+
'.llg-b::after{content:"";position:absolute;inset:-3px;border-radius:50%;border:3px solid '+C+';animation:llgp 2.2s ease-out infinite}'+
'@keyframes llgp{0%{transform:scale(1);opacity:.7}100%{transform:scale(1.35);opacity:0}}'+
'@media(prefers-reduced-motion:reduce){.llg-b::after{animation:none}}'+
'.llg-tip{position:absolute;right:102px;bottom:28px;background:#fff;border-radius:14px;padding:8px 12px;box-shadow:0 8px 24px rgba(0,0,0,.18);white-space:nowrap;font-size:13px}'+
'.llg-tip b{color:'+C+'}'+
'.llg-p{position:absolute;right:0;bottom:104px;width:min(320px,calc(100vw - 28px));background:#fff;border-radius:20px;box-shadow:0 18px 50px rgba(0,0,0,.3);overflow:hidden;display:none}'+
'.llg.on .llg-p{display:block}.llg.on .llg-tip{display:none}'+
'.llg-v{position:relative;aspect-ratio:4/5;background:#111 center/cover;display:grid;place-items:center;color:#fff;text-align:center}'+
'.llg-v video{width:100%;height:100%;object-fit:cover;display:block}'+
'.llg-v .ph{padding:20px}.llg-v .ph b{display:block;font:700 40px Montserrat,Inter,sans-serif;width:84px;height:84px;line-height:84px;border-radius:50%;background:'+C+';margin:0 auto 12px}'+
'.llg-h{padding:12px 14px 4px;font-size:14px}.llg-h small{display:block;color:#6a6e75;font-size:11.5px}'+
'.llg-a{display:grid;gap:6px;padding:8px 14px 14px}.llg-a a{display:block;text-align:center;text-decoration:none;font-weight:600;border-radius:999px;padding:10px;border:1px solid #e5e5e5;color:#111}'+
'.llg-a a.m{background:'+C+';border-color:'+C+';color:#fff}'+
'.llg-x{position:absolute;top:8px;right:8px;z-index:2;width:30px;height:30px;border-radius:50%;border:0;background:rgba(0,0,0,.55);color:#fff;font-size:16px;cursor:pointer}';
var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
var w=document.createElement('div');w.className='llg';
var vid=V?'<video src="'+V+'" playsinline'+(POS?' poster="'+POS+'"':'')+'></video>':POS?'<img src="'+POS+'" alt="'+N+', your tour guide" style="width:100%;height:100%;object-fit:cover;display:block">':'<div class="ph"><b>'+N.charAt(0)+'</b>Hi, I\'m '+N+', your AI tour guide'+(P?' for '+P:'')+'.</div>';
var links='';if(d.tour)links+='<a class="m" href="'+d.tour+'" target="_blank" rel="noopener">Book my tour</a>';if(d.offer)links+='<a href="'+d.offer+'" target="_blank" rel="noopener">Today\'s offer</a>';if(d.call)links+='<a href="'+d.call+'">Call '+PRO+'</a>';
w.innerHTML='<div class="llg-p" role="dialog" aria-label="'+N+', AI tour guide"><button class="llg-x" aria-label="Close">×</button><div class="llg-v">'+vid+'</div><div class="llg-h"><b>'+N+'</b>, your tour guide'+(P?' at '+P:'')+'<small>AI guide. Your leasing pro is '+PRO+'.</small></div><div class="llg-a">'+links+'</div></div>'+
'<div class="llg-tip">Hi! I\'m <b>'+N+'</b>, your tour guide</div>'+
'<button class="llg-b" aria-label="Open '+N+', your AI tour guide"'+(FACE?' style="background-image:url(\''+FACE+'\');background-size:cover;background-position:center"':'')+'>'+(V?'<video src="'+V+'" muted playsinline autoplay loop'+(POS?' poster="'+POS+'"':'')+'></video>':(FACE?'':N.charAt(0)))+'</button>';
document.body.appendChild(w);
var pv=w.querySelector('.llg-v video');
w.querySelector('.llg-b').addEventListener('click',function(){var on=w.classList.toggle('on');if(pv){if(on){pv.currentTime=0;pv.muted=false;pv.play().catch(function(){})}else pv.pause()}});
w.querySelector('.llg-x').addEventListener('click',function(){w.classList.remove('on');if(pv)pv.pause()});
setTimeout(function(){var t=w.querySelector('.llg-tip');if(t)t.style.display='none'},9000);
})();
