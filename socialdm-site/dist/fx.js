(function(){
var RM=matchMedia('(prefers-reduced-motion: reduce)').matches;
var PICS=['p2462015.jpg','p1643383.jpg','p261102.jpg','p106399.jpg','p258154.jpg','p323705.jpg','p1571460.jpg','p1838554.jpg'];
/* 1. Cursor image trail in the hero */
var hero=document.querySelector('.hero');
if(hero&&!RM){
  var tr=document.createElement('div');tr.className='trail';hero.prepend(tr);
  var i=0,lx=-999,ly=-999;
  function drop(x,y){var im=new Image();im.src=PICS[i++%PICS.length];im.alt='';im.style.left=x+'px';im.style.top=y+'px';tr.appendChild(im);setTimeout(function(){im.remove()},1400)}
  hero.addEventListener('pointermove',function(e){if(e.pointerType!=='mouse')return;var r=hero.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;if(Math.hypot(x-lx,y-ly)>110){lx=x;ly=y;drop(x,y)}});
  /* phones and tablets: images follow the finger too (passive, so scrolling still works) */
  function tdrop(t,force){var r=hero.getBoundingClientRect(),x=t.clientX-r.left,y=t.clientY-r.top;if(force||Math.hypot(x-lx,y-ly)>70){lx=x;ly=y;drop(x,y)}}
  hero.addEventListener('touchstart',function(e){tdrop(e.touches[0],true)},{passive:true});
  hero.addEventListener('touchmove',function(e){tdrop(e.touches[0])},{passive:true});
  if(matchMedia('(hover: none)').matches){var vis=true;new IntersectionObserver(function(en){vis=en[0].isIntersecting}).observe(hero);
    setInterval(function(){if(!vis)return;var r=hero.getBoundingClientRect();drop(30+Math.random()*(r.width-60),r.height*.55+Math.random()*(r.height*.4))},650)}
}
/* 2. Drag to play board with simple physics */
var bd=document.querySelector('.play');
if(bd){
  var objs=[].slice.call(bd.querySelectorAll('.obj')),W,H;
  function size(){W=bd.clientWidth;H=bd.clientHeight}size();addEventListener('resize',size);
  var S=objs.map(function(el,k){var a=k/objs.length*Math.PI*2,rx=.38+.06*(k%2),ry=.34+.06*(k%3);
    var nx,ny;if(W<700){var top=k%2===0,col=Math.floor(k/2)%3;nx=8+col*(W-16)/3+(top?0:20);ny=(top?.04:.72)*H+(Math.floor(k/6))*70}else{nx=W/2+Math.cos(a)*W*rx-el.offsetWidth/2;ny=H/2+Math.sin(a)*H*ry-el.offsetHeight/2}return{el:el,x:nx,y:ny,vx:0,vy:0,r:(k%2?1:-1)*(3+k%5),t:Math.random()*6.28,drag:false}});
  var active=null,px,py,ox,oy,lt;
  S.forEach(function(s){s.el.addEventListener('pointerdown',function(e){active=s;s.drag=true;s.el.setPointerCapture(e.pointerId);var r=bd.getBoundingClientRect();ox=e.clientX-r.left-s.x;oy=e.clientY-r.top-s.y;px=e.clientX;py=e.clientY;lt=performance.now();s.el.style.zIndex=5;e.preventDefault()});
    s.el.addEventListener('pointermove',function(e){if(active!==s)return;var r=bd.getBoundingClientRect(),n=performance.now(),dt=Math.max(n-lt,8);s.vx=(e.clientX-px)/dt*16;s.vy=(e.clientY-py)/dt*16;px=e.clientX;py=e.clientY;lt=n;s.x=e.clientX-r.left-ox;s.y=e.clientY-r.top-oy});
    function up(){if(active===s){s.drag=false;active=null;s.el.style.zIndex=2}}s.el.addEventListener('pointerup',up);s.el.addEventListener('pointercancel',up)});
  /* floating hearts and thumbs, like live reactions: burst when a piece is grabbed, plus a gentle stream while on screen */
  var lk=bd.querySelector('.likes'),HEART='<svg viewBox="0 0 24 24"><path fill="#F0566A" d="M12 21s-7.5-4.6-9.6-9.4C.9 8.2 3 4.5 6.7 4.5c2.1 0 3.6 1.1 4.3 2.4h2c.7-1.3 2.2-2.4 4.3-2.4 3.7 0 5.8 3.7 4.3 7.1C19.5 16.4 12 21 12 21z"/></svg>',
      THUMB='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#0866FF"/><path fill="#fff" d="M7 11h2.5v7H7zM10.5 18v-6.6l3-4.4c.3-.4 1-.4 1.3.1.2.3.2.6.1.9L14 10.5h3.3c.8 0 1.4.8 1.2 1.6l-1.2 4.8c-.2.7-.8 1.1-1.5 1.1z"/></svg>';
  function burst(x,y,n){if(RM||!lk)return;for(var i=0;i<n;i++)(function(i){setTimeout(function(){var e=document.createElement('span');e.className='like';e.innerHTML=Math.random()<.62?HEART:THUMB;
    e.style.left=(x+(Math.random()-.5)*30)+'px';e.style.top=y+'px';e.style.setProperty('--dx1',((Math.random()-.5)*30)+'px');e.style.setProperty('--dx2',((Math.random()-.5)*90)+'px');
    lk.appendChild(e);setTimeout(function(){e.remove()},1700)},i*90)})(i)}
  S.forEach(function(s){s.el.addEventListener('pointerdown',function(){burst(s.x+s.el.offsetWidth/2,s.y,6)})});
  var bvis=false;if('IntersectionObserver' in window)new IntersectionObserver(function(en){bvis=en[0].isIntersecting}).observe(bd);
  setInterval(function(){if(!bvis||active)return;var s=S[Math.floor(Math.random()*S.length)];if(s.el.offsetParent)burst(s.x+s.el.offsetWidth/2,s.y,2)},1800);
  function tick(){S.forEach(function(s){var w=s.el.offsetWidth,h=s.el.offsetHeight;if(!s.drag){s.t+=.012;if(!RM){s.x+=s.vx+Math.cos(s.t)*.18;s.y+=s.vy+Math.sin(s.t*1.3)*.18}else{s.x+=s.vx;s.y+=s.vy}s.vx*=.94;s.vy*=.94;
      if(s.x<0){s.x=0;s.vx=Math.abs(s.vx)*.7}if(s.y<0){s.y=0;s.vy=Math.abs(s.vy)*.7}if(s.x>W-w){s.x=W-w;s.vx=-Math.abs(s.vx)*.7}if(s.y>H-h){s.y=H-h;s.vy=-Math.abs(s.vy)*.7}}
      if(W<700&&!s.drag){var a1=H*.36,b1=H*.64,cy=s.y+h/2;if(cy>a1&&cy<b1){s.vy+=(cy<H/2?-.6:.6)}}
      var rot=s.drag?0:s.r+(RM?0:Math.sin(s.t)*2);s.el.style.transform='translate('+s.x+'px,'+s.y+'px) rotate('+rot+'deg)'});requestAnimationFrame(tick)}tick();
}
/* 2b. Image wheel */
var ring=document.querySelector('.ring'),stage=document.querySelector('.stage');
if(ring){var ang=0,vel=RM?0:.12,dragging=false,lx2=0,lastY=scrollY;
  stage.addEventListener('pointerdown',function(e){dragging=true;lx2=e.clientX;stage.setPointerCapture(e.pointerId)});
  stage.addEventListener('pointermove',function(e){if(!dragging)return;var d=e.clientX-lx2;lx2=e.clientX;ang+=d*.3;vel=d*.3});
  function rel(){dragging=false}stage.addEventListener('pointerup',rel);stage.addEventListener('pointercancel',rel);
  addEventListener('scroll',function(){var d=scrollY-lastY;lastY=scrollY;if(!RM)vel+=d*.02},{passive:true});
  /* reels: load and play only while the wheel is on screen; tap opens the full reel with sound */
  var vids=[].slice.call(ring.querySelectorAll('video'));
  if(vids.length&&'IntersectionObserver' in window){new IntersectionObserver(function(en){var on=en[0].isIntersecting;vids.forEach(function(v){if(on){if(!v.src&&!RM)v.src=v.dataset.src;if(!RM){var p=v.play();if(p&&p.catch)p.catch(function(){})}}else v.pause()})},{rootMargin:'200px'}).observe(stage)}
  var dx0=0,dy0=0,dt0=0;stage.addEventListener('pointerdown',function(e){dx0=e.clientX;dy0=e.clientY;dt0=Date.now()},true);
  stage.addEventListener('pointerup',function(e){if(Math.abs(e.clientX-dx0)>6||Math.abs(e.clientY-dy0)>6||Date.now()-dt0>400)return;
    var el=document.elementFromPoint(e.clientX,e.clientY),c=el&&el.closest&&el.closest('.wc');if(c&&c.dataset.full)openReel(c.dataset.full,c.querySelector('video').getAttribute('aria-label'))});
  function openReel(src,label){var o=document.createElement('div');o.className='reel-box';o.setAttribute('role','dialog');o.setAttribute('aria-label',label||'Reel');
    o.innerHTML='<button class="reel-x" aria-label="Close">&times;</button><video controls autoplay playsinline src="'+src+'"></video>';document.body.appendChild(o);
    var v=o.querySelector('video');function close(){v.pause();o.remove();removeEventListener('keydown',k)}function k(ev){if(ev.key==='Escape')close()}
    o.addEventListener('click',function(ev){if(ev.target===o||ev.target.classList.contains('reel-x'))close()});addEventListener('keydown',k);o.querySelector('.reel-x').focus()}
  /* subtle invitations: play badges, a hint pill and one gentle flick when the wheel first appears */
  ring.querySelectorAll('.wc').forEach(function(c){var b=document.createElement('span');b.className='wplay';b.setAttribute('aria-hidden','true');b.innerHTML='<svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z"/></svg>';c.appendChild(b)});
  var hint=document.createElement('div');hint.className='wheel-hint';hint.innerHTML='<span class="wh-ic" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M7 8l-4 4 4 4M17 8l4 4-4 4M3 12h18"/></svg></span>'+(matchMedia('(hover: none)').matches?'Swipe to spin':'Drag to spin')+'<i></i><span class="wh-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></span>Tap a reel to watch';
  stage.parentNode.insertBefore(hint,stage.nextSibling);
  var used=false;function seen(){if(used)return;used=true;hint.classList.add('done')}
  stage.addEventListener('pointerdown',function(){setTimeout(seen,600)});
  if('IntersectionObserver' in window&&!RM){var flicked=false;new IntersectionObserver(function(en,o){if(en[0].isIntersecting&&!flicked){flicked=true;setTimeout(function(){if(!dragging)vel=5.5},500);o.disconnect()}},{threshold:.5}).observe(stage)}
  (function spin(){if(!dragging){ang+=vel;vel+=((RM?0:.12)-vel)*.03}ring.style.transform='translateZ(calc(var(--r) * -1)) rotateX(-6deg) rotateY('+ang+'deg)';requestAnimationFrame(spin)})();}
/* 2c. Ask AI typing demo */
var qt=document.querySelector('.aiq-t'),ans=document.querySelector('.aians');
if(qt){var Q=['Best apartments near downtown with a pool?','Pet friendly apartments near light rail?','Which new apartments have move in specials?'],qi=0;
  function typeQ(){var q=Q[qi++%Q.length],k=0;ans.hidden=true;qt.textContent='';
    if(RM){qt.textContent=q;ans.hidden=false;return}
    (function t(){qt.textContent=q.slice(0,++k);if(k<q.length)setTimeout(t,45+Math.random()*40);else setTimeout(function(){ans.hidden=false;setTimeout(typeQ,4200)},500)})()}
  new IntersectionObserver(function(en,o){if(en[0].isIntersecting){typeQ();o.disconnect()}}).observe(qt)}
/* 3. Scroll reveals */
var els=document.querySelectorAll('.block .split>*,.block .stats,.band .arches,.cta,.words h2,.block .h2,.block h2');
if('IntersectionObserver' in window&&!RM){var io=new IntersectionObserver(function(en){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.15});
  els.forEach(function(el){el.classList.add('rv-in');io.observe(el)})}
})();
/* Words section: inline photos tilt and drift as you scroll past */
(function(){var sec=document.querySelector('.words');if(!sec||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var imgs=[].slice.call(sec.querySelectorAll('h2 img'));if(!imgs.length)return;
var base=[-4,3,-3],dir=[1,-1,1],q=0;
function u(){q=0;var r=sec.getBoundingClientRect(),h=innerHeight;if(r.bottom<0||r.top>h)return;
  var p=((r.top+r.height/2)-h/2)/(h/2+r.height/2);p=Math.max(-1,Math.min(1,p));
  imgs.forEach(function(im,i){var d=dir[i%3];im.style.transform='translate('+(d*p*16)+'px,'+(p*-18)+'px) rotate('+(base[i%3]+d*p*9)+'deg) scale('+(1+(1-Math.abs(p))*.08)+')'})}
addEventListener('scroll',function(){if(!q)q=requestAnimationFrame(u)},{passive:true});addEventListener('resize',u);u()})();
