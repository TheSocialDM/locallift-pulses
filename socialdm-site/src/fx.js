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
