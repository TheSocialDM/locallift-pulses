(function(){const {useState,useEffect,useRef,useMemo}=React;const html=htm.bind(React.createElement);
const LOGO_WHITE="/assets/logo-white.png",SDM_LOGO="/assets/socialdm-logo.png";
const REDUCED=typeof window!=='undefined'&&!!window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- shared helpers ---------- */
function rng(seed){return function(){seed|=0;seed=seed+0x6D2B79F5|0;let t=Math.imul(seed^seed>>>15,1|seed);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function makeRoads(w,h,seed,nx,ny){
  const r=rng(seed),roads=[];
  const line=(fn,major)=>{const pts=[];for(let i=0;i<=24;i++)pts.push(fn(i/24));roads.push({pts,major})};
  for(let i=0;i<=nx;i++){const x=w*i/nx+(r()-.5)*w/nx*.5,a=(r()-.5)*w*.035,f=1.5+r()*2,tilt=(r()-.5)*w*.03,major=r()<.16;line(t=>[x+Math.sin(t*f*3)*a+tilt*t,h*t],major)}
  for(let j=0;j<=ny;j++){const y=h*j/ny+(r()-.5)*h/ny*.5,a=(r()-.5)*h*.035,f=1.5+r()*2,tilt=(r()-.5)*h*.03,major=r()<.16;line(t=>[w*t,y+Math.sin(t*f*3)*a+tilt*t],major)}
  line(t=>[w*(-.05+t*1.1),h*(.92-t*.8)+Math.sin(t*5)*h*.04],true);
  line(t=>[w*(.15+t*.9),h*(.02+t*t*.98)],true);
  return roads;
}
const toPath=pts=>'M'+pts.map(p=>p[0].toFixed(1)+' '+p[1].toFixed(1)).join('L');
function useMedia(q){const[m,s]=useState(false);useEffect(()=>{if(!window.matchMedia)return;const l=matchMedia(q),f=e=>s(e.matches);s(l.matches);l.addEventListener('change',f);return()=>l.removeEventListener('change',f)},[q]);return m}

const Pin=({size=24,color="#E22319",hole="#fff"})=>html`<svg width=${size} height=${size*34/24} viewBox="0 0 24 34" aria-hidden="true"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill=${color}/><circle cx="12" cy="12" r="4.6" fill=${hole}/></svg>`;
const Logo=({h=40})=>html`<span className="logo"><img src=${LOGO_WHITE} alt="LocalLift" style=${{height:h+'px'}}/><span className="ring"></span><span className="ring b"></span></span>`;
const Eyebrow=({children})=>html`<div className="eyebrow"><i></i>${children}</div>`;

/* ---------- motion helpers ---------- */
function useInView(th=.2){
  const ref=useRef(null);const[seen,setSeen]=useState(false);const[vis,setVis]=useState(false);
  useEffect(()=>{if(!window.IntersectionObserver||!ref.current)return;const io=new IntersectionObserver(e=>{setVis(e[0].isIntersecting);if(e[0].isIntersecting)setSeen(true)},{threshold:th});io.observe(ref.current);return()=>io.disconnect()},[]);
  return[ref,seen,vis];
}
function Count({to,run,from=0,dur=1500}){
  const[v,setV]=useState(to);
  useEffect(()=>{if(!run||REDUCED){setV(to);return}let raf,t0;const step=t=>{t0=t0||t;const k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);setV(Math.round(from+(to-from)*e));if(k<1)raf=requestAnimationFrame(step)};raf=requestAnimationFrame(step);return()=>cancelAnimationFrame(raf)},[run,to]);
  return html`<span className="cnt">${v.toLocaleString('en-US')}</span>`;
}
function Pops({items,run}){
  const[i,setI]=useState(0);
  useEffect(()=>{setI(0);if(!run||REDUCED)return;const t=setInterval(()=>setI(x=>(x+1)%items.length),2900);return()=>clearInterval(t)},[run,items]);
  return html`<div className="pops" aria-hidden="true"><div className="pop" key=${i}><i></i><span>${items[i%items.length]}</span></div></div>`;
}
/* The one real number on these sample panels. Raise it here and every counter follows. */
const DOORS=7900; /* real door count. The counter ends here, so raising this raises every counter. */
const DOORS_FAST_TO=DOORS-24; /* quick climb to here, then a few final doors */
const doorStore={v:DOORS,started:false,subs:new Set()};
const setDoors=v=>{doorStore.v=v;doorStore.subs.forEach(f=>f(v))};
function startDoors(){
  if(doorStore.started||REDUCED)return;doorStore.started=true;
  const FROM=7400,DUR=1600;let t0;
  const step=t=>{t0=t0||t;const k=Math.min(1,(t-t0)/DUR);setDoors(Math.round(FROM+(DOORS_FAST_TO-FROM)*(1-Math.pow(1-k,3))));if(k<1)requestAnimationFrame(step);else{const i=setInterval(()=>{if(doorStore.v>=DOORS){clearInterval(i);return}setDoors(Math.min(DOORS,doorStore.v+1))},90)}};
  requestAnimationFrame(step);
}
function Doors(){
  const[v,setV]=useState(doorStore.v);
  useEffect(()=>{doorStore.subs.add(setV);setV(doorStore.v);startDoors();return()=>doorStore.subs.delete(setV)},[]);
  return html`<span className="cnt">${v.toLocaleString('en-US')}</span>`;
}
function DoorsStat(){
  return html`<span className="doors-stat"><i className="live-dot"></i><strong><${Doors}/>+</strong> doors and counting</span>`;
}

/* ---------- 1. navigation ---------- */
const NAV=[["Platform","/#platform"],["Industries","/industries/"],["Intelligence","/#intelligence"],["Results","/#results"]];
function Nav(){
  const[open,setOpen]=useState(false);
  return html`<header className="nav"><div className="wrap">
    <div className="nav-in">
      <a href="/" aria-label="LocalLift home"><${Logo}/></a>
      <nav className="nav-links" aria-label="Main">
        ${NAV.map(([t,h])=>html`<a key=${t} href=${h}>${t}</a>`)}
        <a className="btn red" style=${{color:'#fff'}} href="/#audit">Get Your Visibility Audit</a>
      </nav>
      <button className="menu-btn" aria-label="Menu" aria-expanded=${open} onClick=${()=>setOpen(!open)}>
        <svg width="20" height="14" viewBox="0 0 20 14" aria-hidden="true"><path d="M0 1h20M0 7h20M0 13h20" stroke="currentColor" strokeWidth="1.6"/></svg>
      </button>
    </div>
    <nav className=${'nav-drop'+(open?' open':'')} aria-label="Mobile">
      ${NAV.map(([t,h])=>html`<a key=${t} href=${h} onClick=${()=>setOpen(false)}>${t}</a>`)}
      <a className="btn red" href="/#audit" onClick=${()=>setOpen(false)}>Get Your Visibility Audit</a>
    </nav>
  </div></header>`;
}

/* ---------- 2. hero with live signal map ---------- */
function HeroCanvas(){
  const ref=useRef(null);
  useEffect(()=>{
    const cv=ref.current,ctx=cv.getContext('2d');let W,H,base,nodes,cx,cy,raf,visible=true,start=performance.now();
    const pinPath=new Path2D("M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z");
    function setup(){
      const b=cv.parentElement.getBoundingClientRect(),dpr=Math.min(window.devicePixelRatio||1,2);
      W=Math.max(320,b.width);H=Math.max(320,b.height);cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
      const narrow=W<=720;cx=narrow?W*.56:W*.72;cy=narrow?H-120:H*.5;
      const roads=makeRoads(W,H,7,Math.round(W/78),Math.round(H/78));
      base=document.createElement('canvas');base.width=cv.width;base.height=cv.height;const g=base.getContext('2d');g.setTransform(dpr,0,0,dpr,0,0);
      g.fillStyle='#000000';g.fillRect(0,0,W,H);
      roads.forEach(rd=>{g.beginPath();rd.pts.forEach((p,i)=>i?g.lineTo(p[0],p[1]):g.moveTo(p[0],p[1]));g.strokeStyle=rd.major?'rgba(255,255,255,.17)':'rgba(255,255,255,.065)';g.lineWidth=rd.major?1.4:1;g.stroke()});
      const r=rng(21);nodes=[];const count=narrow?20:44;let guard=0;
      while(nodes.length<count&&guard++<2000){const x=W*(narrow?.04+r()*.92:.28+r()*.7),y=H*(narrow?.42+r()*.56:.05+r()*.9),d=Math.hypot(x-cx,y-cy);if(d<60)continue;if(nodes.some(n=>Math.hypot(n.x-x,n.y-y)<58))continue;nodes.push({x,y,d})}
    }
    function draw(now){
      const t=Math.max(0,(now-start)/1000),cycle=4.2,maxR=Math.hypot(Math.max(cx,W-cx),Math.max(cy,H-cy))*.9;
      ctx.drawImage(base,0,0,W,H);
      const rings=[0,1,2].map(i=>{const age=((t+i*cycle/3)%cycle)/cycle;return{age,r:age*maxR}});
      rings.forEach(({age,r})=>{ctx.beginPath();ctx.arc(cx,cy,r,0,6.2832);ctx.strokeStyle=`rgba(226,35,25,${(1-age)*.55})`;ctx.lineWidth=1.3;ctx.stroke()});
      nodes.forEach((n,i)=>{
        let lit=REDUCED?(i%3===0?.8:0):0;
        if(!REDUCED)rings.forEach(({r})=>{const since=(r-n.d)/maxR*cycle;if(since>=0&&since<2.1)lit=Math.max(lit,1-since/2.1)});
        if(lit>.02){
          const mx=(cx+n.x)/2+(n.y-cy)*.12,my=(cy+n.y)/2-(n.x-cx)*.12;
          ctx.beginPath();ctx.moveTo(cx,cy);ctx.quadraticCurveTo(mx,my,n.x,n.y);ctx.strokeStyle=`rgba(226,35,25,${lit*.42})`;ctx.lineWidth=1;ctx.stroke();
          ctx.beginPath();ctx.arc(n.x,n.y,7+(1-lit)*10,0,6.2832);ctx.strokeStyle=`rgba(255,90,77,${lit*.5})`;ctx.stroke();
        }
        ctx.beginPath();ctx.arc(n.x,n.y,3,0,6.2832);ctx.fillStyle=lit>.02?`rgba(255,90,77,${.35+lit*.65})`:'rgba(255,255,255,.3)';ctx.fill();
      });
      const glow=ctx.createRadialGradient(cx,cy,0,cx,cy,120);glow.addColorStop(0,'rgba(226,35,25,.28)');glow.addColorStop(1,'rgba(226,35,25,0)');ctx.fillStyle=glow;ctx.fillRect(cx-120,cy-120,240,240);
      const s=1.65;ctx.save();ctx.translate(cx-12*s,cy-34*s);ctx.scale(s,s);ctx.fillStyle='#E22319';ctx.fill(pinPath);ctx.beginPath();ctx.arc(12,12,4.6,0,6.2832);ctx.fillStyle='#fff';ctx.fill();ctx.restore();
    }
    function loop(now){if(visible)draw(now);raf=requestAnimationFrame(loop)}
    setup();draw(start+2600);
    const ro=new ResizeObserver(()=>{setup();draw(performance.now())});ro.observe(cv.parentElement);
    const io=new IntersectionObserver(e=>{visible=e[0].isIntersecting});io.observe(cv);
    if(!REDUCED)raf=requestAnimationFrame(loop);
    return()=>{cancelAnimationFrame(raf);ro.disconnect();io.disconnect()};
  },[]);
  return html`<canvas ref=${ref} aria-hidden="true"></canvas>`;
}
const QUERIES=[["Google Search","apartments near downtown with a pool"],["Google Maps","med spa open near me"],["AI answer","who is the best listing agent in my area?"],["Google Maps","dermatologist accepting new patients"],["AI answer","which boutique hotel should I book this weekend?"],["Google Search","build to rent homes with a yard"]];
function Ticker(){
  const[i,setI]=useState(0);const[n,setN]=useState(REDUCED?99:0);
  useEffect(()=>{if(REDUCED)return;const q=QUERIES[i][1];if(n<q.length){const t=setTimeout(()=>setN(n+1),38);return()=>clearTimeout(t)}const t=setTimeout(()=>{setN(0);setI((i+1)%QUERIES.length)},2200);return()=>clearTimeout(t)},[i,n]);
  return html`<div className="ticker" aria-label="Sample customer searches">
    <div className="ticker-top"><span>Someone is asking</span><span>${QUERIES[i][0]}</span></div>
    <div className="ticker-q">${QUERIES[i][1].slice(0,n)}<span className="caret"></span></div>
  </div>`;
}
function StatBand(){
  return html`<div className="stat-band"><div className="wrap"><div className="stat-grid">
    <div className="stat-c"><div className="stat-l">By the numbers</div><div className="stat-s">Every report audited before it ships.</div></div>
    <div className="stat-c"><div className="stat-n"><${Doors}/>+</div><div className="stat-t">Doors and counting</div></div>
    <div className="stat-c"><div className="stat-n">500+</div><div className="stat-t">Posts published every week</div></div>
    <div className="stat-c"><div className="stat-n">10</div><div className="stat-t">Tools working for you</div></div>
  </div></div></div>`;
}
function Hero(){
  return html`<section className="hero" id="top"><${HeroCanvas}/>
    <div className="wrap hero-in">
      <${Eyebrow}>Local visibility intelligence<//>
      <h1>Your next customer is searching. <em>Will they find you?</em></h1>
      <p className="sub">LocalLift shows how your business appears across Google, Google Maps, AI search and local discovery, then strengthens it through intelligence, strategy, content and managed execution.</p>
      <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a><a className="btn ghost" href="#map">See the signal</a></div>
      <${Ticker}/>
    </div>
    <div className="sample hero-cap">Illustrative map and sample searches</div>
  </section>
  <div className="statement"><div className="wrap statement-in"><span>Be found.</span><span>Be understood.</span><span>Be chosen.</span></div></div><${StatBand}/>`;
}

/* ---------- 3. interactive reach map ---------- */
const RQ=[
 {id:"apt",label:"apartments near me",k:15,p:1.5,n:3,comps:["Sample Community A","Sample Community B","Sample Community C","Sample Community D"]},
 {id:"spa",label:"med spa near me",k:24,p:1.15,n:4,comps:["Sample Med Spa A","Sample Med Spa B","Sample Med Spa C","Sample Med Spa D"]},
 {id:"agent",label:"best real estate agent near me",k:34,p:1.0,n:6,comps:["Sample Agent A","Sample Agent B","Sample Agent C","Sample Agent D"]},
];
const MW=800,MH=560,PX=400,PY=280;
function ReachMap(){
  const[qi,setQi]=useState(0);const[sel,setSel]=useState(null);const narrow=useMedia('(max-width:720px)');
  const q=RQ[qi];
  const roads=useMemo(()=>makeRoads(MW,MH,11,12,9),[]);
  const pts=useMemo(()=>{const r=rng(5),out=[];for(let row=0;row<8;row++)for(let col=0;col<11;col++){const x=40+col*72+(row%2?36:0)+(r()-.5)*12,y=35+row*70+(r()-.5)*12;const d=Math.hypot((x-PX)/380,(y-PY)/270);out.push({x,y,d,noise:r()})}return out.filter(p=>p.d<1.02&&p.d>.1&&p.x<MW-20&&p.x>20)},[]);
  const view=narrow?{x:170,w:460}:{x:0,w:MW};
  const shown=pts.filter(p=>p.x>view.x+16&&p.x<view.x+view.w-16);
  const ranked=shown.map(p=>{const v=Math.round(1+q.k*Math.pow(p.d,q.p)+(p.noise-.5)*q.n*2);return{...p,rank:Math.max(1,v)}});
  const active=ranked.find(p=>p.x===(sel&&sel.x)&&p.y===(sel&&sel.y))||ranked.reduce((a,b)=>Math.hypot(a.x-560,a.y-190)<Math.hypot(b.x-560,b.y-190)?a:b);
  const top3=ranked.filter(p=>p.rank<=3).length,top10=ranked.filter(p=>p.rank>3&&p.rank<=10).length,missing=ranked.filter(p=>p.rank>10).length;
  const list=useMemo(()=>{const off=Math.floor(active.noise*4),c=[0,1,2,3].map(i=>q.comps[(i+off)%4]),out=[];let k=0;for(let pos=1;pos<=3;pos++){if(pos===active.rank)out.push({pos,name:"Your business",you:true});else out.push({pos,name:c[k++]})}return out},[active,q]);
  const fill=r=>r<=3?"#E22319":r<=10?"#141414":"#FFFFFF",txt=r=>r<=10?"#FFFFFF":"#595959";
  return html`<section className="band white" id="map"><div className="wrap">
    <div className="reach-head">
      <div><${Eyebrow}>Map Reach<//><h2 className="title">Your rank can change <em>every few streets.</em></h2></div>
      <p className="lede" style=${{marginTop:0}}>A search from your front door shows only one view. Tap any point to see what a customer standing there sees.</p>
    </div>
    <div className="chips" role="group" aria-label="Sample search">
      ${RQ.map((r,i)=>html`<button key=${r.id} className="chip" aria-pressed=${i===qi} onClick=${()=>{setQi(i)}}>${r.label}</button>`)}
    </div>
    <div className="reach-grid">
      <div className="reach-map">
        <svg viewBox=${view.x+' 0 '+view.w+' '+MH} role="group" aria-label="Illustrative neighborhood map with sample rank at each point">
          ${roads.map((rd,i)=>html`<path key=${i} d=${toPath(rd.pts)} fill="none" stroke=${rd.major?"#C9C9C9":"#E2E2E2"} strokeWidth=${rd.major?3.5:1.5}/>`)}
          <circle key=${'w'+qi} className="wave" cx=${PX} cy=${PY} r="460"/>
          <circle key=${'w2'+qi} className="wave" style=${{animationDelay:'.5s',opacity:0}} cx=${PX} cy=${PY} r="460"/>
          <line className="link-line" x1=${PX} y1=${PY} x2=${active.x} y2=${active.y}/>
          ${ranked.map((p,i)=>html`<g key=${p.x+'-'+p.y} className="pt" tabIndex="0" role="button" aria-label=${'Rank '+(p.rank>20?'beyond 20':p.rank)+' at this point'} onClick=${()=>setSel(p)} onKeyDown=${e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();setSel(p)}}}>
            <circle cx=${p.x} cy=${p.y} r="30" fill="transparent"/>
            <circle className="dot" cx=${p.x} cy=${p.y} r="17" style=${{transitionDelay:p.d*500+'ms'}} fill=${fill(p.rank)} stroke=${p===active||(p.x===active.x&&p.y===active.y)?"#000000":p.rank>10?"#B8B8B8":"transparent"} strokeWidth=${p.x===active.x&&p.y===active.y?2.5:1}/>
            <text x=${p.x} y=${p.y} fill=${txt(p.rank)} style=${{transitionDelay:p.d*500+'ms'}}>${p.rank>20?'20+':p.rank}</text>
          </g>`)}
          <g transform=${`translate(${PX-18} ${PY-51}) scale(1.5)`}><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319" stroke="#fff" strokeWidth="1.2"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></g>
        </svg>
      </div>
      <aside className="reach-side">
        <div className="fade" key=${active.x+'-'+qi}>
          <h3>A customer searching from this point sees</h3>
          <ul className="results" style=${{marginTop:'10px'}}>
            ${list.map(l=>html`<li key=${l.pos} className=${l.you?'you':''}><span>${l.name}</span><b>${l.pos}</b></li>`)}
            ${active.rank>3?html`<li className="you"><span>Your business</span><b>${active.rank>20?'beyond 20':active.rank}</b></li>`:null}
          </ul>
        </div>
        <div className="tally">
          <div><strong>${top3}</strong><span>points in the top 3</span></div>
          <div><strong>${top10}</strong><span>points ranked 4 to 10</span></div>
          <div><strong>${missing}</strong><span>points ranked 11 or lower</span></div>
        </div>
        <div className="legend"><span><i style=${{background:'#E22319'}}></i>Top 3</span><span><i style=${{background:'#141414'}}></i>4 to 10</span><span><i style=${{background:'#fff',border:'1px solid #B8B8B8'}}></i>11 and beyond</span></div>
        <div className="sample">Illustrative sample. Not client data.</div>
      </aside>
    </div>
  </div></section>`;
}

/* ---------- 4. the problem ---------- */
function Problem(){
  return html`<section className="band char" id="problem"><div className="wrap">
    <${Eyebrow}>The visibility problem<//>
    <h2 className="title" style=${{maxWidth:'17em'}}>The same question gets three different answers. <em>You may be missing from all of them.</em></h2>
    <p className="lede">A customer can move between Google Search, Google Maps and AI assistants before they ever call, visit or click. Each one decides who to show in its own way, so checking one tells you only part of the story.</p>
    <div className="three">
      <article className="surface">
        <div className="surface-top"><h3>Google Search</h3><span className="sample">Sample</span></div>
        <div className="q">best med spa near me</div>
        <div>
          <div className="row"><span>Sample Med Spa A</span><b>1</b></div><div className="row"><span>Sample Med Spa B</span><b>2</b></div><div className="row"><span>Regional directory</span><b>3</b></div>
          <div className="row you"><span>Your business</span><b>9</b></div>
        </div>
        <p className="verdict">Present, but far down the page.</p>
      </article>
      <article className="surface">
        <div className="surface-top"><h3>Google Maps</h3><span className="sample">Sample</span></div>
        <div className="q">med spa open now</div>
        <div>
          <div className="row"><span>Sample Med Spa B</span><b>1</b></div><div className="row"><span>Sample Med Spa C</span><b>2</b></div><div className="row"><span>Sample Med Spa A</span><b>3</b></div>
          <div className="row you"><span>Your business</span><b>not shown</b></div>
        </div>
        <p className="verdict">Close by on the map, and still not on the list people see first.</p>
      </article>
      <article className="surface">
        <div className="surface-top"><h3>AI answer</h3><span className="sample">Sample</span></div>
        <div className="q">which med spa should I try?</div>
        <p className="answer">Two options come up often in this area: <mark>Sample Med Spa B</mark>, known for its recent reviews, and <mark>Sample Med Spa C</mark>, known for its range of treatments.</p>
        <div className="row you" style=${{borderTop:'1px solid var(--on-dark-3)'}}><span>Your business</span><b>not named</b></div>
        <p className="verdict">A shortlist can form before your website gets a visit.</p>
      </article>
    </div>
    <div className="bfc">
      <div><h3>Be found.</h3><p>Show up where people look, across the whole area you serve, not only from your own address.</p></div>
      <div><h3>Be understood.</h3><p>See how Google and AI tools describe your business, your prices and your offers, and catch what is wrong.</p></div>
      <div><h3>Be chosen.</h3><p>Give people a current, credible reason to pick you over the other names on the list.</p></div>
    </div>
  </div></section>`;
}

/* ---------- 5. framework ---------- */
const STAGES=[
 {t:"Discover",h:"See yourself the way a customer does.",p:"We look at your business across Google Search, Google Maps and AI answers, and across the neighborhoods you want to reach.",tools:["AI Shortlist","Map Reach","Site Read"]},
 {t:"Compare",h:"See who gets picked instead.",p:"We track which competitors are recommended in your place and what they are doing in your market.",tools:["AI Shortlist","Market Survey"]},
 {t:"Strengthen",h:"Close the gaps for you.",p:"Our team does the work: a daily presence on Google, review responses in your voice, and content built for the people you want to reach.",tools:["Daily Presence","Review Desk"]},
 {t:"Measure",h:"Know what changed and what comes next.",p:"Every week you see what moved, in one page and one score, with one recommended next step. Monthly reports carry the longer view.",tools:["Weekly Pulse","Lift Score","Snapshot","ClearView"]},
];
function Framework({goTool}){
  const[a,setA]=useState(0);const[auto,setAuto]=useState(!REDUCED);
  useEffect(()=>{if(!auto)return;const t=setInterval(()=>setA(x=>(x+1)%4),5200);return()=>clearInterval(t)},[auto]);
  const s=STAGES[a];const C=2*Math.PI*150;
  const pos=[[50,15.5],[84.5,50],[50,84.5],[15.5,50]];
  return html`<section className="band white" id="platform"><div className="wrap">
    <${Eyebrow}>The platform<//>
    <h2 className="title">Discover. Compare. Strengthen. Measure.</h2>
    <p className="lede">One loop that keeps running, week after week, so visibility never becomes a project you finished last year.</p>
    <div className="fw">
      <div className="ring-box">
        <svg viewBox="0 0 400 400" aria-hidden="true">
          <circle cx="200" cy="200" r="150" fill="none" stroke="#E4E4E4" strokeWidth="1.5"/>
          <g className="arc" style=${{transform:`rotate(${a*90-135}deg)`}}>
            <circle cx="200" cy="200" r="150" fill="none" stroke="#E22319" strokeWidth="3" strokeDasharray=${`${C/4} ${C*3/4}`}/>
          </g>
          <g transform="translate(182 172) scale(1.5)"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></g>
        </svg>
        ${STAGES.map((st,i)=>html`<button key=${st.t} className="stage-btn" style=${{left:pos[i][0]+'%',top:pos[i][1]+'%'}} aria-pressed=${i===a} onClick=${()=>{setA(i);setAuto(false)}}>${st.t}</button>`)}
      </div>
      <div className="fw-detail fade" key=${a}>
        <div className="step">${a+1} of 4</div>
        <h3>${s.h}</h3>
        <p>${s.p}</p>
        <div className="tool-links">${s.tools.map(t=>html`<button key=${t} className="tool-link" onClick=${()=>goTool(t)}>${t}</button>`)}</div>
      </div>
    </div>
  </div></section>`;
}

/* ---------- 6. intelligence tools ---------- */
const Rows=({rows})=>html`<div>${rows.map((r,i)=>html`<div className="drow" key=${i}><span>${r[0]}</span><span>${r[1]}</span><b className=${r[3]||''}>${r[2]}</b></div>`)}</div>`;
function LiftChart(){
  const v=[52,54,55,58,60,61,64,68],W=520,H=170,L=30,R=18,T=14,B=26;
  const x=i=>L+i*(W-L-R)/(v.length-1),y=n=>T+(80-n)*(H-T-B)/(80-40);
  const d=v.map((n,i)=>(i?'L':'M')+x(i)+' '+y(n)).join('');
  return html`<svg viewBox=${`0 0 ${W} ${H}`} style=${{width:'100%',height:'auto',display:'block'}} role="img" aria-label="Sample Lift Score rising from 52 to 68 across eight weeks">
    ${[40,60,80].map(n=>html`<g key=${n}><line x1=${L} x2=${W-R} y1=${y(n)} y2=${y(n)} stroke="#2A2A2A"/><text x=${L-8} y=${y(n)+4} fontSize="11" textAnchor="end" fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">${n}</text></g>`)}
    <path d=${d+`L${x(7)} ${H-B}L${x(0)} ${H-B}Z`} fill="rgba(226,35,25,.14)"/>
    <path d=${d} fill="none" stroke="#FF5A4D" strokeWidth="2"/>
    <circle cx=${x(7)} cy=${y(68)} r="4.5" fill="#FF5A4D"/>
    <text x=${L} y=${H-6} fontSize="11" fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">Week 1</text>
    <text x=${W-R} y=${H-6} fontSize="11" textAnchor="end" fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">Week 8</text>
  </svg>`;
}
const TOOLS=[
 {n:"Weekly Pulse",c:"Fridays",d:"One page on what changed across Search, Maps and AI, plus one recommended next step.",b:()=>html`<div><${Rows} rows=${[["Search","More people found you for two local phrases","Up"],["Maps","Stronger on the east side, softer downtown","Mixed"],["AI answers","Named in one more answer this week","Up"]]}/><div className="next"><small>This week's one next step</small>Add your current offer to your Google profile before the weekend.</div></div>`},
 {n:"Lift Score",c:"Weekly",d:"A single number that shows whether you are getting easier to find.",b:()=>html`<div className="score"><div className="score-n">68</div><${LiftChart}/></div>`},
 {n:"AI Shortlist",c:"Weekly",d:"Whether AI assistants recommend you, and who they suggest instead.",b:()=>html`<${Rows} rows=${[["Who should I try near me?","Competitor A, Competitor B","Not named","flag"],["Best value nearby?","You, Competitor C","Named","good"],["Who has the best reviews?","Competitor B, Competitor A","Not named","flag"],["Who is closest to downtown?","You, Competitor A","Named","good"]]}/>`},
 {n:"Map Reach",c:"Weekly",d:"Google Maps rank across the surrounding neighborhood, not only from your own address.",b:(o={})=>html`<div><div style=${{display:'grid',gridTemplateColumns:'repeat(9,minmax(0,1fr))',gap:'4px',maxWidth:'460px'}}>${Array.from({length:45}).map((_,i)=>{const cx=(i%9)-4,cy=Math.floor(i/9)-2,d=Math.hypot(cx/4,cy/2),r=Math.max(1,Math.round(1+d*d*14+((i*7)%5)-1));return html`<div key=${i} style=${{aspectRatio:'1',display:'flex',alignItems:'center',justifyContent:'center',fontFamily:'var(--mono)',fontSize:'12px',borderRadius:'50%',background:r<=3?'#E22319':r<=10?'#2A2A2A':'transparent',border:r>10?'1px solid #2A2A2A':'0',color:r>10?'rgba(255,255,255,.72)':'#fff'}}>${r}</div>`})}</div>${o.ind?null:html`<a href="#map" style=${{display:'inline-block',marginTop:'16px',fontSize:'15px'}}>Open the full map above</a>`}</div>`},
 {n:"Site Read",c:"Weekly",d:"Checks that Google and AI tools describe your business, your pricing and your specials accurately.",b:()=>html`<${Rows} rows=${[["Hours","Website and Google profile agree","Match","good"],["Current offer","Website shows it, Google profile does not","Fix","flag"],["Pricing","AI answer quotes last season's price","Fix","flag"],["Address and phone","Consistent everywhere checked","Match","good"]]}/>`},
 {n:"Market Survey",c:"Sundays",d:"Tracks what your competitors are doing in your market.",b:()=>html`<${Rows} rows=${[["Competitor A","New offer started this week","New","flag"],["Competitor B","Prices down from last survey","Changed","flag"],["Competitor C","No change since last survey","Steady"],["Competitor D","Added a new listing photo set","Changed"]]}/>`},
 {n:"Snapshot",c:"Monthly",d:"Your monthly Google report: searches, views, calls, direction requests and website clicks.",b:()=>html`<div className="tiles">${[["1,240","Searches"],["3,180","Views"],["46","Calls"],["88","Direction requests"],["212","Website clicks"]].map(t=>html`<div className="tile" key=${t[1]}><strong>${t[0]}</strong><span>${t[1]}</span></div>`)}</div>`},
 {n:"ClearView",c:"Monthly",d:"Your monthly social media report: what posted, what performed and what changes next.",b:()=>html`<${Rows} rows=${[["What posted","24 posts across your social channels","24"],["What performed","Neighborhood reels outperformed photo posts","Reels"],["What changes","More neighborhood content next month","Next"]]}/>`},
 {n:"Review Desk",c:"Ongoing",d:"Google review responses written in your voice, with fair housing and privacy in mind.",b:()=>html`<div><div className="quote"><small>Sample review, five stars</small>The team made the whole process easy and answered every question.</div><div className="quote"><small>Sample response, in your voice</small>Thank you for sharing this. We are glad the process felt easy, and we will pass your note along to the team.</div></div>`},
 {n:"Daily Presence",c:"7 days a week",d:"Daily posts on your Google profile, written for your business and your neighborhood.",b:()=>html`<div className="week">${[["Mon","Neighborhood guide"],["Tue","Current offer"],["Wed","Team spotlight"],["Thu","Local event"],["Fri","Weekend idea"],["Sat","Customer favorite"],["Sun","Week ahead"]].map(d=>html`<div className="day" key=${d[0]}><b>${d[0]}</b><span>${d[1]}</span><i></i></div>`)}</div>`},
];
function Console({tool,setTool}){
  const T=TOOLS.find(t=>t.n===tool);
  return html`<section className="band mist" id="intelligence"><div className="wrap">
    <${Eyebrow}>LocalLift intelligence<//>
    <h2 className="title" style=${{maxWidth:'15em'}}>Ten tools. <em>One clear read</em> on your market.</h2>
    <p className="lede">We run the tools and tell you what they mean. You get the answer, not another login to manage.</p>
    <div className="console">
      <div className="console-bar"><span>LocalLift Intelligence / Sample Business</span><span>Illustrative data. Not client results.</span></div>
      <div className="console-body">
        <div className="rail" role="group" aria-label="LocalLift tools">
          ${TOOLS.map(t=>html`<button key=${t.n} aria-pressed=${t.n===tool} onClick=${()=>setTool(t.n)}><span>${t.n}</span><small>${t.c}</small></button>`)}
        </div>
        <div className="panel fade" key=${tool}>
          <div className="panel-head"><h3>${T.n}</h3><span className="sample">${T.c}</span></div>
          <p className="panel-desc">${T.d}</p>
          <div className="panel-body">${T.b()}</div>
        </div>
      </div>
    </div>
  </div></section>`;
}

/* ---------- sample charts: fake numbers, fictional places ---------- */
const smoothPath=pts=>{let d='M'+pts[0][0].toFixed(1)+' '+pts[0][1].toFixed(1);for(let i=0;i<pts.length-1;i++){const p0=pts[i-1]||pts[i],p1=pts[i],p2=pts[i+1],p3=pts[i+2]||p2;d+=`C${(p1[0]+(p2[0]-p0[0])/6).toFixed(1)} ${(p1[1]+(p2[1]-p0[1])/6).toFixed(1)} ${(p2[0]-(p3[0]-p1[0])/6).toFixed(1)} ${(p2[1]-(p3[1]-p1[1])/6).toFixed(1)} ${p2[0].toFixed(1)} ${p2[1].toFixed(1)}`}return d};
function LineChart({data,base,run,vis,name}){
  const W=680,H=250,L=34,R=16,T=14,B=28;const last=data.length-1;const[h,setH]=useState(last);const[auto,setAuto]=useState(true);
  useEffect(()=>{if(!vis||!auto||REDUCED)return;const t=setInterval(()=>setH(x=>(x+1)%data.length),1100);return()=>clearInterval(t)},[vis,auto]);
  const min=40,max=80,x=i=>L+i*(W-L-R)/last,y=n=>T+(max-n)*(H-T-B)/(max-min);
  const p=smoothPath(data.map((n,i)=>[x(i),y(n)])),q=smoothPath(base.map((n,i)=>[x(i),y(n)]));
  const tw=150,tx=x(h)+tw+14>W-R?x(h)-tw-12:x(h)+12,ty=Math.max(2,Math.min(y(data[h])-34,H-B-70));
  const pick=i=>{setAuto(false);setH(i)};
  return html`<svg viewBox=${`0 0 ${W} ${H}`} role="img" aria-label=${name+' sample trend from '+data[0]+' to '+data[last]}>
    <defs><linearGradient id="ln" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stopColor="#E22319" stopOpacity=".12"/><stop offset=".22" stopColor="#FF5A4D"/></linearGradient>
    <linearGradient id="ar" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stopColor="#E22319" stopOpacity=".3"/><stop offset="1" stopColor="#E22319" stopOpacity="0"/></linearGradient></defs>
    ${[40,60,80].map(n=>html`<g key=${n}><line x1=${L} x2=${W-R} y1=${y(n)} y2=${y(n)} style=${{stroke:'var(--line)'}}/><text x=${L-8} y=${y(n)+4} fontSize="11" textAnchor="end" style=${{fill:'var(--grey)',fontFamily:'var(--mono)'}}>${n}</text></g>`)}
    <path className=${run?'area-in':''} d=${p+`L${x(last)} ${H-B}L${x(0)} ${H-B}Z`} fill="url(#ar)"/>
    <path d=${q} fill="none" stroke="#8C8C8C" strokeWidth="1.6" strokeDasharray="3 5"/>
    <path className=${run?'draw':''} pathLength="1" d=${p} fill="none" stroke="url(#ln)" strokeWidth="2.6"/>
    <text x=${L} y=${H-8} fontSize="11" style=${{fill:'var(--grey)',fontFamily:'var(--mono)'}}>Week 1</text>
    <text x=${W-R} y=${H-8} fontSize="11" textAnchor="end" style=${{fill:'var(--grey)',fontFamily:'var(--mono)'}}>Week ${data.length}</text>
    <line x1=${x(h)} x2=${x(h)} y1=${T} y2=${H-B} stroke="#8C8C8C" opacity=".5"/>
    <circle cx=${x(h)} cy=${y(base[h])} r="3.5" fill="#8C8C8C"/>
    <circle cx=${x(h)} cy=${y(data[h])} r="5" fill="#FF5A4D" stroke="#000000" strokeWidth="2"/>
    <g transform=${`translate(${tx} ${ty})`} style=${{transition:'transform .45s ease'}}>
      <rect className="tip-bg" width=${tw} height="70" rx="3"/>
      <text x="11" y="20" fontSize="11" fill="rgba(255,255,255,.68)" fontFamily="var(--mono)">Week ${h+1}</text>
      <circle cx="15" cy="37" r="3.5" fill="#FF5A4D"/><text x="25" y="41" fontSize="12.5" fill="#fff">Lift Score</text><text x=${tw-11} y="41" fontSize="12.5" textAnchor="end" fill="#fff" fontFamily="var(--mono)">${data[h]}</text>
      <circle cx="15" cy="55" r="3.5" fill="#8C8C8C"/><text x="25" y="59" fontSize="12.5" fill="rgba(255,255,255,.78)">Market</text><text x=${tw-11} y="59" fontSize="12.5" textAnchor="end" fill="rgba(255,255,255,.78)" fontFamily="var(--mono)">${base[h]}</text>
    </g>
    ${data.map((n,i)=>html`<rect key=${i} className="bar-hit" x=${x(i)-(W-L-R)/last/2} y=${T} width=${(W-L-R)/last} height=${H-T-B} fill="transparent" onMouseEnter=${()=>pick(i)} onClick=${()=>pick(i)}/>`)}
  </svg>`;
}
function TypeLine({text,run}){
  const[n,setN]=useState(run&&!REDUCED?0:text.length);
  useEffect(()=>{if(n>=text.length)return;const t=setTimeout(()=>setN(n+1),22);return()=>clearTimeout(t)},[n,text]);
  return html`<span>${text.slice(0,n)}${n<text.length?html`<span className="caret"></span>`:null}</span>`;
}
function Bars({data,labels,run,name,accentLast=true,height=190,hi}){
  const W=680,H=height,L=8,R=8,T=26,B=24;const[h,setH]=useState(hi==null?data.length-1:hi);
  const max=Math.max(...data)*1.08,bw=(W-L-R)/data.length;
  return html`<svg viewBox=${`0 0 ${W} ${H}`} role="img" aria-label=${name+' sample values '+data.join(', ')}>
    <line x1=${L} x2=${W-R} y1=${H-B} y2=${H-B} style=${{stroke:'var(--line)'}}/>
    ${data.map((v,i)=>{const bh=(H-T-B)*v/max,on=i===h;return html`<g key=${i} className="bar-hit" onMouseEnter=${()=>setH(i)} onClick=${()=>setH(i)}>
      <rect x=${L+i*bw} y=${T} width=${bw} height=${H-T-B} fill="transparent"/>
      <rect className=${run?'grow-y':''} x=${L+i*bw+bw*.17} y=${H-B-bh} width=${bw*.66} height=${bh} style=${{fill:on?'#E22319':'var(--bar)',animationDelay:i*45+'ms'}}/>
      ${on?html`<text x=${L+i*bw+bw/2} y=${H-B-bh-8} fontSize="14" fontWeight="500" textAnchor="middle" style=${{fill:'var(--ink)',fontFamily:'var(--mono)'}}>${v}</text>`:null}
      <text x=${L+i*bw+bw/2} y=${H-7} fontSize="11" textAnchor="middle" style=${{fill:'var(--grey)',fontFamily:'var(--mono)'}}>${labels[i]}</text>
    </g>`})}
  </svg>`;
}
const SHARE=[["Google listing",38,"#E22319"],["Search",27,"#F5F5F5"],["Paid",14,"#8C8C8C"],["Social",11,"#5A5A5A"],["Referral",10,"#3A3A3A"]];
function Donut({run}){
  const[h,setH]=useState(0);let cum=0;
  return html`<div>
    <div className="donut"><svg viewBox="0 0 42 42" role="img" aria-label="Sample share of leads by source">
      ${SHARE.map((s,i)=>{const off=25-cum;cum+=s[1];return html`<circle key=${s[0]} className=${run?'seg':''} cx="21" cy="21" r="15.9155" fill="none" stroke=${s[2]} strokeWidth=${i===h?7:5.4} pathLength="100" strokeDasharray=${s[1]-.5+' '+(100-s[1]+.5)} strokeDashoffset=${off} onMouseEnter=${()=>setH(i)} onClick=${()=>setH(i)}/>`})}
    </svg><div className="donut-c"><strong>${SHARE[h][1]}%</strong><span>${SHARE[h][0]}</span></div></div>
    <div className="src-list">${SHARE.map((s,i)=>html`<button key=${s[0]} className=${'src'+(i===h?' on':'')} onMouseEnter=${()=>setH(i)} onClick=${()=>setH(i)}><i className=${'sb'+(run?' grow-x':'')} style=${{width:s[1]/38*100+'%',animationDelay:i*90+'ms'}}></i><span>${s[0]}</span><b>${s[1]}%</b></button>`)}</div>
  </div>`;
}
const COMPS=[["Your community",1685,1610,1],["Competitor A",1640,1575],["Competitor B",1720,1590],["Competitor C",1595,1595],["Competitor D",1660,1540]];
const RMIN=1500,RMAX=1800,pct=v=>(v-RMIN)/(RMAX-RMIN)*100;
const MKT=Math.round(COMPS.slice(1).reduce((a,c)=>a+c[2],0)/4);
const AIB=[["You",9,1],["Competitor A",14],["Competitor B",11],["Competitor C",6],["Competitor D",3]];
const AIQ=[["Best community near downtown?",[0,1,1,0]],["Which allows large dogs?",[1,1,0,0]],["Newest apartments in the area?",[1,0,1,0]],["Who has a move in special?",[0,1,0,1]]];
const PULSE=[46,47,49,50,52,54,55,58,60,61,64,68];const MKTLINE=[48,48,49,49,50,50,51,51,52,52,53,53];
const MONTHS=["D","J","F","M","A","M","J","J","A","S","O","N"],LEADS=[18,21,19,24,26,25,29,31,30,34,37,41];

const RTABS=[
 {t:"Weekly Pulse",pops:["Three more map points in the top 3","Named in one more AI answer","New review answered"],body:(run,vis)=>html`<div>
   <div className="rw-head"><h3>This week at a glance</h3><span className="sample">Every Friday</span></div>
   <div className="kpis">
     <div className="kpi"><strong><${Count} to=${68} run=${run}/></strong><span>Lift Score</span><em>up 4</em></div>
     <div className="kpi"><strong><${Count} to=${412} run=${run}/></strong><span>Actions on Google</span><em>up 11%</em></div>
     <div className="kpi"><strong><${Count} to=${14} run=${run}/></strong><span>Map points in the top 3</span><em>up 3</em></div>
     <div className="kpi"><strong><${Count} to=${9} run=${run}/> of 24</strong><span>AI answers that name you</span><em>up 1</em></div>
   </div>
   <div className="viz"><div className="viz-t">Lift Score against the market, last 12 weeks</div><${LineChart} data=${PULSE} base=${MKTLINE} run=${run} vis=${vis} name="Lift Score"/></div>
   <div className="rw-so"><b>This week's one next step:</b> <${TypeLine} run=${run} text="ask for five new reviews. Competitor A is pulling ahead on count."/></div>
 </div>`},
 {t:"LocalLift Lens",pops:["Google listing is your top lead source","Best month for leads this year","Search leads up for the third month"],body:(run)=>html`<div>
   <div className="rw-head"><h3>Where your business really came from</h3><span className="sample">Inside the Weekly Pulse</span></div>
   <div className="lens" style=${{marginTop:'20px'}}>
     <${Donut} run=${run}/>
     <div className="viz" style=${{marginTop:0}}><div className="viz-t">Leads, last 12 months</div><${Bars} data=${LEADS} labels=${MONTHS} run=${run} name="Leads by month"/>
       <div className="rw-so"><b>So what:</b> <${TypeLine} run=${run} text="your Google listing brought in more leads than any other source, so it gets the attention first."/></div></div>
   </div>
 </div>`},
 {t:"Market Survey",pops:["Competitor B has a new special","Competitor D is the lowest effective rent","You are above the market on one beds"],body:(run)=>html`<div>
   <div className="rw-head"><h3>One bedroom rent against your competitors</h3><span className="sample">Every Sunday</span></div>
   <div className="viz mk">
     <div className="mk-row h"><span>Community</span><span className="tk"><span className="axis"><span>$1,500</span><span>$1,600</span><span>$1,700</span><span>$1,800</span></span></span><b>Asking</b><b>Effective</b><b>Concession</b></div>
     ${COMPS.map((c,i)=>html`<div key=${c[0]} className=${'mk-row'+(c[3]?' you':'')}>
       <span>${c[0]}</span>
       <span className="trk"><span className=${'ln'+(run?' grow-x':'')} style=${{left:pct(c[2])+'%',width:(pct(c[1])-pct(c[2]))+'%',animationDelay:i*90+'ms'}}></span><span className="dot ask" style=${{left:pct(c[1])+'%'}}></span><span className="dot" style=${{left:pct(c[2])+'%'}}></span></span>
       <b>$${c[1].toLocaleString('en-US')}</b><b>$${c[2].toLocaleString('en-US')}</b><b>${((c[1]-c[2])/c[1]*100).toFixed(1)}%</b>
     </div>`)}
   </div>
   <div className="legend" style=${{marginTop:'12px'}}><span><i style=${{background:'var(--white)',border:'2px solid var(--ink)'}}></i>Asking rent</span><span><i style=${{background:'var(--ink)'}}></i>Effective rent</span></div>
   <div className="rw-so"><b>So what:</b> <${TypeLine} run=${run} text=${'your effective rent is $'+(COMPS[0][2]-MKT)+' above the $'+MKT.toLocaleString('en-US')+' competitor average on one beds.'}/></div>
 </div>`},
 {t:"AI Shortlist",pops:["Competitor A named in 14 answers","You were added to one more answer","Competitor C dropped out of two answers"],body:(run)=>html`<div>
   <div className="rw-head"><h3>Who AI recommends instead of you</h3><span className="sample">Weekly</span></div>
   <div className="viz ai-bars">
     ${AIB.map((b,i)=>html`<div key=${b[0]} className=${'ai-b'+(b[2]?' you':'')}><span>${b[0]}</span><div className="tr"><div className=${'fl'+(run?' grow-x':'')} style=${{width:b[1]/24*100+'%',animationDelay:i*90+'ms'}}></div></div><b>${b[1]} of 24</b></div>`)}
   </div>
   <div className="matrix">
     <div className="mq mh">Sample questions</div><div className="mh">You</div><div className="mh">A</div><div className="mh">B</div><div className="mh">C</div>
     ${AIQ.map((q,i)=>html`<${React.Fragment} key=${q[0]}><div className="mq">${q[0]}</div>${q[1].map((v,k)=>html`<div key=${k}><i className=${v?(k===0?'y':''):'n'} style=${{animationDelay:(i*4+k)*60+'ms'}}></i></div>`)}<//>`)}
   </div>
 </div>`},
 {t:"The Brief",pops:["Short enough to forward from a phone"],body:(run)=>html`<div>
   <div className="rw-head"><h3>What to tell your team</h3><span className="sample">Top of the Weekly Pulse</span></div>
   <div className="brief" key=${run?'p':'r'}>
     <small>Sample Community, Quillmere</small>
     <ol>
       <li>Actions on Google are up 11% this week.</li>
       <li style=${{animationDelay:'.2s'}}>Competitor B's one bed effective rent now sits $20 below yours.</li>
       <li style=${{animationDelay:'.4s'}}>AI answers named you once more than last week.</li>
       <li className="ask" style=${{animationDelay:'.6s'}}>The one ask: five new reviews this week.</li>
     </ol>
   </div>
 </div>`},
];

function useTick(ms,on){const[t,setT]=useState(0);useEffect(()=>{if(!on||REDUCED)return;const i=setInterval(()=>setT(x=>x+1),ms);return()=>clearInterval(i)},[ms,on]);return t}
const FUNNEL=[["Views on Google",1180],["Actions on Google",412],["Website visits",212],["Leads",10]];
const RACE=[["You",128,"+5",1],["Competitor A",164,"+8"],["Competitor B",97,"+2"],["Competitor C",61,"+1"]];
const MOVES=[["Competitor B started a new special","New"],["Competitor A posted on Google","Today"],["Competitor D lowered one bed rent","Down"],["Competitor C added new photos","New"],["Competitor A gained eight reviews","Up"]];
const CITIES=[["Quillmere",44],["Fernhallow",21],["Ostrabay",15],["Calderwick",11],["Brindlecrest",9]];
const ASKS=[["Which apartments near downtown allow large dogs?",["Competitor A","Your community","Competitor C"]],["Who has the best recent reviews nearby?",["Competitor B","Competitor A"]],["What is the newest community in this area?",["Your community","Competitor B"]]];
function AskTile({run,vis}){
  const t=useTick(5600,vis);const a=ASKS[t%ASKS.length];
  return html`<div key=${t}><div className="ask-q"><${TypeLine} run=${run} text=${a[0]}/></div><div className="ask-l">A few names come up:</div><div className="ask-a">${a[1].map((n,i)=>html`<span key=${n} className=${n==="Your community"?'y':''} style=${{animationDelay:(run?a[0].length*22+i*260:0)+'ms'}}>${n}</span>`)}</div></div>`;
}
function FeedTile({vis}){
  const t=useTick(2600,vis);const rows=[0,1,2,3].map(k=>MOVES[(t+k)%MOVES.length]);
  return html`<div className="feed"><div className="feed-in" key=${t}>${rows.map(r=>html`<div className="feed-r" key=${r[0]}><span>${r[0]}</span><b>${r[1]}</b></div>`)}</div></div>`;
}
function SweepTile(){
  const dots=[];for(let y=0;y<7;y++)for(let x=0;x<11;x++)dots.push(Math.hypot(x-5,(y-3)*1.2));
  return html`<div className="sweep" aria-hidden="true">${dots.map((d,i)=>html`<i key=${i} style=${{animationDelay:(d*.16).toFixed(2)+'s'}}></i>`)}<${Pin} size=${22} hole="#000000"/></div>`;
}
function Tiles(){
  const[ref,seen,vis]=useInView(.1);
  const maxR=Math.max(...RACE.map(r=>r[1]));
  return html`<div ref=${ref}>
    <h3 className="bento-h">A closer look at what we watch.</h3>
    <div className="bento">
      <div className="bt"><div className="bt-vis"><${SweepTile}/></div><h3>Signal across the map</h3><p>How far your visibility reaches, street by street.</p></div>
      <div className="bt"><div className="bt-vis"><${AskTile} run=${seen} vis=${vis}/></div><h3>What AI says</h3><p>Who gets named when customers ask.</p></div>
      <div className="bt"><div className="bt-vis"><${FeedTile} vis=${vis}/></div><h3>Competitor moves</h3><p>What changed in your market this week.</p></div>
      <div className="bt"><div className="bt-vis"><div className="fn">${FUNNEL.map((f,i)=>html`<div className="fn-r" key=${f[0]}><i className=${seen?'grow-x':''} style=${{width:f[1]/FUNNEL[0][1]*100+'%',animationDelay:i*140+'ms'}}></i><span>${f[0]}</span><b>${f[1].toLocaleString('en-US')}</b></div>`)}</div></div><h3>From view to lead</h3><p>Where people continue and drop off in a sample week.</p></div>
      <div className="bt"><div className="bt-vis"><div className="ai-bars" style=${{marginTop:0}}>${RACE.map((r,i)=>html`<div key=${r[0]} className=${'ai-b'+(r[3]?' you':'')}><span>${r[0]}</span><div className="tr"><div className=${'fl'+(seen?' grow-x':'')} style=${{width:r[1]/maxR*100+'%',animationDelay:i*110+'ms'}}></div></div><b>${r[1]} ${r[2]}</b></div>`)}</div></div><h3>The review race</h3><p>Your review count against your competitors.</p></div>
      <div className="bt"><div className="bt-vis"><div className="src-list" style=${{marginTop:0}}>${CITIES.map((c,i)=>html`<div className=${'src'+(i===0?' on':'')} key=${c[0]} style=${{cursor:'default'}}><i className=${'sb'+(seen?' grow-x':'')} style=${{width:c[1]/44*100+'%',animationDelay:i*90+'ms'}}></i><span>${c[0]}</span><b>${c[1]}%</b></div>`)}</div></div><h3>Where interest comes from</h3><p>The cities your visitors come from.</p></div>
    </div>
    <div className="sample" style=${{marginTop:'14px'}}>Sample graphics. Fake numbers and fictional cities.</div>
  </div>`;
}

const Ghost=()=>html`<div className="pghost" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><div className="fade-out" aria-hidden="true"></div>`;
const Mini=({d,c="#E22319"})=>{const W=320,H=84,min=Math.min(...d)-3,max=Math.max(...d)+3,p=smoothPath(d.map((n,i)=>[4+i*(W-8)/(d.length-1),H-4-(n-min)*(H-8)/(max-min)]));return html`<svg viewBox=${`0 0 ${W} ${H}`} aria-hidden="true"><path d=${p+`L${W-4} ${H}L4 ${H}Z`} fill="rgba(226,35,25,.1)"/><path d=${p} fill="none" stroke=${c} strokeWidth="2.4"/></svg>`};
const PEEKS=[
 {t:"Weekly Pulse",when:"Every Friday",body:()=>html`<div><div className="big">68</div><div className="small">Lift Score, up 4 this week</div><${Mini} d=${PULSE}/><div className="pr you" style=${{marginTop:'8px',gridTemplateColumns:'1fr'}}><span>This week's one next step: ask for five new reviews.</span></div></div>`},
 {t:"Market Survey",when:"Every Sunday",body:()=>html`<div><div className="small" style=${{marginTop:'14px',marginBottom:'6px'}}>One bedroom effective rent</div>${COMPS.map(c=>html`<div key=${c[0]} className=${'pr'+(c[3]?' you':'')}><span>${c[3]?'You':c[0]}</span><div className="t"><div className="f" style=${{width:(c[2]-1400)/300*100+'%'}}></div></div><b>$${c[2].toLocaleString('en-US')}</b></div>`)}<div className="pr you" style=${{marginTop:'8px',gridTemplateColumns:'1fr'}}><span>You sit $${COMPS[0][2]-MKT} above the competitor average.</span></div></div>`},
 {t:"AI Shortlist",when:"Weekly",body:()=>html`<div><div className="big">9<span style=${{fontSize:'26px',letterSpacing:'-.02em'}}> of 24</span></div><div className="small">AI answers that name you</div><div style=${{marginTop:'12px'}}>${AIB.slice(0,4).map(c=>html`<div key=${c[0]} className=${'pr'+(c[2]?' you':'')}><span>${c[0]}</span><div className="t"><div className="f" style=${{width:c[1]/24*100+'%'}}></div></div><b>${c[1]}</b></div>`)}</div></div>`},
 {t:"LocalLift Lens",when:"Every Friday",body:()=>html`<div><div className="big">38%</div><div className="small">of leads came from your Google listing</div><div style=${{marginTop:'12px'}}>${SHARE.map((c,i)=>html`<div key=${c[0]} className=${'pr'+(i===0?' you':'')}><span>${c[0]}</span><div className="t"><div className="f" style=${{width:c[1]/38*100+'%'}}></div></div><b>${c[1]}%</b></div>`)}</div></div>`},
];
const FAN=[{x:0,y:0,r:0,s:1,z:4,b:1},{x:62,y:-6,r:5,s:.95,z:3,b:.72},{x:-62,y:-2,r:-5,s:.93,z:2,b:.62},{x:112,y:6,r:10,s:.88,z:1,b:.45}];
function SneakPeek(){
  const[a,setA]=useState(0);const[auto,setAuto]=useState(!REDUCED);const[ref,seen,vis]=useInView(.2);const narrow=useMedia('(max-width:560px)');
  useEffect(()=>{if(!auto||!vis)return;const t=setInterval(()=>setA(x=>(x+1)%PEEKS.length),3400);return()=>clearInterval(t)},[auto,vis]);
  const go=i=>{setA(i);setAuto(false)};const k=narrow?.5:1;
  return html`<div className="peek-grid">
    <div>
      <${Eyebrow}>A sneak peek<//>
      <h2 className="title">Reports like no other. <em>Only the data that matters.</em></h2>
      <p className="lede">This is the look of what lands in your inbox. Every number here is made up and every place is fictional. The real reports are built for each client and audited before they ship.</p>
      <div className="peek-tabs" role="group" aria-label="Sneak peek reports">${PEEKS.map((p,i)=>html`<button key=${p.t} className="chip" aria-pressed=${i===a} onClick=${()=>go(i)}>${p.t}</button>`)}</div>
    </div>
    <div className="peek" ref=${ref}>
      ${PEEKS.map((p,i)=>{const pos=(i-a+PEEKS.length)%PEEKS.length,f=seen||REDUCED?FAN[pos]:{x:0,y:30,r:0,s:.94,z:FAN[pos].z,b:FAN[pos].b};return html`<button key=${p.t} className="paper" aria-label=${'Show the '+p.t+' sample'} onClick=${()=>go(i)} style=${{transform:`translate(${f.x*k}px,${f.y}px) rotate(${f.r*k}deg) scale(${f.s})`,zIndex:f.z,filter:`brightness(${f.b})`,transitionDelay:seen?'0ms':pos*120+'ms'}}>
        <div className="paper-wrap"><span className="paper-top"><img src=${LOGO_WHITE} alt=""/><span>${p.when}</span></span>
        <div className="paper-in"><h3>${p.t}</h3><div className="sub">Sample Community, Quillmere</div>${p.body()}</div>
        <${Ghost}/>
        <div className="paper-tag"><span>Fake numbers</span><b>Full report is private</b></div></div>
      </button>`})}
    </div>
  </div>`;
}
function Reports(){
  const[i,setI]=useState(0);const[auto,setAuto]=useState(!REDUCED);const[ref,seen,vis]=useInView(.15);
  useEffect(()=>{if(!auto||!vis)return;const t=setInterval(()=>setI(x=>(x+1)%RTABS.length),9000);return()=>clearInterval(t)},[auto,vis]);
  const T=RTABS[i];
  return html`<section className="band black" id="reports"><div className="wrap">
    <${SneakPeek}/>
    <h3 className="bento-h">Open one up.</h3>
    <div className="rw" ref=${ref} style=${{marginTop:'24px'}}>
      <div className="rw-bar"><span>Sample Community / Quillmere</span><span>Fake numbers. Fictional city. Not client data.</span></div>
      <div className="rw-tabs" role="group" aria-label="Sample reports">${RTABS.map((t,k)=>html`<button key=${t.t} aria-pressed=${k===i} onClick=${()=>{setI(k);setAuto(false)}}>${t.t}</button>`)}</div>
      <div className="rw-body">
                <div className="fade" key=${i}>
          <div className="viz" style=${{marginTop:0,minHeight:'44px'}}><${Pops} items=${T.pops} run=${vis}/></div>
          ${T.body(seen,vis)}
        </div>
      </div>
    </div>
    <${Tiles}/>
  </div></section>`;
}

/* ---------- 7. industries ---------- */
const M6=["Jun","Jul","Aug","Sep","Oct","Nov"];
const IND=[
 {t:"Multifamily",who:"A renter relocating for a new job, with two weeks to decide.",s:["Searches for apartments near downtown with a pool and a move in special.","Opens Google Maps and compares the closest communities by recent reviews.","Asks an AI assistant which newer communities near the office allow large dogs.","Books tours at the two names that appeared everywhere."],tools:["Map Reach","AI Shortlist","Market Survey","Site Read"],city:"Sample community, Quillmere",metric:"Direction requests from Google",d:[62,71,68,84,92,108],pops:["Up in the last two months","A new map point reached the top 3"],stats:[["5","sample competitors tracked"],["9 of 24","sample AI answers naming you"]],doors:true},
 {t:"Build to Rent",who:"A renter who wants a house and a yard without buying one.",s:["Searches for build to rent homes with a yard near work.","Checks Google Maps for commute, nearby parks and community photos.","Asks an AI assistant how build to rent differs from a house rental nearby.","Tours the community that explained itself clearly."],tools:["AI Shortlist","Site Read","Map Reach","Daily Presence"],city:"Sample community, Fernhallow",metric:"Website clicks from Google",d:[44,49,57,55,66,73],pops:["Named for build to rent in a new AI answer","Website clicks at a six month high"],big:["73","sample website clicks in November"],stats:[["7","sample posts a week on Google"],["2","sample site details corrected"]]},
 {t:"Medical",who:"A new patient comparing practices after a referral.",s:["Searches for the practice by name, then for a specialist near home.","Compares ratings, hours and location on Google Maps.","Asks an AI assistant who is well reviewed for that specialty nearby.","Calls the practice whose details all match and feel current."],tools:["Site Read","Review Desk","AI Shortlist","Map Reach"],city:"Sample practice, Ostrabay",metric:"Calls from Google",d:[31,34,33,41,46,52],pops:["Calls up again this month","Hours now match everywhere checked"],big:["52","sample calls from Google in November"],stats:[["4.9","sample Google rating"],["6","sample reviews answered this month"]]},
 {t:"Med Spa",who:"Someone choosing a first treatment, and reading everything first.",s:["Searches for a med spa open near work.","Scans Google Maps photos, reviews and how the owner answers them.","Asks an AI assistant which local med spa has the best reputation.","Books a consult at the name that looks established."],tools:["AI Shortlist","Review Desk","Daily Presence","Map Reach"],city:"Sample med spa, Marrowvale",metric:"Website clicks from Google",d:[58,63,74,72,88,97],pops:["Your med spa appeared in a new AI answer","A new review was answered"],big:["97","sample website clicks in November"],stats:[["5 of 12","sample AI answers naming you"],["30","sample Google posts this month"]]},
 {t:"Real Estate",who:"A homeowner getting ready to sell, looking for the right agent.",s:["Searches for the top listing agent in their neighborhood.","Reads Google reviews and looks at recent activity on each profile.","Asks an AI assistant who knows that part of town best.","Calls the agent who looks established and current."],tools:["AI Shortlist","Map Reach","Review Desk","Daily Presence"],city:"Sample agent, Calderwick",metric:"Profile views on Google",d:[120,134,129,151,168,186],pops:["Profile views keep climbing","Named for a new neighborhood"],big:["186","sample profile views in November"],stats:[["3","sample neighborhoods in the top 3"],["12","sample Google posts this month"]]},
 {t:"Hair Salons",who:"A neighbor who just moved in and needs a new salon by Saturday.",s:["Searches for a hair salon open Saturday near home.","Opens Google Maps and checks photos, hours and how owners answer reviews.","Asks an AI assistant which salon is best with curly hair nearby.","Books the salon that looked open, active and easy to trust."],tools:["Map Reach","Review Desk","Daily Presence","Snapshot"],city:"Sample salon, Wrenhollow",metric:"Direction requests from Google",d:[26,29,35,33,41,47],pops:["Saturday searches are finding you","New photos are live on Google"],big:["47","sample direction requests in November"],stats:[["4.8","sample Google rating"],["9","sample reviews answered this month"]]},
 {t:"Hospitality",who:"A traveler planning a weekend in a city they barely know.",s:["Searches for a boutique hotel near the old town with a rooftop.","Uses Google Maps to judge the walk to restaurants and sights.","Asks an AI assistant which stay fits a quiet anniversary trip.","Books the place that kept appearing, with recent photos and replies."],tools:["AI Shortlist","Review Desk","Snapshot","Daily Presence"],city:"Sample hotel, Brindlecrest",metric:"Website clicks from Google",d:[140,152,171,163,188,204],pops:["Weekend searches are up","AI answer named your rooftop"],big:["204","sample website clicks in November"],stats:[["2 of 8","sample AI answers naming you"],["14","sample reviews answered this month"]]},
 {t:"Portfolios",who:"An owner who needs one clear read on every property at once.",labels:["Portfolio view","Market","AI answers","Decision"],s:["Sees every property side by side, with the same measures on each.","Checks which properties are falling behind their local competitors.","Sees which properties AI assistants name, and which they skip.","Puts attention where one recommended move will count most."],tools:["Lift Score","Weekly Pulse","Market Survey","AI Shortlist"],city:"Sample portfolio, six properties",metric:"Lift Score by property",d:[58,74,63,81,49,68],labels2:["P1","P2","P3","P4","P5","P6"],pops:["Property 4 leads the portfolio","Property 5 needs attention first"],big:["66","sample portfolio average Lift Score"],stats:[["6","sample properties compared"],["1","recommended move per property"]]},
];
const JLABEL=["Search","Google Maps","AI answer","Decision"];
function Industries(){
  const[i,setI]=useState(0);const d=IND[i];const[ref,seen,vis]=useInView(.15);const labels=d.labels||JLABEL;
  return html`<section className="band white" id="industries"><div className="wrap">
    <${Eyebrow}>Industries<//>
    <h2 className="title">Every customer takes a different path to <em>the same decision.</em></h2>
    <div className="tabs" role="group" aria-label="Choose an industry">
      ${IND.map((x,k)=>html`<button key=${x.t} className="chip" aria-pressed=${k===i} onClick=${()=>setI(k)}>${x.t}</button>`)}
    </div>
    <div className="fade" key=${i} ref=${ref}>
      <p className="journey-who">${d.who}</p>
      <div className="journey">
        <div className="track"><span className="traveler"></span></div>
        ${d.s.map((t,k)=>html`<div className="j-step" key=${k}><h3>${labels[k]}</h3><p>${t}</p></div>`)}
      </div>
      <div className="ia">
        <div>
          ${d.doors?html`<div className="ia-city">Multifamily doors we work across</div><div className="ia-big"><i className="live-dot"></i><span><${Doors}/>+</span></div><div className="ia-sub">doors and counting</div>`
            :html`<div className="ia-big"><${Count} to=${+d.big[0]} run=${seen}/></div><div className="ia-sub">${d.big[1]}</div>`}
          ${d.doors?html`<div className="ia-city" style=${{margin:'20px 0 -6px'}}>Sample figures</div>`:null}<div className="ia-stats">${d.stats.map(s=>html`<div key=${s[1]}><strong>${s[0]}</strong><span>${s[1]}</span></div>`)}</div>
        </div>
        <div>
          <div className="ia-city">${d.city}. Fake numbers.</div>
          <div className="viz" style=${{marginTop:0}}>
            <${Pops} items=${d.pops} run=${vis}/>
            <div className="viz-t">${d.metric}</div>
            <${Bars} data=${d.d} labels=${d.labels2||M6} run=${seen} name=${d.metric} height=${210}/>
          </div>
        </div>
      </div>
      <div className="j-tools"><b>Where LocalLift works this journey:</b><span>${d.tools.join(', ')}</span><a className="j-more" href=${indHref(d)}>See LocalLift for ${d.t}</a></div>
      <div className="sample" style=${{marginTop:'14px'}}>Sample journey, sample place and sample charts. Illustrative only.</div>
    </div>
  </div></section>`;
}

/* ---------- 8. managed service ---------- */
function Managed(){
  const days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"];
  const dot=on=>on?html`<i></i>`:null;const[pref,seen]=useInView(.3);
  return html`<section className="band char" id="managed"><div className="wrap">
    <${Eyebrow}>Fully managed<//>
    <h2 className="title" style=${{maxWidth:'15em'}}>We are not selling another <em>complicated dashboard.</em></h2>
    <p className="lede">We provide the intelligence and we help you act on it. Your team stays focused on customers, and the visibility work keeps moving every day.</p>
    <div className="m-grid">
      <ul className="not-list">
        <li>One team across Google, Maps, AI answers and content.</li>
        <li>Written reports you can read in minutes and forward to ownership.</li>
        <li>One recommended next step each week, in plain language.</li>
        <li>No new platform for your team to log in to or learn.</li>
      </ul>
      <div>
        <div className="sched-wrap"><div className="sched" role="table" aria-label="A typical LocalLift week">
          <div className="h"></div>${days.map(d=>html`<div className="h" key=${d}>${d}</div>`)}
          <div className="n">Daily Presence</div>${days.map(d=>html`<div className="c" key=${d}>${dot(true)}</div>`)}
          <div className="n">Review Desk</div><div className="span">Ongoing</div>
          <div className="n">Weekly reads</div><div className="span">Lift Score, AI Shortlist, Map Reach, Site Read</div>
          <div className="n">Weekly Pulse</div>${days.map(d=>html`<div className="c" key=${d}>${dot(d==="Fri")}</div>`)}
          <div className="n">Market Survey</div>${days.map(d=>html`<div className="c" key=${d}>${dot(d==="Sun")}</div>`)}
        </div></div>
        <p className="sched-note">Snapshot and ClearView arrive monthly.</p>
      </div>
    </div>
  </div></section>`;
}

/* ---------- results and insights, linked to the live site ---------- */
function Results(){
  return html`<section className="band mist" id="results"><div className="wrap">
    <${Eyebrow}>Results and insights<//>
    <h2 className="title" id="insights">See the work and <em>the thinking behind it.</em></h2>
    <div className="cards">
      <a className="card" href="https://www.thesocialdm.com/blog/montage-tigard-case-study" target="_blank" rel="noopener"><span className="sample">Case study</span><h3>Montage, Tigard, Oregon</h3><p>33 reviews at 4.8. The gap was the count, not the rating.</p><em>Read the case study</em></a>
      <a className="card" href="https://www.thesocialdm.com/2026-multifamily-visibility-report" target="_blank" rel="noopener"><span className="sample">Research</span><h3>2026 Multifamily Visibility Report</h3><p>Published by The SocialDM, powered by LocalLift.</p><em>Read the report</em></a>
      <a className="card" href="https://www.thesocialdm.com/blog" target="_blank" rel="noopener"><span className="sample">Insights</span><h3>Market Intelligence</h3><p>Ongoing writing on Google, Maps, AI search and local visibility.</p><em>Read the latest</em></a>
    </div>
  </div></section>`;
}

/* ---------- 9. audit ---------- */
function Audit({industry="Multifamily"}){
  return html`<section className="band black audit" id="audit">
    <div className="audit-rings" aria-hidden="true"><span></span><span></span><span></span></div>
    <div className="wrap audit-grid">
      <div>
        <${Eyebrow}>Visibility audit<//>
        <h2 className="title">See where you show up, and <em>where you don't.</em></h2>
        <p className="lede">We check Google Search, Google Maps and AI answers for your business and send a clear plan to close the gaps.</p>
      </div>
      <form className="form" aria-describedby="audit-note" onSubmit=${e=>e.preventDefault()} noValidate>
        <p className="form-flag" id="audit-note" role="note"><b>This form does not send yet.</b> It is switched off in this preview and collects nothing. Nothing you see here is saved, stored or sent.</p>
        <fieldset disabled style=${{border:0,margin:0,padding:0,display:'flex',flexDirection:'column',gap:'14px'}}>
          <label htmlFor="biz">Business name<input id="biz" placeholder="Your business" autoComplete="off"/></label>
          <label htmlFor="city">City<input id="city" placeholder="Your city" autoComplete="off"/></label>
          <label htmlFor="ind">Industry<select id="ind" defaultValue=${industry}>${IND.map(x=>html`<option key=${x.t}>${x.t}</option>`)}</select></label>
          <label htmlFor="mail">Work email<input id="mail" type="text" placeholder="you@company.com" autoComplete="off"/></label>
          <button className="btn red" type="button">Get Your Visibility Audit</button>
        </fieldset>
        <p className="form-note">Want an audit now? <a href="https://www.thesocialdm.com/contact" target="_blank" rel="noopener">Contact The SocialDM</a>.</p>
      </form>
    </div>
  </section>`;
}

/* ---------- 10. footer ---------- */
function Giant(){
  const box=useRef(null),inner=useRef(null);
  useEffect(()=>{const fit=()=>{if(!box.current||!inner.current)return;inner.current.style.fontSize='100px';const w=inner.current.getBoundingClientRect().width;inner.current.style.fontSize=(100*box.current.clientWidth/w*.995)+'px'};fit();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);const ro=new ResizeObserver(fit);ro.observe(box.current);return()=>ro.disconnect()},[]);
  return html`<div className="giant" ref=${box} aria-hidden="true"><span className="giant-in" ref=${inner}>L<span className="giant-pin"><span className="gr"></span><span className="gr b"></span><svg viewBox="0 0 24 34" preserveAspectRatio="xMidYMid meet"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319"/><circle cx="12" cy="12" r="4.6" fill="#000"/></svg></span>calLift<sup>™</sup></span></div>`;
}
function Footer(){
  return html`<footer className="foot"><div className="wrap">
    <div className="foot-grid">
      <div>
        <${Logo} h=${36}/>
        <div><a className="by" href="https://www.thesocialdm.com/" target="_blank" rel="noopener"><img src=${SDM_LOGO} alt=""/><span>Developed by The SocialDM.<br/>Visit thesocialdm.com</span></a></div>
      </div>
      <div><h3>LocalLift</h3><ul><li><a href="/#platform">Platform</a></li><li><a href="/#intelligence">Intelligence</a></li><li><a href="/#managed">Fully managed</a></li><li><a href="/#audit">Visibility audit</a></li></ul></div>
      <div><h3>Industries</h3><ul>${IND.map(x=>html`<li key=${x.t}><a href=${indHref(x)}>${x.t}</a></li>`)}</ul></div>
      <div><h3>The SocialDM</h3><ul><li><a href="https://www.thesocialdm.com/about" target="_blank" rel="noopener">About</a></li><li><a href="https://www.thesocialdm.com/blog" target="_blank" rel="noopener">Market Intelligence</a></li><li><a href="https://www.thesocialdm.com/research-insights" target="_blank" rel="noopener">Research and Insights</a></li><li><a href="https://www.thesocialdm.com/contact" target="_blank" rel="noopener">Contact</a></li></ul></div>
    </div>
    <${Giant}/>
    <div className="foot-base"><span>LocalLift™ by The SocialDM™. Phoenix, Arizona.</span><span>Private preview. All maps, scores and sample businesses are illustrative.</span></div>
  </div></footer>`;
}

function App(){
  const[tool,setTool]=useState("Weekly Pulse");
  const goTool=t=>{setTool(t);const el=document.getElementById('intelligence');if(el)el.scrollIntoView({behavior:REDUCED?'auto':'smooth'})};
  return html`<div><${Nav}/><main id="main"><${Hero}/><${ReachMap}/><${Problem}/><${Framework} goTool=${goTool}/><${Console} tool=${tool} setTool=${setTool}/><${Reports}/><${Industries}/><${Managed}/><${Results}/><${Faq} items=${FAQS.Home}/><${Audit}/></main><${Footer}/></div>`;
}

/* ---------- industry pages ---------- */
const IND_SLUG={"Multifamily":"multifamily","Build to Rent":"build-to-rent","Medical":"medical","Med Spa":"med-spa","Real Estate":"real-estate","Hair Salons":"hair-salons","Hospitality":"hospitality","Portfolios":"portfolios"};
function indHref(x){return '/industries/'+IND_SLUG[x.t]+'/'}

const IND_COPY={
 "Multifamily":{
  plural:"apartment communities",sample:"Sample community",
  h1:["Renters decide who to tour ","before they call."],
  sub:"LocalLift shows how your communities appear when renters search Google, scan Google Maps and ask AI assistants, then keeps every property visible, accurate and chosen through lease up and beyond.",
  card:"Communities, lease ups and stabilized assets.",
  pains:[["Specials go stale online.","A concession ends on your website but lives on in your Google profile and in AI answers. Renters arrive expecting a price you no longer offer."],
   ["Rank depends on the street.","A community can lead the map from its leasing office and vanish a mile away, right where your next renter works."],
   ["AI builds the shortlist.","Renters ask AI assistants which communities allow large dogs or sit near the office. If you are not named, you are not toured."]],
  does:[["Market Survey","Every Sunday, competitor asking rents, effective rents and specials, side by side with yours."],
   ["Map Reach","Weekly Google Maps rank across the neighborhoods your renters come from, not only from the leasing office."],
   ["AI Shortlist","The renter questions that matter, asked every week, with the communities AI names instead of you."],
   ["Site Read","Checks that your pricing, specials and pet policy read the same on your website, your Google profile and in AI answers."],
   ["Review Desk","Resident review responses in your voice, written with fair housing in mind."],
   ["Daily Presence","A Google post every day about your community, your neighborhood and what is happening this week."]]},
 "Build to Rent":{
  plural:"build to rent communities",sample:"Sample build to rent community",
  h1:["Renters want the yard. ","Help them find yours."],
  sub:"Build to rent is still new to many searchers. LocalLift helps Google and AI assistants explain your community clearly, so renters who want a house without buying one find you.",
  card:"Single family rental communities, from first phase to fully leased.",
  pains:[["The category needs explaining.","Many renters do not search for build to rent by name. They search for homes for rent with a yard, and your community has to show up for that."],
   ["AI answers fill the gap.","When someone asks how build to rent differs from renting a house, the answer shapes who they tour. You want to be the example."],
   ["Lease up moves fast.","New phases, new pricing and new amenities change often. Every listing has to keep up, or renters see last month's story."]],
  does:[["AI Shortlist","Weekly checks on whether AI assistants name your community for the questions renters actually ask."],
   ["Site Read","Makes sure phases, pricing and amenities read the same on your website, your Google profile and in AI answers."],
   ["Map Reach","Google Maps rank across the neighborhoods and commute routes renters care about."],
   ["Daily Presence","Daily Google posts that explain the community, the homes and the neighborhood in plain language."],
   ["Market Survey","What nearby rentals and other communities are offering, every Sunday."],
   ["Weekly Pulse","One page every Friday on what moved and the one next step for your lease up."]]},
 "Medical":{
  plural:"medical practices",sample:"Sample practice",
  h1:["Patients check you ","before they call."],
  sub:"After a referral, many patients search the practice, compare ratings and ask AI who is well reviewed nearby. LocalLift keeps your hours, locations and reputation accurate everywhere they look.",
  card:"Practices, specialists and groups with several locations.",
  pains:[["Details drift across listings.","Old hours, a moved suite or a retired provider can linger on Google and in AI answers, and patients call the wrong place."],
   ["Reviews carry the decision.","Patients read how a practice answers reviews. Silence reads as neglect, and a careless reply can expose private details."],
   ["Specialists compete street by street.","A patient searching from home sees a different list than one searching from the hospital campus."]],
  does:[["Site Read","Checks that hours, locations, providers and services match across your website, your Google profile and AI answers."],
   ["Review Desk","Review responses in your voice that never confirm someone is a patient and never discuss care."],
   ["AI Shortlist","Whether AI assistants name your practice when patients ask who is well reviewed for your specialty nearby."],
   ["Map Reach","Google Maps rank across the neighborhoods your patients drive from."],
   ["Snapshot","Your monthly Google report: searches, views, calls and direction requests."],
   ["Weekly Pulse","One page every Friday, short enough to share with the practice manager."]]},
 "Med Spa":{
  plural:"med spas",sample:"Sample med spa",
  h1:["First time clients read everything. ","Make it worth reading."],
  sub:"Someone choosing a first treatment studies photos, reviews and every answer an AI assistant gives. LocalLift keeps your med spa visible, current and trusted across all of it.",
  card:"Med spas, aesthetics studios and wellness clinics.",
  pains:[["Reputation is the product.","Clients choose the med spa that looks established. Thin photos and unanswered reviews send them to the name that looks busier."],
   ["Offers change monthly.","Seasonal pricing and new treatments need to read the same on your website, your Google profile and in AI answers."],
   ["Near work matters.","Many clients book close to the office, not home. Your map rank needs to hold where they spend the day."]],
  does:[["AI Shortlist","Whether AI assistants name your med spa when people ask who has the best reputation nearby."],
   ["Review Desk","Thoughtful review responses in your voice, written with client privacy in mind."],
   ["Daily Presence","Daily Google posts on treatments, aftercare tips, your team and this month's offer."],
   ["Map Reach","Google Maps rank across the office districts and neighborhoods your clients come from."],
   ["Site Read","Checks that treatments, pricing and offers match everywhere a client looks."],
   ["Snapshot","Your monthly Google report: searches, views, calls and website clicks."]]},
 "Real Estate":{
  plural:"real estate agents",sample:"Sample agent",
  h1:["Sellers pick the agent ","who looks current."],
  sub:"Before a homeowner calls, they search your name, read your reviews and ask AI who knows their part of town. LocalLift helps make sure the answer includes you.",
  card:"Agents, teams and brokerages.",
  pains:[["Activity signals expertise.","A Google profile with no recent posts looks retired, even when your calendar is full."],
   ["Neighborhoods are the battleground.","Sellers want the agent who knows their streets. Your visibility has to hold neighborhood by neighborhood."],
   ["AI names a few agents.","When a homeowner asks who the best listing agent nearby is, a short list forms in seconds."]],
  does:[["AI Shortlist","Whether AI assistants name you when homeowners ask who knows their neighborhood best."],
   ["Map Reach","Google Maps rank across every neighborhood you want listings from."],
   ["Review Desk","Client review responses in your voice, so every reply adds to your reputation."],
   ["Daily Presence","Daily Google posts on listings, sales, market notes and the neighborhoods you serve."],
   ["Snapshot","Your monthly Google report: profile views, calls and website clicks."],
   ["Weekly Pulse","One page every Friday on what moved and the one next step."]]},
 "Hair Salons":{
  plural:"hair salons",sample:"Sample salon",
  h1:["New neighbors need a salon ","by Saturday."],
  sub:"People new to the area search, scan photos and check hours on their phone, then book the salon that looks open and active. LocalLift keeps your salon in that first look.",
  card:"Salons, barbers and independent stylists.",
  pains:[["Hours decide the booking.","If Saturday hours are wrong anywhere, a ready client books somewhere else."],
   ["Photos do the selling.","Searchers judge the work before they read a word. Fresh photos and recent posts show the chairs are full."],
   ["Specialties get asked about.","People ask AI assistants which salon is best with curly hair or color correction nearby. You want to be named for what you do best."]],
  does:[["Map Reach","Google Maps rank across the neighborhoods around your salon, street by street."],
   ["Review Desk","Review responses in your voice, so happy clients feel thanked and new ones see you care."],
   ["Daily Presence","Daily Google posts on cuts, color, your stylists and open appointments."],
   ["Snapshot","Your monthly Google report: searches, calls and direction requests."],
   ["AI Shortlist","Whether AI assistants name your salon for the specialties you are known for."],
   ["Site Read","Checks that hours, services and prices match everywhere."]]},
 "Hospitality":{
  plural:"hotels and stays",sample:"Sample hotel",
  h1:["Travelers plan the trip ","in an AI answer."],
  sub:"Guests ask which stay fits a quiet weekend, check the walk to dinner on Google Maps, then book the place that kept appearing. LocalLift works to keep your property in that answer.",
  card:"Boutique hotels, inns and short stay properties.",
  pains:[["Booking sites own the first click.","Your own Google profile and website need to give travelers a reason to book with you directly."],
   ["Every trip has a reason.","Anniversaries, conferences, game weekends. AI answers match stays to reasons, and you want to match more of them."],
   ["Recent beats beautiful.","Travelers trust recent photos and recent replies over polished pictures from three years ago."]],
  does:[["AI Shortlist","Whether AI assistants recommend your property for the trips travelers describe."],
   ["Review Desk","Guest review responses in your voice, posted while the stay is still fresh."],
   ["Snapshot","Your monthly Google report: searches, views, calls and website clicks."],
   ["Daily Presence","Daily Google posts on rooms, dining, events and what is happening nearby."],
   ["Map Reach","Google Maps rank from the places guests start their search: the station, the stadium, the old town."],
   ["Site Read","Checks that amenities, policies and rates read the same everywhere."]]},
 "Portfolios":{
  plural:"portfolios",sample:"Sample portfolio",
  h1:["One clear read ","on every property."],
  sub:"Owners and operators see every property side by side, on the same measures, with one recommended move for each. LocalLift turns a stack of reports into one decision.",
  card:"Owners, operators and asset managers.",
  pains:[["Every site reports differently.","Different vendors and different measures make properties hard to compare, and the weakest one hides."],
   ["Problems surface late.","A property can slip behind its local competitors for weeks before occupancy or leads show it."],
   ["Attention is limited.","You cannot fix everything at once. You need to know which move counts most this week."]],
  does:[["Lift Score","The same score on every property, so you can see which are getting easier to find and which are slipping."],
   ["Weekly Pulse","One page per property every Friday, with one recommended next step for each."],
   ["Market Survey","Competitor pricing and specials around every property, every Sunday."],
   ["AI Shortlist","Which properties AI assistants name, and which they skip."],
   ["Snapshot","Monthly Google results for every property, in one consistent format."],
   ["ClearView","Monthly social results across the portfolio: what posted, what performed, what changes next."]]},
};

function IndJourney({d}){
  const[ref,seen,vis]=useInView(.15);const labels=d.labels||JLABEL;
  return html`<div ref=${ref}>
      <p className="journey-who">${d.who}</p>
      <div className="journey">
        <div className="track"><span className="traveler"></span></div>
        ${d.s.map((t,k)=>html`<div className="j-step" key=${k}><h3>${labels[k]}</h3><p>${t}</p></div>`)}
      </div>
      <div className="ia">
        <div>
          ${d.doors?html`<div className="ia-city">Multifamily doors we work across</div><div className="ia-big"><i className="live-dot"></i><span><${Doors}/>+</span></div><div className="ia-sub">doors and counting</div>`
            :html`<div className="ia-big"><${Count} to=${+d.big[0]} run=${seen}/></div><div className="ia-sub">${d.big[1]}</div>`}
          ${d.doors?html`<div className="ia-city" style=${{margin:'20px 0 -6px'}}>Sample figures</div>`:null}<div className="ia-stats">${d.stats.map(s=>html`<div key=${s[1]}><strong>${s[0]}</strong><span>${s[1]}</span></div>`)}</div>
        </div>
        <div>
          <div className="ia-city">${d.city}. Fake numbers.</div>
          <div className="viz" style=${{marginTop:0}}>
            <${Pops} items=${d.pops} run=${vis}/>
            <div className="viz-t">${d.metric}</div>
            <${Bars} data=${d.d} labels=${d.labels2||M6} run=${seen} name=${d.metric} height=${210} hi=${d.labels2?d.d.indexOf(Math.max(...d.d)):null}/>
          </div>
        </div>
      </div>
      <div className="sample" style=${{marginTop:'14px'}}>Sample journey, sample place and sample charts. Illustrative only.</div>
  </div>`;
}

function IndTools({d,c}){
  const names=c.does.map(x=>x[0]);const[tool,setTool]=useState(names[0]);
  const T=TOOLS.find(t=>t.n===tool);const mine=c.does.find(x=>x[0]===tool);
  return html`<div className="console" style=${{marginTop:'40px'}}>
      <div className="console-bar"><span>LocalLift Intelligence / ${c.sample}</span><span>Illustrative panels. A separate sample from the chart above.</span></div>
      <div className="console-body">
        <div className="rail" role="group" aria-label="LocalLift tools">
          ${names.map(n=>{const t=TOOLS.find(x=>x.n===n);return html`<button key=${n} aria-pressed=${n===tool} onClick=${()=>setTool(n)}><span>${n}</span><small>${t.c}</small></button>`})}
        </div>
        <div className="panel fade" key=${tool}>
          <div className="panel-head"><h3>${T.n}</h3><span className="sample">${T.c}</span></div>
          <p className="panel-desc">${mine[1]}</p>
          <div className="panel-body">${T.b({ind:true})}</div>
        </div>
      </div>
    </div>`;
}

function Faq({items,dark}){
  if(!items||!items.length)return null;
  return html`<section className=${'band '+(dark?'char':'white')} id="faq"><div className="wrap faq-wrap">
    <div><${Eyebrow}>Questions<//><h2 className="title">Answers, <em>before you ask.</em></h2></div>
    <div className="faq">${items.map((f,i)=>html`<details key=${i} open=${i===0}><summary>${f[0]}</summary><p>${f[1]}</p></details>`)}</div>
  </div></section>`;
}

function IndustryPage({name}){
  const d=IND.find(x=>x.t===name),c=IND_COPY[name];
  return html`<div><${Nav}/><main id="main">
    <section className="hero ind-hero"><${HeroCanvas}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span aria-current="page">${name}</span></nav>
        <h1>${c.h1[0]}<em>${c.h1[1]}</em></h1>
        <p className="sub">${c.sub}</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a><a className="btn ghost" href="#journey">See the journey</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <div className="statement"><div className="wrap statement-in"><span>Be found.</span><span>Be understood.</span><span>Be chosen.</span>${d.doors?html`<${DoorsStat}/>`:null}</div></div>
    <section className="band char"><div className="wrap">
      <${Eyebrow}>The visibility problem for ${c.plural}<//>
      <h2 className="title" style=${{maxWidth:'16em'}}>Where the customer slips away, <em>and why.</em></h2>
      <div className="pains">${c.pains.map((p,i)=>html`<article className="pain" key=${i}><b>0${i+1}</b><h3>${p[0]}</h3><p>${p[1]}</p></article>`)}</div>
    </div></section>
    <section className="band white" id="journey"><div className="wrap">
      <${Eyebrow}>The customer journey<//>
      <h2 className="title" style=${{maxWidth:'15em'}}>Four moments decide <em>who gets chosen.</em></h2>
      <${IndJourney} d=${d}/>
    </div></section>
    <section className="band mist" id="intelligence"><div className="wrap">
      <${Eyebrow}>What LocalLift does for ${c.plural}<//>
      <h2 className="title" style=${{maxWidth:'15em'}}>The tools that matter here, <em>run for you.</em></h2>
      <p className="lede">We run the tools and tell you what they mean. You get the answer and one next step, not another login.</p>
      <div className="does">${c.does.map(x=>{const t=TOOLS.find(y=>y.n===x[0]);return html`<div className="do" key=${x[0]}><small>${t.c}</small><h3>${x[0]}</h3><p>${x[1]}</p></div>`})}</div>
      <${IndTools} d=${d} c=${c}/>
    </div></section>
    <${Faq} items=${FAQS[name]}/>
    <section className="band white" style=${{paddingTop:0}}><div className="wrap">
      <${Eyebrow}>Other industries<//>
      <div className="others">${IND.filter(x=>x.t!==name).map(x=>html`<a key=${x.t} href=${indHref(x)}>${x.t}</a>`)}</div>
    </div></section>
    <${Audit} industry=${name}/>
  </main><${Footer}/></div>`;
}

function IndustriesIndex(){
  return html`<div><${Nav}/><main id="main">
    <section className="hero ind-hero"><${HeroCanvas}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><span aria-current="page">Industries</span></nav>
        <h1>Built for businesses people <em>search for nearby.</em></h1>
        <p className="sub">Every customer takes a different path to the same decision. LocalLift follows that path across Google Search, Google Maps and AI answers for eight kinds of local business.</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <section className="band white"><div className="wrap">
      <${Eyebrow}>Choose your industry<//>
      <h2 className="title">Eight industries. <em>One loop.</em></h2>
      <div className="ind-cards">${IND.map(x=>html`<a className="card" key=${x.t} href=${indHref(x)}><span className="sample">Industry</span><h3>${x.t}</h3><p>${IND_COPY[x.t].card}</p><em>See LocalLift for ${x.t}</em></a>`)}</div>
    </div></section>
    <${Industries}/>
    <${Faq} items=${FAQS.Industries} dark=${true}/>
    <${Audit}/>
  </main><${Footer}/></div>`;
}

/* ---------- page registry ---------- */
const FAQS={
 Home:[
  ["What is LocalLift?","LocalLift is a local visibility service from The SocialDM. We show how your business appears across Google Search, Google Maps and AI answers, then do the work to strengthen it: daily Google posts, review responses, content and weekly reporting."],
  ["How do you know what AI assistants say about my business?","Every week we ask the leading AI assistants the questions your customers ask, and record who gets named. You see where you appear, where you do not, and who is named instead."],
  ["Do I need to learn a new platform?","No. There is no dashboard to log in to. Our team runs the tools and sends written reports you can read in minutes and forward to ownership."],
  ["What do I receive each week?","A Weekly Pulse every Friday with one recommended next step, plus weekly reads on your map rank, AI answers and listing accuracy. Snapshot and ClearView reports arrive monthly."],
  ["Does LocalLift replace my website or my ads?","No. LocalLift works alongside them. It strengthens how you appear in organic search, on Google Maps and in AI answers, where many local decisions start."],
  ["Are the numbers on this site real?","The door count, the weekly post count and the case study are real. Every number, chart, business and city in the samples is made up to show what our reports look like."],
  ["How do I get started?","Request a Visibility Audit. The audit form on this preview does not send yet, so contact The SocialDM directly in the meantime."]],
 Industries:[
  ["Which industries does LocalLift work with?","Multifamily, build to rent, medical practices, med spas, real estate agents, hair salons, hospitality and portfolios of many properties."],
  ["Is the service different for each industry?","The loop is the same: discover, compare, strengthen and measure. The questions we track, the competitors we watch and the content we write change for each industry."],
  ["My industry is not listed. Can you still help?","If customers search for you nearby, the same approach applies. Contact The SocialDM and we will tell you honestly whether LocalLift fits."],
  ["Do you work with groups and multi location businesses?","Yes. Portfolio reporting puts every location side by side on the same measures, with one recommended move for each."]],
 "Multifamily":[
  ["How does LocalLift help apartment communities?","We track how renters find your community on Google Search, Google Maps and AI answers, fix what is wrong or out of date, and keep your Google presence active every day. Every Friday you get one page on what moved and one next step."],
  ["Do you track competitor rents and specials?","Yes. Market Survey compares asking rents, effective rents and specials at your competitors every Sunday, side by side with yours."],
  ["Are review responses written with fair housing in mind?","Yes. Every response is written in your voice, stays neutral and never references a protected characteristic or a resident's personal details."],
  ["Do you work with lease ups as well as stabilized communities?","Yes. Lease ups need visibility fast and change often. Stabilized communities need to hold their place against newer competitors. The weekly loop covers both."],
  ["How large is your multifamily portfolio?","LocalLift works across more than 7,900 doors, and counting."]],
 "Build to Rent":[
  ["What makes build to rent visibility different?","Many renters do not yet search for build to rent by name. Your community has to appear for the searches they do make, like homes for rent with a yard, and be explained clearly when they ask AI assistants."],
  ["Do you support communities still in lease up?","Yes. We keep phases, pricing and amenities current across your website, your Google profile and AI answers as they change."],
  ["Can you control what AI assistants say about us?","No one can control AI answers directly. We track what they say every week, correct the sources they draw on, and publish clear content so the answers improve over time."],
  ["Do you track nearby rentals and other communities?","Yes. Market Survey watches nearby offers every Sunday so you know what renters are comparing you with."]],
 "Medical":[
  ["Is your review response process safe for patient privacy?","Yes. Responses never confirm that someone is a patient and never discuss care. We do not need access to patient records."],
  ["Can you fix wrong hours, addresses or provider details?","Yes. Site Read checks your details across your website, your Google profile and AI answers every week, and we correct what is out of date."],
  ["Do you work with practices that have several locations?","Yes. Each location is tracked on its own, and portfolio reporting shows every location side by side."],
  ["Will this replace our website or patient marketing?","No. LocalLift works alongside them and focuses on how patients find and judge your practice before they call."]],
 "Med Spa":[
  ["How do you help a med spa get recommended by AI assistants?","We track the questions clients ask every week, see which med spas are named, and strengthen the reviews, posts and details AI answers draw on."],
  ["Can you promote our monthly offers?","Yes. Daily Presence posts feature current offers and treatments, and Site Read checks that the offer reads the same everywhere."],
  ["Do your posts make claims about treatment results?","No. Posts and review replies stay factual, avoid promising outcomes and respect client privacy."],
  ["How soon will we see changes?","Some fixes, like correct hours or a current offer, show within days. Map rank and AI answers move over weeks, which is why we report every week."]],
 "Real Estate":[
  ["Do you work with individual agents or teams?","Both. LocalLift works for a single agent, a team or a brokerage with many profiles."],
  ["Can you help me show up in specific neighborhoods?","Yes. Map Reach measures your Google Maps rank across the neighborhoods you choose, and your posts and content are written for those same areas."],
  ["Do I need to write the posts myself?","No. We write and publish daily Google posts on your listings, sales and market notes. You can review them whenever you like."],
  ["How do you handle client reviews?","Review Desk answers every review in your voice, so each reply adds to your reputation instead of sitting unanswered."]],
 "Hair Salons":[
  ["Does LocalLift work for a single salon?","Yes. LocalLift runs for you, so one salon gets the same weekly work without adding to the front desk."],
  ["Do you need our photos?","Your own photos work best. Share them with us and we will put them to work in your daily Google posts."],
  ["How do you handle a negative review?","Calmly and in your voice. We thank the client, acknowledge the concern and invite them to talk with you directly."],
  ["Will our hours and services stay correct online?","Yes. Site Read checks hours, services and prices across your website, your Google profile and AI answers every week."]],
 "Hospitality":[
  ["Can LocalLift help us earn more direct bookings?","We strengthen your own Google profile and website so travelers have a reason to book with you directly, and we report the calls and website clicks that come from Google."],
  ["How do you respond to guest reviews?","In your voice, while the stay is still fresh. Thoughtful replies show future guests that someone is paying attention."],
  ["Do you track how AI assistants recommend hotels?","Yes. Every week we ask the trip questions your guests ask and record which properties are named."],
  ["Do you work with groups of properties?","Yes. Portfolio reporting shows every property side by side on the same measures."]],
 "Portfolios":[
  ["How do you compare properties in different markets?","Each property is measured against its own local market, then scored on the same Lift Score, so a portfolio view is a fair comparison."],
  ["Can ownership read the reports directly?","Yes. Every report is written to be read in minutes and forwarded as it is."],
  ["How many properties can you cover?","From a handful to a full portfolio. Each property gets the same weekly read and one recommended move."],
  ["Do property teams need to change how they work?","No. There is no new login. Teams receive one clear next step each week, and our team does the visibility work."]],
};
const PAGES={home:App,industries:IndustriesIndex};
IND.forEach(x=>{PAGES['ind:'+x.t]=()=>html`<${IndustryPage} name=${x.t}/>`});

var P=PAGES[window.__PAGE__];if(P)ReactDOM.hydrateRoot(document.getElementById("root"),React.createElement(P));})();