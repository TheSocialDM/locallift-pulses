(function(){const{useState:g,useEffect:L,useRef:U,useMemo:ee}=React,o=htm.bind(React.createElement),ye="/assets/logo-white.png",Pe="/assets/socialdm-logo.png",A=typeof window<"u"&&!!window.matchMedia&&window.matchMedia("(prefers-reduced-motion: reduce)").matches;function ae(e){return function(){e|=0,e=e+1831565813|0;let s=Math.imul(e^e>>>15,1|e);return s=s+Math.imul(s^s>>>7,61|s)^s,((s^s>>>14)>>>0)/4294967296}}function we(e,s,a,i,t){const n=ae(a),d=[],c=(r,m)=>{const h=[];for(let p=0;p<=24;p++)h.push(r(p/24));d.push({pts:h,major:m})};for(let r=0;r<=i;r++){const m=e*r/i+(n()-.5)*e/i*.5,h=(n()-.5)*e*.035,p=1.5+n()*2,y=(n()-.5)*e*.03,w=n()<.16;c(f=>[m+Math.sin(f*p*3)*h+y*f,s*f],w)}for(let r=0;r<=t;r++){const m=s*r/t+(n()-.5)*s/t*.5,h=(n()-.5)*s*.035,p=1.5+n()*2,y=(n()-.5)*s*.03,w=n()<.16;c(f=>[e*f,m+Math.sin(f*p*3)*h+y*f],w)}return c(r=>[e*(-.05+r*1.1),s*(.92-r*.8)+Math.sin(r*5)*s*.04],!0),c(r=>[e*(.15+r*.9),s*(.02+r*r*.98)],!0),d}const Be=e=>"M"+e.map(s=>s[0].toFixed(1)+" "+s[1].toFixed(1)).join("L");function B(e){const[s,a]=g(!1);return L(()=>{if(!window.matchMedia)return;const i=matchMedia(e),t=n=>a(n.matches);return a(i.matches),i.addEventListener("change",t),()=>i.removeEventListener("change",t)},[e]),s}const Ye=({size:e=24,color:s="#E22319",hole:a="#fff"})=>o`<svg width=${e} height=${e*34/24} viewBox="0 0 24 34" aria-hidden="true"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill=${s}/><circle cx="12" cy="12" r="4.6" fill=${a}/></svg>`,fe=({h:e=40})=>o`<span className="logo"><img src=${ye} alt="LocalLift" style=${{height:e+"px"}}/><span className="ring"></span><span className="ring b"></span></span>`,M=({children:e})=>o`<div className="eyebrow"><i></i>${e}</div>`;function E(e=.2){const s=U(null),[a,i]=g(!1),[t,n]=g(!1);return L(()=>{if(!window.IntersectionObserver||!s.current)return;const d=new IntersectionObserver(c=>{n(c[0].isIntersecting),c[0].isIntersecting&&i(!0)},{threshold:e});return d.observe(s.current),()=>d.disconnect()},[]),[s,a,t]}function P({to:e,run:s,from:a=0,dur:i=1500}){const[t,n]=g(e);return L(()=>{if(!s||A){n(e);return}let d,c;const r=m=>{c=c||m;const h=Math.min(1,(m-c)/i),p=1-Math.pow(1-h,3);n(Math.round(a+(e-a)*p)),h<1&&(d=requestAnimationFrame(r))};return d=requestAnimationFrame(r),()=>cancelAnimationFrame(d)},[s,e]),o`<span className="cnt">${t.toLocaleString("en-US")}</span>`}function se({items:e,run:s}){const[a,i]=g(0);return L(()=>{if(i(0),!s||A)return;const t=setInterval(()=>i(n=>(n+1)%e.length),2900);return()=>clearInterval(t)},[s,e]),o`<div className="pops" aria-hidden="true"><div className="pop" key=${a}><i></i><span>${e[a%e.length]}</span></div></div>`}const Q=7900,Oe=Q-24,D={v:Q,started:!1,subs:new Set},ge=e=>{D.v=e,D.subs.forEach(s=>s(e))};function ze(){if(D.started||A)return;D.started=!0;const e=7400,s=1600;let a;const i=t=>{a=a||t;const n=Math.min(1,(t-a)/s);if(ge(Math.round(e+(Oe-e)*(1-Math.pow(1-n,3)))),n<1)requestAnimationFrame(i);else{const d=setInterval(()=>{if(D.v>=Q){clearInterval(d);return}ge(Math.min(Q,D.v+1))},90)}};requestAnimationFrame(i)}function J(){const[e,s]=g(D.v);return L(()=>(D.subs.add(s),s(D.v),ze(),()=>D.subs.delete(s)),[]),o`<span className="cnt">${e.toLocaleString("en-US")}</span>`}function qe(){return o`<span className="doors-stat"><i className="live-dot"></i><strong><${J}/>+</strong> doors and counting</span>`}const $e=[["Platform","/#platform"],["Industries","/industries/"],["Intelligence","/#intelligence"],["Results","/#results"]];function te(){const[e,s]=g(!1);return o`<header className="nav"><div className="wrap">
    <div className="nav-in">
      <a href="/" aria-label="LocalLift home"><${fe}/></a>
      <nav className="nav-links" aria-label="Main">
        ${$e.map(([a,i])=>o`<a key=${a} href=${i}>${a}</a>`)}
        <a className="back-sdm" href="https://www.thesocialdm.com/">The SocialDM</a>
        <a className="btn red" style=${{color:"#fff"}} href="/#audit">Get Your Visibility Audit</a>
      </nav>
      <button className="menu-btn" aria-label="Menu" aria-expanded=${e} onClick=${()=>s(!e)}>
        <svg width="20" height="14" viewBox="0 0 20 14" aria-hidden="true"><path d="M0 1h20M0 7h20M0 13h20" stroke="currentColor" strokeWidth="1.6"/></svg>
      </button>
    </div>
    <nav className=${"nav-drop"+(e?" open":"")} aria-label="Mobile">
      ${$e.map(([a,i])=>o`<a key=${a} href=${i} onClick=${()=>s(!1)}>${a}</a>`)}
      <a href="https://www.thesocialdm.com/">Back to The SocialDM</a>
      <a className="btn red" href="/#audit" onClick=${()=>s(!1)}>Get Your Visibility Audit</a>
    </nav>
  </div></header>`}function oe(){const e=U(null);return L(()=>{const s=e.current,a=s.getContext("2d");let i,t,n,d,c,r,m,h=!0,p=performance.now();const y=new Path2D("M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z");function w(){const l=s.parentElement.getBoundingClientRect(),v=Math.min(window.devicePixelRatio||1,2);i=Math.max(320,l.width),t=Math.max(320,l.height),s.width=i*v,s.height=t*v,a.setTransform(v,0,0,v,0,0);const u=i<=720;c=u?i*.56:i*.72,r=u?t-120:t*.5;const k=we(i,t,7,Math.round(i/78),Math.round(t/78));n=document.createElement("canvas"),n.width=s.width,n.height=s.height;const b=n.getContext("2d");b.setTransform(v,0,0,v,0,0),b.fillStyle="#000000",b.fillRect(0,0,i,t),k.forEach(C=>{b.beginPath(),C.pts.forEach((N,$)=>$?b.lineTo(N[0],N[1]):b.moveTo(N[0],N[1])),b.strokeStyle=C.major?"rgba(255,255,255,.17)":"rgba(255,255,255,.065)",b.lineWidth=C.major?1.4:1,b.stroke()});const T=ae(21);d=[];const W=u?20:44;let S=0;for(;d.length<W&&S++<2e3;){const C=i*(u?.04+T()*.92:.28+T()*.7),N=t*(u?.42+T()*.56:.05+T()*.9),$=Math.hypot(C-c,N-r);$<60||d.some(x=>Math.hypot(x.x-C,x.y-N)<58)||d.push({x:C,y:N,d:$})}}function f(l){const v=Math.max(0,(l-p)/1e3),u=4.2,k=Math.hypot(Math.max(c,i-c),Math.max(r,t-r))*.9;a.drawImage(n,0,0,i,t);const b=[0,1,2].map(S=>{const C=(v+S*u/3)%u/u;return{age:C,r:C*k}});b.forEach(({age:S,r:C})=>{a.beginPath(),a.arc(c,r,C,0,6.2832),a.strokeStyle=`rgba(226,35,25,${(1-S)*.55})`,a.lineWidth=1.3,a.stroke()}),d.forEach((S,C)=>{let N=A&&C%3===0?.8:0;if(A||b.forEach(({r:$})=>{const x=($-S.d)/k*u;x>=0&&x<2.1&&(N=Math.max(N,1-x/2.1))}),N>.02){const $=(c+S.x)/2+(S.y-r)*.12,x=(r+S.y)/2-(S.x-c)*.12;a.beginPath(),a.moveTo(c,r),a.quadraticCurveTo($,x,S.x,S.y),a.strokeStyle=`rgba(226,35,25,${N*.42})`,a.lineWidth=1,a.stroke(),a.beginPath(),a.arc(S.x,S.y,7+(1-N)*10,0,6.2832),a.strokeStyle=`rgba(255,90,77,${N*.5})`,a.stroke()}a.beginPath(),a.arc(S.x,S.y,3,0,6.2832),a.fillStyle=N>.02?`rgba(255,90,77,${.35+N*.65})`:"rgba(255,255,255,.3)",a.fill()});const T=a.createRadialGradient(c,r,0,c,r,120);T.addColorStop(0,"rgba(226,35,25,.28)"),T.addColorStop(1,"rgba(226,35,25,0)"),a.fillStyle=T,a.fillRect(c-120,r-120,240,240);const W=1.65;a.save(),a.translate(c-12*W,r-34*W),a.scale(W,W),a.fillStyle="#E22319",a.fill(y),a.beginPath(),a.arc(12,12,4.6,0,6.2832),a.fillStyle="#fff",a.fill(),a.restore()}function G(l){h&&f(l),m=requestAnimationFrame(G)}w(),f(p+2600);const R=new ResizeObserver(()=>{w(),f(performance.now())});R.observe(s.parentElement);const I=new IntersectionObserver(l=>{h=l[0].isIntersecting});return I.observe(s),A||(m=requestAnimationFrame(G)),()=>{cancelAnimationFrame(m),R.disconnect(),I.disconnect()}},[]),o`<canvas ref=${e} aria-hidden="true"></canvas>`}const K=[["Google Search","apartments near downtown with a pool"],["Google Maps","med spa open near me"],["AI answer","who is the best listing agent in my area?"],["Google Maps","dermatologist accepting new patients"],["AI answer","which boutique hotel should I book this weekend?"],["Google Search","build to rent homes with a yard"]];function He(){const[e,s]=g(0),[a,i]=g(A?99:0);return L(()=>{if(A)return;const t=K[e][1];if(a<t.length){const d=setTimeout(()=>i(a+1),38);return()=>clearTimeout(d)}const n=setTimeout(()=>{i(0),s((e+1)%K.length)},2200);return()=>clearTimeout(n)},[e,a]),o`<div className="ticker" aria-label="Sample customer searches">
    <div className="ticker-top"><span>Someone is asking</span><span>${K[e][0]}</span></div>
    <div className="ticker-q">${K[e][1].slice(0,a)}<span className="caret"></span></div>
  </div>`}function je(){return o`<div className="stat-band"><div className="wrap"><div className="stat-grid">
    <div className="stat-c"><div className="stat-l">By the numbers</div><div className="stat-s">Every report audited before it ships.</div></div>
    <div className="stat-c"><div className="stat-n"><${J}/>+</div><div className="stat-t">Doors and counting</div></div>
    <div className="stat-c"><div className="stat-n">400+</div><div className="stat-t">Posts published every week</div></div>
    <div className="stat-c"><div className="stat-n">10</div><div className="stat-t">Tools working for you</div></div>
  </div></div></div>`}function Ve(){return o`<section className="hero" id="top"><${oe}/>
    <div className="wrap hero-in">
      <${M}>Local visibility intelligence<//>
      <h1>Your next customer is searching. <em>Will they find you?</em></h1>
      <p className="sub">LocalLift shows how your business appears across Google, Google Maps, AI search and local discovery, then strengthens it through intelligence, strategy, content and managed execution.</p>
      <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a><a className="btn ghost" href="#map">See the signal</a></div>
      <${He}/>
    </div>
    <div className="sample hero-cap">Illustrative map and sample searches</div>
  </section>
  <div className="statement"><div className="wrap statement-in"><span>Be found.</span><span>Be understood.</span><span>Be chosen.</span></div></div><${je}/>`}const be=[{id:"apt",label:"apartments near me",k:15,p:1.5,n:3,comps:["Sample Community A","Sample Community B","Sample Community C","Sample Community D"]},{id:"spa",label:"med spa near me",k:24,p:1.15,n:4,comps:["Sample Med Spa A","Sample Med Spa B","Sample Med Spa C","Sample Med Spa D"]},{id:"agent",label:"best real estate agent near me",k:34,p:1,n:6,comps:["Sample Agent A","Sample Agent B","Sample Agent C","Sample Agent D"]}],ie=800,ke=560,Y=400,O=280;function _e(){const[e,s]=g(0),[a,i]=g(null),t=B("(max-width:720px)"),n=be[e],d=ee(()=>we(ie,ke,11,12,9),[]),c=ee(()=>{const l=ae(5),v=[];for(let u=0;u<8;u++)for(let k=0;k<11;k++){const b=40+k*72+(u%2?36:0)+(l()-.5)*12,T=35+u*70+(l()-.5)*12,W=Math.hypot((b-Y)/380,(T-O)/270);v.push({x:b,y:T,d:W,noise:l()})}return v.filter(u=>u.d<1.02&&u.d>.1&&u.x<ie-20&&u.x>20)},[]),r=t?{x:170,w:460}:{x:0,w:ie},h=c.filter(l=>l.x>r.x+16&&l.x<r.x+r.w-16).map(l=>{const v=Math.round(1+n.k*Math.pow(l.d,n.p)+(l.noise-.5)*n.n*2);return{...l,rank:Math.max(1,v)}}),p=h.find(l=>l.x===(a&&a.x)&&l.y===(a&&a.y))||h.reduce((l,v)=>Math.hypot(l.x-560,l.y-190)<Math.hypot(v.x-560,v.y-190)?l:v),y=h.filter(l=>l.rank<=3).length,w=h.filter(l=>l.rank>3&&l.rank<=10).length,f=h.filter(l=>l.rank>10).length,G=ee(()=>{const l=Math.floor(p.noise*4),v=[0,1,2,3].map(b=>n.comps[(b+l)%4]),u=[];let k=0;for(let b=1;b<=3;b++)b===p.rank?u.push({pos:b,name:"Your business",you:!0}):u.push({pos:b,name:v[k++]});return u},[p,n]),R=l=>l<=3?"#E22319":l<=10?"#141414":"#FFFFFF",I=l=>l<=10?"#FFFFFF":"#595959";return o`<section className="band white" id="map"><div className="wrap">
    <div className="reach-head">
      <div><${M}>Map Reach<//><h2 className="title">Your rank can change <em>every few streets.</em></h2></div>
      <p className="lede" style=${{marginTop:0}}>A search from your front door shows only one view. Tap any point to see what a customer standing there sees.</p>
    </div>
    <div className="chips" role="group" aria-label="Sample search">
      ${be.map((l,v)=>o`<button key=${l.id} className="chip" aria-pressed=${v===e} onClick=${()=>{s(v)}}>${l.label}</button>`)}
    </div>
    <div className="reach-grid">
      <div className="reach-map">
        <svg viewBox=${r.x+" 0 "+r.w+" "+ke} role="group" aria-label="Illustrative neighborhood map with sample rank at each point">
          ${d.map((l,v)=>o`<path key=${v} d=${Be(l.pts)} fill="none" stroke=${l.major?"#C9C9C9":"#E2E2E2"} strokeWidth=${l.major?3.5:1.5}/>`)}
          <circle key=${"w"+e} className="wave" cx=${Y} cy=${O} r="460"/>
          <circle key=${"w2"+e} className="wave" style=${{animationDelay:".5s",opacity:0}} cx=${Y} cy=${O} r="460"/>
          <line className="link-line" x1=${Y} y1=${O} x2=${p.x} y2=${p.y}/>
          ${h.map((l,v)=>o`<g key=${l.x+"-"+l.y} className="pt" tabIndex="0" role="button" aria-label=${"Rank "+(l.rank>20?"beyond 20":l.rank)+" at this point"} onClick=${()=>i(l)} onKeyDown=${u=>{(u.key==="Enter"||u.key===" ")&&(u.preventDefault(),i(l))}}>
            <circle cx=${l.x} cy=${l.y} r="30" fill="transparent"/>
            <circle className="dot" cx=${l.x} cy=${l.y} r="17" style=${{transitionDelay:l.d*500+"ms"}} fill=${R(l.rank)} stroke=${l===p||l.x===p.x&&l.y===p.y?"#000000":l.rank>10?"#B8B8B8":"transparent"} strokeWidth=${l.x===p.x&&l.y===p.y?2.5:1}/>
            <text x=${l.x} y=${l.y} fill=${I(l.rank)} style=${{transitionDelay:l.d*500+"ms"}}>${l.rank>20?"20+":l.rank}</text>
          </g>`)}
          <g transform=${`translate(${Y-18} ${O-51}) scale(1.5)`}><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319" stroke="#fff" strokeWidth="1.2"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></g>
        </svg>
      </div>
      <aside className="reach-side">
        <div className="fade" key=${p.x+"-"+e}>
          <h3>A customer searching from this point sees</h3>
          <ul className="results" style=${{marginTop:"10px"}}>
            ${G.map(l=>o`<li key=${l.pos} className=${l.you?"you":""}><span>${l.name}</span><b>${l.pos}</b></li>`)}
            ${p.rank>3?o`<li className="you"><span>Your business</span><b>${p.rank>20?"beyond 20":p.rank}</b></li>`:null}
          </ul>
        </div>
        <div className="tally">
          <div><strong>${y}</strong><span>points in the top 3</span></div>
          <div><strong>${w}</strong><span>points ranked 4 to 10</span></div>
          <div><strong>${f}</strong><span>points ranked 11 or lower</span></div>
        </div>
        <div className="legend"><span><i style=${{background:"#E22319"}}></i>Top 3</span><span><i style=${{background:"#141414"}}></i>4 to 10</span><span><i style=${{background:"#fff",border:"1px solid #B8B8B8"}}></i>11 and beyond</span></div>
        <div className="sample">Illustrative sample. Not client data.</div>
      </aside>
    </div>
  </div></section>`}function Ue(){return o`<section className="band char" id="problem"><div className="wrap">
    <${M}>The visibility problem<//>
    <h2 className="title" style=${{maxWidth:"17em"}}>The same question gets three different answers. <em>You may be missing from all of them.</em></h2>
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
        <div className="row you" style=${{borderTop:"1px solid var(--on-dark-3)"}}><span>Your business</span><b>not named</b></div>
        <p className="verdict">A shortlist can form before your website gets a visit.</p>
      </article>
    </div>
    <div className="bfc">
      <div><h3>Be found.</h3><p>Show up where people look, across the whole area you serve, not only from your own address.</p></div>
      <div><h3>Be understood.</h3><p>See how Google and AI tools describe your business, your prices and your offers, and catch what is wrong.</p></div>
      <div><h3>Be chosen.</h3><p>Give people a current, credible reason to pick you over the other names on the list.</p></div>
    </div>
  </div></section>`}const Ne=[{t:"Discover",h:"See yourself the way a customer does.",p:"We look at your business across Google Search, Google Maps and AI answers, and across the neighborhoods you want to reach.",tools:["AI Shortlist","Map Reach","Site Read"]},{t:"Compare",h:"See who gets picked instead.",p:"We track which competitors are recommended in your place and what they are doing in your market.",tools:["AI Shortlist","Market Survey"]},{t:"Strengthen",h:"Close the gaps for you.",p:"Our team does the work: a daily presence on Google, review responses in your voice, and content built for the people you want to reach.",tools:["Daily Presence","Review Desk"]},{t:"Measure",h:"Know what changed and what comes next.",p:"Every week you see what moved, in one page and one score, with one recommended next step. Monthly reports carry the longer view.",tools:["Weekly Pulse","Lift Score","Snapshot","ClearView"]}];function Qe({goTool:e}){const[s,a]=g(0),[i,t]=g(!A);L(()=>{if(!i)return;const r=setInterval(()=>a(m=>(m+1)%4),5200);return()=>clearInterval(r)},[i]);const n=Ne[s],d=2*Math.PI*150,c=[[50,15.5],[84.5,50],[50,84.5],[15.5,50]];return o`<section className="band white" id="platform"><div className="wrap">
    <${M}>The platform<//>
    <h2 className="title">Discover. Compare. Strengthen. Measure.</h2>
    <p className="lede">One loop that keeps running, week after week, so visibility never becomes a project you finished last year.</p>
    <div className="fw">
      <div className="ring-box">
        <svg viewBox="0 0 400 400" aria-hidden="true">
          <circle cx="200" cy="200" r="150" fill="none" stroke="#E4E4E4" strokeWidth="1.5"/>
          <g className="arc" style=${{transform:`rotate(${s*90-135}deg)`}}>
            <circle cx="200" cy="200" r="150" fill="none" stroke="#E22319" strokeWidth="3" strokeDasharray=${`${d/4} ${d*3/4}`}/>
          </g>
          <g transform="translate(182 172) scale(1.5)"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319"/><circle cx="12" cy="12" r="4.6" fill="#fff"/></g>
        </svg>
        ${Ne.map((r,m)=>o`<button key=${r.t} className="stage-btn" style=${{left:c[m][0]+"%",top:c[m][1]+"%"}} aria-pressed=${m===s} onClick=${()=>{a(m),t(!1)}}>${r.t}</button>`)}
      </div>
      <div className="fw-detail fade" key=${s}>
        <div className="step">${s+1} of 4</div>
        <h3>${n.h}</h3>
        <p>${n.p}</p>
        <div className="tool-links">${n.tools.map(r=>o`<button key=${r} className="tool-link" onClick=${()=>e(r)}>${r}</button>`)}</div>
      </div>
    </div>
  </div></section>`}const z=({rows:e})=>o`<div>${e.map((s,a)=>o`<div className="drow" key=${a}><span>${s[0]}</span><span>${s[1]}</span><b className=${s[3]||""}>${s[2]}</b></div>`)}</div>`;function Je(){const e=B("(max-width:600px)"),s=e?12:11,a=[52,54,55,58,60,61,64,68],i=e?320:520,t=e?150:170,n=30,d=e?12:18,c=14,r=26,m=y=>n+y*(i-n-d)/(a.length-1),h=y=>c+(80-y)*(t-c-r)/40,p=a.map((y,w)=>(w?"L":"M")+m(w)+" "+h(y)).join("");return o`<svg viewBox=${`0 0 ${i} ${t}`} style=${{width:"100%",height:"auto",display:"block"}} role="img" aria-label="Sample Lift Score rising from 52 to 68 across eight weeks">
    ${[40,60,80].map(y=>o`<g key=${y}><line x1=${n} x2=${i-d} y1=${h(y)} y2=${h(y)} stroke="#2A2A2A"/><text x=${n-8} y=${h(y)+4} fontSize=${s} textAnchor="end" fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">${y}</text></g>`)}
    <path d=${p+`L${m(7)} ${t-r}L${m(0)} ${t-r}Z`} fill="rgba(226,35,25,.14)"/>
    <path d=${p} fill="none" stroke="#FF5A4D" strokeWidth="2"/>
    <circle cx=${m(7)} cy=${h(68)} r="4.5" fill="#FF5A4D"/>
    <text x=${n} y=${t-6} fontSize=${s} fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">Week 1</text>
    <text x=${i-d} y=${t-6} fontSize=${s} textAnchor="end" fill="rgba(255,255,255,.72)" fontFamily="var(--mono)">Week 8</text>
  </svg>`}const q=[{n:"Weekly Pulse",c:"Fridays",d:"One page on what changed across Search, Maps and AI, plus one recommended next step.",b:()=>o`<div><${z} rows=${[["Search","More people found you for two local phrases","Up"],["Maps","Stronger on the east side, softer downtown","Mixed"],["AI answers","Named in one more answer this week","Up"]]}/><div className="next"><small>This week's one next step</small>Add your current offer to your Google profile before the weekend.</div></div>`},{n:"Lift Score",c:"Weekly",d:"A single number that shows whether you are getting easier to find.",b:()=>o`<div className="score"><div className="score-n">68</div><${Je}/></div>`},{n:"AI Shortlist",c:"Weekly",d:"Whether AI assistants recommend you, and who they suggest instead.",b:()=>o`<${z} rows=${[["Who should I try near me?","Competitor A, Competitor B","Not named","flag"],["Best value nearby?","You, Competitor C","Named","good"],["Who has the best reviews?","Competitor B, Competitor A","Not named","flag"],["Who is closest to downtown?","You, Competitor A","Named","good"]]}/>`},{n:"Map Reach",c:"Weekly",d:"Google Maps rank across the surrounding neighborhood, not only from your own address.",b:(e={})=>o`<div><div style=${{display:"grid",gridTemplateColumns:"repeat(9,minmax(0,1fr))",gap:"4px",maxWidth:"460px"}}>${Array.from({length:45}).map((s,a)=>{const i=a%9-4,t=Math.floor(a/9)-2,n=Math.hypot(i/4,t/2),d=Math.max(1,Math.round(1+n*n*14+a*7%5-1));return o`<div key=${a} style=${{aspectRatio:"1",display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"var(--mono)",fontSize:"12px",borderRadius:"50%",background:d<=3?"#E22319":d<=10?"#2A2A2A":"transparent",border:d>10?"1px solid #2A2A2A":"0",color:d>10?"rgba(255,255,255,.72)":"#fff"}}>${d}</div>`})}</div>${e.ind?null:o`<a href="#map" style=${{display:"inline-block",marginTop:"16px",fontSize:"15px"}}>Open the full map above</a>`}</div>`},{n:"Site Read",c:"Weekly",d:"Checks that Google and AI tools describe your business, your pricing and your specials accurately.",b:()=>o`<${z} rows=${[["Hours","Website and Google profile agree","Match","good"],["Current offer","Website shows it, Google profile does not","Fix","flag"],["Pricing","AI answer quotes last season's price","Fix","flag"],["Address and phone","Consistent everywhere checked","Match","good"]]}/>`},{n:"Market Survey",c:"Sundays",d:"Tracks what your competitors are doing in your market.",b:()=>o`<${z} rows=${[["Competitor A","New offer started this week","New","flag"],["Competitor B","Prices down from last survey","Changed","flag"],["Competitor C","No change since last survey","Steady"],["Competitor D","Added a new listing photo set","Changed"]]}/>`},{n:"Snapshot",c:"Monthly",d:"Your monthly Google report: searches, views, calls, direction requests and website clicks.",b:()=>o`<div className="tiles">${[["1,240","Searches"],["3,180","Views"],["46","Calls"],["88","Direction requests"],["212","Website clicks"]].map(e=>o`<div className="tile" key=${e[1]}><strong>${e[0]}</strong><span>${e[1]}</span></div>`)}</div>`},{n:"ClearView",c:"Monthly",d:"Your monthly social media report: what posted, what performed and what changes next.",b:()=>o`<${z} rows=${[["What posted","24 posts across your social channels","24"],["What performed","Neighborhood reels outperformed photo posts","Reels"],["What changes","More neighborhood content next month","Next"]]}/>`},{n:"Review Desk",c:"Ongoing",d:"Google review responses written in your voice, with fair housing and privacy in mind.",b:()=>o`<div><div className="quote"><small>Sample review, five stars</small>The team made the whole process easy and answered every question.</div><div className="quote"><small>Sample response, in your voice</small>Thank you for sharing this. We are glad the process felt easy, and we will pass your note along to the team.</div></div>`},{n:"Daily Presence",c:"7 days a week",d:"Daily posts on your Google profile, written for your business and your neighborhood.",b:()=>o`<div className="week">${[["Mon","Neighborhood guide"],["Tue","Common question"],["Wed","Team spotlight"],["Thu","Local event"],["Fri","Weekend idea"],["Sat","Customer favorite"],["Sun","Week ahead"]].map(e=>o`<div className="day" key=${e[0]}><b>${e[0]}</b><span>${e[1]}</span><i></i></div>`)}</div>`}];function Ke({tool:e,setTool:s}){const a=q.find(i=>i.n===e);return o`<section className="band mist" id="intelligence"><div className="wrap">
    <${M}>LocalLift intelligence<//>
    <h2 className="title" style=${{maxWidth:"15em"}}>Ten tools. <em>One clear read</em> on your market.</h2>
    <p className="lede">We run the tools and tell you what they mean. You get the answer, not another login to manage.</p>
    <div className="console">
      <div className="console-bar"><span>LocalLift Intelligence / Sample Business</span><span>Illustrative data. Not client results.</span></div>
      <div className="console-body">
        <div className="rail" role="group" aria-label="LocalLift tools">
          ${q.map(i=>o`<button key=${i.n} aria-pressed=${i.n===e} onClick=${()=>s(i.n)}><span>${i.n}</span><small>${i.c}</small></button>`)}
        </div>
        <div className="panel fade" key=${e}>
          <div className="panel-head"><h3>${a.n}</h3><span className="sample">${a.c}</span></div>
          <p className="panel-desc">${a.d}</p>
          <div className="panel-body">${a.b()}</div>
        </div>
      </div>
    </div>
  </div></section>`}const ne=e=>{let s="M"+e[0][0].toFixed(1)+" "+e[0][1].toFixed(1);for(let a=0;a<e.length-1;a++){const i=e[a-1]||e[a],t=e[a],n=e[a+1],d=e[a+2]||n;s+=`C${(t[0]+(n[0]-i[0])/6).toFixed(1)} ${(t[1]+(n[1]-i[1])/6).toFixed(1)} ${(n[0]-(d[0]-t[0])/6).toFixed(1)} ${(n[1]-(d[1]-t[1])/6).toFixed(1)} ${n[0].toFixed(1)} ${n[1].toFixed(1)}`}return s};function Ze({data:e,base:s,run:a,vis:i,name:t}){const n=B("(max-width:600px)"),d=n?12:11,c=n?320:680,r=n?210:250,m=n?30:34,h=n?10:16,p=14,y=28,w=e.length-1,[f,G]=g(w),[R,I]=g(!0);L(()=>{if(!i||!R||A)return;const $=setInterval(()=>G(x=>(x+1)%e.length),1100);return()=>clearInterval($)},[i,R]);const l=40,v=80,u=$=>m+$*(c-m-h)/w,k=$=>p+(v-$)*(r-p-y)/(v-l),b=ne(e.map(($,x)=>[u(x),k($)])),T=ne(s.map(($,x)=>[u(x),k($)])),W=150,S=u(f)+W+14>c-h?u(f)-W-12:u(f)+12,C=Math.max(2,Math.min(k(e[f])-34,r-y-70)),N=$=>{I(!1),G($)};return o`<svg viewBox=${`0 0 ${c} ${r}`} role="img" aria-label=${t+" sample trend from "+e[0]+" to "+e[w]}>
    <defs><linearGradient id="ln" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stopColor="#E22319" stopOpacity=".12"/><stop offset=".22" stopColor="#FF5A4D"/></linearGradient>
    <linearGradient id="ar" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stopColor="#E22319" stopOpacity=".3"/><stop offset="1" stopColor="#E22319" stopOpacity="0"/></linearGradient></defs>
    ${[40,60,80].map($=>o`<g key=${$}><line x1=${m} x2=${c-h} y1=${k($)} y2=${k($)} style=${{stroke:"var(--line)"}}/><text x=${m-8} y=${k($)+4} fontSize=${d} textAnchor="end" style=${{fill:"var(--grey)",fontFamily:"var(--mono)"}}>${$}</text></g>`)}
    <path className=${a?"area-in":""} d=${b+`L${u(w)} ${r-y}L${u(0)} ${r-y}Z`} fill="url(#ar)"/>
    <path d=${T} fill="none" stroke="#8C8C8C" strokeWidth="1.6" strokeDasharray="3 5"/>
    <path className=${a?"draw":""} pathLength="1" d=${b} fill="none" stroke="url(#ln)" strokeWidth="2.6"/>
    <text x=${m} y=${r-8} fontSize=${d} style=${{fill:"var(--grey)",fontFamily:"var(--mono)"}}>Week 1</text>
    <text x=${c-h} y=${r-8} fontSize=${d} textAnchor="end" style=${{fill:"var(--grey)",fontFamily:"var(--mono)"}}>Week ${e.length}</text>
    <line x1=${u(f)} x2=${u(f)} y1=${p} y2=${r-y} stroke="#8C8C8C" opacity=".5"/>
    <circle cx=${u(f)} cy=${k(s[f])} r="3.5" fill="#8C8C8C"/>
    <circle cx=${u(f)} cy=${k(e[f])} r="5" fill="#FF5A4D" stroke="#000000" strokeWidth="2"/>
    <g transform=${`translate(${S} ${C})`} style=${{transition:"transform .45s ease"}}>
      <rect className="tip-bg" width=${W} height="70" rx="3"/>
      <text x="11" y="20" fontSize="11" fill="rgba(255,255,255,.68)" fontFamily="var(--mono)">Week ${f+1}</text>
      <circle cx="15" cy="37" r="3.5" fill="#FF5A4D"/><text x="25" y="41" fontSize="12.5" fill="#fff">Lift Score</text><text x=${W-11} y="41" fontSize="12.5" textAnchor="end" fill="#fff" fontFamily="var(--mono)">${e[f]}</text>
      <circle cx="15" cy="55" r="3.5" fill="#8C8C8C"/><text x="25" y="59" fontSize="12.5" fill="rgba(255,255,255,.78)">Market</text><text x=${W-11} y="59" fontSize="12.5" textAnchor="end" fill="rgba(255,255,255,.78)" fontFamily="var(--mono)">${s[f]}</text>
    </g>
    ${e.map(($,x)=>o`<rect key=${x} className="bar-hit" x=${u(x)-(c-m-h)/w/2} y=${p} width=${(c-m-h)/w} height=${r-p-y} fill="transparent" onMouseEnter=${()=>N(x)} onClick=${()=>N(x)}/>`)}
  </svg>`}function Z({text:e,run:s}){const[a,i]=g(s&&!A?0:e.length);return L(()=>{if(a>=e.length)return;const t=setTimeout(()=>i(a+1),22);return()=>clearTimeout(t)},[a,e]),o`<span>${e.slice(0,a)}${a<e.length?o`<span className="caret"></span>`:null}</span>`}function re({data:e,labels:s,run:a,name:i,accentLast:t=!0,height:n=190,hi:d}){const c=B("(max-width:600px)"),r=c?320:680,m=c?Math.round(n*.9):n,h=8,p=8,y=26,w=24,[f,G]=g(d??e.length-1),R=Math.max(...e)*1.08,I=(r-h-p)/e.length;return o`<svg viewBox=${`0 0 ${r} ${m}`} role="img" aria-label=${i+" sample values "+e.join(", ")}>
    <line x1=${h} x2=${r-p} y1=${m-w} y2=${m-w} style=${{stroke:"var(--line)"}}/>
    ${e.map((l,v)=>{const u=(m-y-w)*l/R,k=v===f;return o`<g key=${v} className="bar-hit" onMouseEnter=${()=>G(v)} onClick=${()=>G(v)}>
      <rect x=${h+v*I} y=${y} width=${I} height=${m-y-w} fill="transparent"/>
      <rect className=${a?"grow-y":""} x=${h+v*I+I*.17} y=${m-w-u} width=${I*.66} height=${u} style=${{fill:k?"#E22319":"var(--bar)",animationDelay:v*45+"ms"}}/>
      ${k?o`<text x=${h+v*I+I/2} y=${m-w-u-8} fontSize=${c?13:14} fontWeight="500" textAnchor="middle" style=${{fill:"var(--ink)",fontFamily:"var(--mono)"}}>${l}</text>`:null}
      <text x=${h+v*I+I/2} y=${m-7} fontSize=${c?12:11} textAnchor="middle" style=${{fill:"var(--grey)",fontFamily:"var(--mono)"}}>${s[v]}</text>
    </g>`})}
  </svg>`}const H=[["Google listing",38,"#E22319"],["Search",27,"#F5F5F5"],["Paid",14,"#8C8C8C"],["Social",11,"#5A5A5A"],["Referral",10,"#3A3A3A"]];function Xe({run:e}){const[s,a]=g(0);let i=0;return o`<div>
    <div className="donut"><svg viewBox="0 0 42 42" role="img" aria-label="Sample share of leads by source">
      ${H.map((t,n)=>{const d=25-i;return i+=t[1],o`<circle key=${t[0]} className=${e?"seg":""} cx="21" cy="21" r="15.9155" fill="none" stroke=${t[2]} strokeWidth=${n===s?7:5.4} pathLength="100" strokeDasharray=${t[1]-.5+" "+(100-t[1]+.5)} strokeDashoffset=${d} onMouseEnter=${()=>a(n)} onClick=${()=>a(n)}/>`})}
    </svg><div className="donut-c"><strong>${H[s][1]}%</strong><span>${H[s][0]}</span></div></div>
    <div className="src-list">${H.map((t,n)=>o`<button key=${t[0]} className=${"src"+(n===s?" on":"")} onMouseEnter=${()=>a(n)} onClick=${()=>a(n)}><i className=${"sb"+(e?" grow-x":"")} style=${{width:t[1]/38*100+"%",animationDelay:n*90+"ms"}}></i><span>${t[0]}</span><b>${t[1]}%</b></button>`)}</div>
  </div>`}const j=[["Your community",1685,1610,1],["Competitor A",1640,1575],["Competitor B",1720,1590],["Competitor C",1595,1595],["Competitor D",1660,1540]],Se=1500,ea=1800,V=e=>(e-Se)/(ea-Se)*100,le=Math.round(j.slice(1).reduce((e,s)=>e+s[2],0)/4),xe=[["You",9,1],["Competitor A",14],["Competitor B",11],["Competitor C",6],["Competitor D",3]],aa=[["Best community near downtown?",[0,1,1,0]],["Which allows large dogs?",[1,1,0,0]],["Newest apartments in the area?",[1,0,1,0]],["Who has a move in special?",[0,1,0,1]]],Ae=[46,47,49,50,52,54,55,58,60,61,64,68],sa=[48,48,49,49,50,50,51,51,52,52,53,53],ta=["D","J","F","M","A","M","J","J","A","S","O","N"],oa=[18,21,19,24,26,25,29,31,30,34,37,41],ce=[{t:"Weekly Pulse",pops:["Three more map points in the top 3","Named in one more AI answer","New review answered"],body:(e,s)=>o`<div>
   <div className="rw-head"><h3>This week at a glance</h3><span className="sample">Every Friday</span></div>
   <div className="kpis">
     <div className="kpi"><strong><${P} to=${68} run=${e}/></strong><span>Lift Score</span><em>up 4</em></div>
     <div className="kpi"><strong><${P} to=${412} run=${e}/></strong><span>Actions on Google</span><em>up 11%</em></div>
     <div className="kpi"><strong><${P} to=${14} run=${e}/></strong><span>Map points in the top 3</span><em>up 3</em></div>
     <div className="kpi"><strong><${P} to=${9} run=${e}/> of 24</strong><span>AI answers that name you</span><em>up 1</em></div>
   </div>
   <div className="viz"><div className="viz-t">Lift Score against the market, last 12 weeks</div><${Ze} data=${Ae} base=${sa} run=${e} vis=${s} name="Lift Score"/></div>
   <div className="rw-so"><b>This week's one next step:</b> <${Z} run=${e} text="ask for five new reviews. Competitor A is pulling ahead on count."/></div>
 </div>`},{t:"LocalLift Lens",pops:["Google listing is your top lead source","Best month for leads this year","Search leads up for the third month"],body:e=>o`<div>
   <div className="rw-head"><h3>Where your business really came from</h3><span className="sample">Inside the Weekly Pulse</span></div>
   <div className="lens" style=${{marginTop:"20px"}}>
     <${Xe} run=${e}/>
     <div className="viz" style=${{marginTop:0}}><div className="viz-t">Leads, last 12 months</div><${re} data=${oa} labels=${ta} run=${e} name="Leads by month"/>
       <div className="rw-so"><b>So what:</b> <${Z} run=${e} text="your Google listing brought in more leads than any other source, so it gets the attention first."/></div></div>
   </div>
 </div>`},{t:"Market Survey",pops:["Competitor B has a new special","Competitor D is the lowest effective rent","You are above the market on one beds"],body:e=>o`<div>
   <div className="rw-head"><h3>One bedroom rent against your competitors</h3><span className="sample">Every Sunday</span></div>
   <div className="viz mk">
     <div className="mk-row h"><span>Community</span><span className="tk"><span className="axis"><span>$1,500</span><span>$1,600</span><span>$1,700</span><span>$1,800</span></span></span><b>Asking</b><b>Effective</b><b>Concession</b></div>
     ${j.map((s,a)=>o`<div key=${s[0]} className=${"mk-row"+(s[3]?" you":"")}>
       <span>${s[0]}</span>
       <span className="trk"><span className=${"ln"+(e?" grow-x":"")} style=${{left:V(s[2])+"%",width:V(s[1])-V(s[2])+"%",animationDelay:a*90+"ms"}}></span><span className="dot ask" style=${{left:V(s[1])+"%"}}></span><span className="dot" style=${{left:V(s[2])+"%"}}></span></span>
       <b>$${s[1].toLocaleString("en-US")}</b><b>$${s[2].toLocaleString("en-US")}</b><b>${((s[1]-s[2])/s[1]*100).toFixed(1)}%</b>
     </div>`)}
   </div>
   <div className="legend" style=${{marginTop:"12px"}}><span><i style=${{background:"var(--white)",border:"2px solid var(--ink)"}}></i>Asking rent</span><span><i style=${{background:"var(--ink)"}}></i>Effective rent</span></div>
   <div className="rw-so"><b>So what:</b> <${Z} run=${e} text=${"your effective rent is $"+(j[0][2]-le)+" above the $"+le.toLocaleString("en-US")+" competitor average on one beds."}/></div>
 </div>`},{t:"AI Shortlist",pops:["Competitor A named in 14 answers","You were added to one more answer","Competitor C dropped out of two answers"],body:e=>o`<div>
   <div className="rw-head"><h3>Who AI recommends instead of you</h3><span className="sample">Weekly</span></div>
   <div className="viz ai-bars">
     ${xe.map((s,a)=>o`<div key=${s[0]} className=${"ai-b"+(s[2]?" you":"")}><span>${s[0]}</span><div className="tr"><div className=${"fl"+(e?" grow-x":"")} style=${{width:s[1]/24*100+"%",animationDelay:a*90+"ms"}}></div></div><b>${s[1]} of 24</b></div>`)}
   </div>
   <div className="matrix">
     <div className="mq mh">Sample questions</div><div className="mh">You</div><div className="mh">A</div><div className="mh">B</div><div className="mh">C</div>
     ${aa.map((s,a)=>o`<${React.Fragment} key=${s[0]}><div className="mq">${s[0]}</div>${s[1].map((i,t)=>o`<div key=${t}><i className=${i?t===0?"y":"":"n"} style=${{animationDelay:(a*4+t)*60+"ms"}}></i></div>`)}<//>`)}
   </div>
 </div>`},{t:"The Brief",pops:["Short enough to forward from a phone"],body:e=>o`<div>
   <div className="rw-head"><h3>What to tell your team</h3><span className="sample">Top of the Weekly Pulse</span></div>
   <div className="brief" key=${e?"p":"r"}>
     <small>Sample Community, Quillmere</small>
     <ol>
       <li>Actions on Google are up 11% this week.</li>
       <li style=${{animationDelay:".2s"}}>Competitor B's one bed effective rent now sits $20 below yours.</li>
       <li style=${{animationDelay:".4s"}}>AI answers named you once more than last week.</li>
       <li className="ask" style=${{animationDelay:".6s"}}>The one ask: five new reviews this week.</li>
     </ol>
   </div>
 </div>`}];function Me(e,s){const[a,i]=g(0);return L(()=>{if(!s||A)return;const t=setInterval(()=>i(n=>n+1),e);return()=>clearInterval(t)},[e,s]),a}const Ie=[["Views on Google",1180],["Actions on Google",412],["Website visits",212],["Leads",10]],Ce=[["You",128,"+5",1],["Competitor A",164,"+8"],["Competitor B",97,"+2"],["Competitor C",61,"+1"]],Le=[["Competitor B started a new special","New"],["Competitor A posted on Google","Today"],["Competitor D lowered one bed rent","Down"],["Competitor C added new photos","New"],["Competitor A gained eight reviews","Up"]],ia=[["Quillmere",44],["Fernhallow",21],["Ostrabay",15],["Calderwick",11],["Brindlecrest",9]],We=[["Which apartments near downtown allow large dogs?",["Competitor A","Your community","Competitor C"]],["Who has the best recent reviews nearby?",["Competitor B","Competitor A"]],["What is the newest community in this area?",["Your community","Competitor B"]]];function na({run:e,vis:s}){const a=Me(5600,s),i=We[a%We.length];return o`<div key=${a}><div className="ask-q"><${Z} run=${e} text=${i[0]}/></div><div className="ask-l">A few names come up:</div><div className="ask-a">${i[1].map((t,n)=>o`<span key=${t} className=${t==="Your community"?"y":""} style=${{animationDelay:(e?i[0].length*22+n*260:0)+"ms"}}>${t}</span>`)}</div></div>`}function ra({vis:e}){const s=Me(2600,e),a=[0,1,2,3].map(i=>Le[(s+i)%Le.length]);return o`<div className="feed"><div className="feed-in" key=${s}>${a.map(i=>o`<div className="feed-r" key=${i[0]}><span>${i[0]}</span><b>${i[1]}</b></div>`)}</div></div>`}function la(){const e=[];for(let s=0;s<7;s++)for(let a=0;a<11;a++)e.push(Math.hypot(a-5,(s-3)*1.2));return o`<div className="sweep" aria-hidden="true">${e.map((s,a)=>o`<i key=${a} style=${{animationDelay:(s*.16).toFixed(2)+"s"}}></i>`)}<${Ye} size=${22} hole="#000000"/></div>`}function ca(){const[e,s,a]=E(.1),i=Math.max(...Ce.map(t=>t[1]));return o`<div ref=${e}>
    <h3 className="bento-h">A closer look at what we watch.</h3>
    <div className="bento">
      <div className="bt"><div className="bt-vis"><${la}/></div><h3>Signal across the map</h3><p>How far your visibility reaches, street by street.</p></div>
      <div className="bt"><div className="bt-vis"><${na} run=${s} vis=${a}/></div><h3>What AI says</h3><p>Who gets named when customers ask.</p></div>
      <div className="bt"><div className="bt-vis"><${ra} vis=${a}/></div><h3>Competitor moves</h3><p>What changed in your market this week.</p></div>
      <div className="bt"><div className="bt-vis"><div className="fn">${Ie.map((t,n)=>o`<div className="fn-r" key=${t[0]}><i className=${s?"grow-x":""} style=${{width:t[1]/Ie[0][1]*100+"%",animationDelay:n*140+"ms"}}></i><span>${t[0]}</span><b>${t[1].toLocaleString("en-US")}</b></div>`)}</div></div><h3>From view to lead</h3><p>Where people continue and drop off in a sample week.</p></div>
      <div className="bt"><div className="bt-vis"><div className="ai-bars" style=${{marginTop:0}}>${Ce.map((t,n)=>o`<div key=${t[0]} className=${"ai-b"+(t[3]?" you":"")}><span>${t[0]}</span><div className="tr"><div className=${"fl"+(s?" grow-x":"")} style=${{width:t[1]/i*100+"%",animationDelay:n*110+"ms"}}></div></div><b>${t[1]} ${t[2]}</b></div>`)}</div></div><h3>The review race</h3><p>Your review count against your competitors.</p></div>
      <div className="bt"><div className="bt-vis"><div className="src-list" style=${{marginTop:0}}>${ia.map((t,n)=>o`<div className=${"src"+(n===0?" on":"")} key=${t[0]} style=${{cursor:"default"}}><i className=${"sb"+(s?" grow-x":"")} style=${{width:t[1]/44*100+"%",animationDelay:n*90+"ms"}}></i><span>${t[0]}</span><b>${t[1]}%</b></div>`)}</div></div><h3>Where interest comes from</h3><p>The cities your visitors come from.</p></div>
    </div>
    <div className="sample" style=${{marginTop:"14px"}}>Sample graphics. Fake numbers and fictional cities.</div>
  </div>`}const da=()=>o`<div className="pghost" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div><div className="fade-out" aria-hidden="true"></div>`,ma=({d:e,c:s="#E22319"})=>{const t=Math.min(...e)-3,n=Math.max(...e)+3,d=ne(e.map((c,r)=>[4+r*312/(e.length-1),80-(c-t)*76/(n-t)]));return o`<svg viewBox=${"0 0 320 84"} aria-hidden="true"><path d=${d+"L316 84L4 84Z"} fill="rgba(226,35,25,.1)"/><path d=${d} fill="none" stroke=${s} strokeWidth="2.4"/></svg>`},_=[{t:"Weekly Pulse",when:"Every Friday",body:()=>o`<div><div className="big">68</div><div className="small">Lift Score, up 4 this week</div><${ma} d=${Ae}/><div className="pr you" style=${{marginTop:"8px",gridTemplateColumns:"1fr"}}><span>This week's one next step: ask for five new reviews.</span></div></div>`},{t:"Market Survey",when:"Every Sunday",body:()=>o`<div><div className="small" style=${{marginTop:"14px",marginBottom:"6px"}}>One bedroom effective rent</div>${j.map(e=>o`<div key=${e[0]} className=${"pr"+(e[3]?" you":"")}><span>${e[3]?"You":e[0]}</span><div className="t"><div className="f" style=${{width:(e[2]-1400)/300*100+"%"}}></div></div><b>$${e[2].toLocaleString("en-US")}</b></div>`)}<div className="pr you" style=${{marginTop:"8px",gridTemplateColumns:"1fr"}}><span>You sit $${j[0][2]-le} above the competitor average.</span></div></div>`},{t:"AI Shortlist",when:"Weekly",body:()=>o`<div><div className="big">9<span style=${{fontSize:"26px",letterSpacing:"-.02em"}}> of 24</span></div><div className="small">AI answers that name you</div><div style=${{marginTop:"12px"}}>${xe.slice(0,4).map(e=>o`<div key=${e[0]} className=${"pr"+(e[2]?" you":"")}><span>${e[0]}</span><div className="t"><div className="f" style=${{width:e[1]/24*100+"%"}}></div></div><b>${e[1]}</b></div>`)}</div></div>`},{t:"LocalLift Lens",when:"Every Friday",body:()=>o`<div><div className="big">38%</div><div className="small">of leads came from your Google listing</div><div style=${{marginTop:"12px"}}>${H.map((e,s)=>o`<div key=${e[0]} className=${"pr"+(s===0?" you":"")}><span>${e[0]}</span><div className="t"><div className="f" style=${{width:e[1]/38*100+"%"}}></div></div><b>${e[1]}%</b></div>`)}</div></div>`}],de=[{x:0,y:0,r:0,s:1,z:4,b:1},{x:62,y:-6,r:5,s:.95,z:3,b:.72},{x:-62,y:-2,r:-5,s:.93,z:2,b:.62},{x:112,y:6,r:10,s:.88,z:1,b:.45}];function ha(){const[e,s]=g(0),[a,i]=g(!A),[t,n,d]=E(.2),c=B("(max-width:560px)");L(()=>{if(!a||!d)return;const h=setInterval(()=>s(p=>(p+1)%_.length),3400);return()=>clearInterval(h)},[a,d]);const r=h=>{s(h),i(!1)},m=c?.5:1;return o`<div className="peek-grid">
    <div>
      <${M}>A sneak peek<//>
      <h2 className="title">Reports like no other. <em>Only the data that matters.</em></h2>
      <p className="lede">This is the look of what lands in your inbox. Every number here is made up and every place is fictional. The real reports are built for each client and audited before they ship.</p>
      <div className="peek-tabs" role="group" aria-label="Sneak peek reports">${_.map((h,p)=>o`<button key=${h.t} className="chip" aria-pressed=${p===e} onClick=${()=>r(p)}>${h.t}</button>`)}</div>
    </div>
    <div className="peek" ref=${t}>
      ${_.map((h,p)=>{const y=(p-e+_.length)%_.length,w=n||A?de[y]:{x:0,y:30,r:0,s:.94,z:de[y].z,b:de[y].b};return o`<button key=${h.t} className="paper" aria-label=${"Show the "+h.t+" sample"} onClick=${()=>r(p)} style=${{transform:`translate(${w.x*m}px,${w.y}px) rotate(${w.r*m}deg) scale(${w.s})`,zIndex:w.z,filter:`brightness(${w.b})`,transitionDelay:n?"0ms":y*120+"ms"}}>
        <div className="paper-wrap"><span className="paper-top"><img src=${ye} alt=""/><span>${h.when}</span></span>
        <div className="paper-in"><h3>${h.t}</h3><div className="sub">Sample Community, Quillmere</div>${h.body()}</div>
        <${da}/>
        <div className="paper-tag"><span>Fake numbers</span><b>Full report is private</b></div></div>
      </button>`})}
    </div>
  </div>`}function pa(){const[e,s]=g(0),[a,i]=g(!A),[t,n,d]=E(.15);L(()=>{if(!a||!d)return;const r=setInterval(()=>s(m=>(m+1)%ce.length),9e3);return()=>clearInterval(r)},[a,d]);const c=ce[e];return o`<section className="band black" id="reports"><div className="wrap">
    <${ha}/>
    <h3 className="bento-h">Open one up.</h3>
    <div className="rw" ref=${t} style=${{marginTop:"24px"}}>
      <div className="rw-bar"><span>Sample Community / Quillmere</span><span>Fake numbers. Fictional city. Not client data.</span></div>
      <div className="rw-tabs" role="group" aria-label="Sample reports">${ce.map((r,m)=>o`<button key=${r.t} aria-pressed=${m===e} onClick=${()=>{s(m),i(!1)}}>${r.t}</button>`)}</div>
      <div className="rw-body">
                <div className="fade" key=${e}>
          <div className="viz" style=${{marginTop:0,minHeight:"44px"}}><${se} items=${c.pops} run=${d}/></div>
          ${c.body(n,d)}
        </div>
      </div>
    </div>
    <${ca}/>
  </div></section>`}const Te=["Jun","Jul","Aug","Sep","Oct","Nov"],F=[{t:"Multifamily",who:"A renter relocating for a new job, with two weeks to decide.",s:["Searches for apartments near downtown with a pool and a move in special.","Opens Google Maps and compares the closest communities by recent reviews.","Asks an AI assistant which newer communities near the office allow large dogs.","Books tours at the two names that appeared everywhere."],tools:["Map Reach","AI Shortlist","Market Survey","Site Read"],city:"Sample community, Quillmere",metric:"Direction requests from Google",d:[62,71,68,84,92,108],pops:["Up in the last two months","A new map point reached the top 3"],stats:[["4","sample competitors tracked"],["9 of 24","sample AI answers naming you"]],doors:!0},{t:"Build to Rent",who:"A renter who wants a house and a yard without buying one.",s:["Searches for build to rent homes with a yard near work.","Checks Google Maps for commute, nearby parks and community photos.","Asks an AI assistant how build to rent differs from a house rental nearby.","Tours the community that explained itself clearly."],tools:["AI Shortlist","Site Read","Map Reach","Daily Presence"],city:"Sample community, Fernhallow",metric:"Website clicks from Google",d:[44,49,57,55,66,73],pops:["Named for build to rent in a new AI answer","Website clicks at a six month high"],big:["73","sample website clicks in November"],stats:[["7","sample posts a week on Google"],["2","sample site details corrected"]]},{t:"Medical",who:"A new patient comparing practices after a referral.",s:["Searches for the practice by name, then for a specialist near home.","Compares ratings, hours and location on Google Maps.","Asks an AI assistant who is well reviewed for that specialty nearby.","Calls the practice whose details all match and feel current."],tools:["Site Read","Review Desk","AI Shortlist","Map Reach"],city:"Sample practice, Ostrabay",metric:"Calls from Google",d:[31,34,33,41,46,52],pops:["Calls up again this month","Hours now match everywhere checked"],big:["52","sample calls from Google in November"],stats:[["4.9","sample Google rating"],["6","sample reviews answered this month"]]},{t:"Med Spa",who:"Someone choosing a first treatment, and reading everything first.",s:["Searches for a med spa open near work.","Scans Google Maps photos, reviews and how the owner answers them.","Asks an AI assistant which local med spa has the best reputation.","Books a consult at the name that looks established."],tools:["AI Shortlist","Review Desk","Daily Presence","Map Reach"],city:"Sample med spa, Marrowvale",metric:"Website clicks from Google",d:[58,63,74,72,88,97],pops:["Your med spa appeared in a new AI answer","A new review was answered"],big:["97","sample website clicks in November"],stats:[["5 of 12","sample AI answers naming you"],["30","sample Google posts this month"]]},{t:"Real Estate",who:"A homeowner getting ready to sell, looking for the right agent.",s:["Searches for the top listing agent in their neighborhood.","Reads Google reviews and looks at recent activity on each profile.","Asks an AI assistant who knows that part of town best.","Calls the agent who looks established and current."],tools:["AI Shortlist","Map Reach","Review Desk","Daily Presence"],city:"Sample agent, Calderwick",metric:"Profile views on Google",d:[120,134,129,151,168,186],pops:["Profile views keep climbing","Named for a new neighborhood"],big:["186","sample profile views in November"],stats:[["3","sample neighborhoods in the top 3"],["30","sample Google posts this month"]]},{t:"Hair Salons",who:"A neighbor who just moved in and needs a new salon by Saturday.",s:["Searches for a hair salon open Saturday near home.","Opens Google Maps and checks photos, hours and how owners answer reviews.","Asks an AI assistant which salon is best with curly hair nearby.","Books the salon that looked open, active and easy to trust."],tools:["Map Reach","Review Desk","Daily Presence","Snapshot"],city:"Sample salon, Wrenhollow",metric:"Direction requests from Google",d:[26,29,35,33,41,47],pops:["Saturday searches are finding you","New photos are live on Google"],big:["47","sample direction requests in November"],stats:[["4.8","sample Google rating"],["9","sample reviews answered this month"]]},{t:"Hospitality",who:"A traveler planning a weekend in a city they barely know.",s:["Searches for a boutique hotel near the old town with a rooftop.","Uses Google Maps to judge the walk to restaurants and sights.","Asks an AI assistant which stay fits a quiet anniversary trip.","Books the place that kept appearing, with recent photos and replies."],tools:["AI Shortlist","Review Desk","Snapshot","Daily Presence"],city:"Sample hotel, Brindlecrest",metric:"Website clicks from Google",d:[140,152,171,163,188,204],pops:["Weekend searches are up","AI answer named your rooftop"],big:["204","sample website clicks in November"],stats:[["2 of 8","sample AI answers naming you"],["14","sample reviews answered this month"]]},{t:"Portfolios",who:"An owner who needs one clear read on every property at once.",labels:["Portfolio view","Market","AI answers","Decision"],s:["Sees every property side by side, with the same measures on each.","Checks which properties are falling behind their local competitors.","Sees which properties AI assistants name, and which they skip.","Puts attention where one recommended move will count most."],tools:["Lift Score","Weekly Pulse","Market Survey","AI Shortlist"],city:"Sample portfolio, six properties",metric:"Lift Score by property",d:[58,74,63,81,49,68],labels2:["P1","P2","P3","P4","P5","P6"],pops:["Property 4 leads the portfolio","Property 5 needs attention first"],big:["66","sample portfolio average Lift Score"],stats:[["6","sample properties compared"],["1","recommended move per property"]]}],De=["Search","Google Maps","AI answer","Decision"];function Ge(){const[e,s]=g(0),a=F[e],[i,t,n]=E(.15),d=a.labels||De;return o`<section className="band white" id="industries"><div className="wrap">
    <${M}>Industries<//>
    <h2 className="title">Every customer takes a different path to <em>the same decision.</em></h2>
    <div className="tabs" role="group" aria-label="Choose an industry">
      ${F.map((c,r)=>o`<button key=${c.t} className="chip" aria-pressed=${r===e} onClick=${()=>s(r)}>${c.t}</button>`)}
    </div>
    <div className="fade" key=${e} ref=${i}>
      <p className="journey-who">${a.who}</p>
      <div className="journey">
        <div className="track"><span className="traveler"></span></div>
        ${a.s.map((c,r)=>o`<div className="j-step" key=${r}><h3>${d[r]}</h3><p>${c}</p></div>`)}
      </div>
      <div className="ia">
        <div>
          ${a.doors?o`<div className="ia-city">Multifamily doors we work across</div><div className="ia-big"><i className="live-dot"></i><span><${J}/>+</span></div><div className="ia-sub">doors and counting</div>`:o`<div className="ia-big"><${P} to=${+a.big[0]} run=${t}/></div><div className="ia-sub">${a.big[1]}</div>`}
          ${a.doors?o`<div className="ia-city" style=${{margin:"20px 0 -6px"}}>Sample figures</div>`:null}<div className="ia-stats">${a.stats.map(c=>o`<div key=${c[1]}><strong>${c[0]}</strong><span>${c[1]}</span></div>`)}</div>
        </div>
        <div>
          <div className="ia-city">${a.city}. Fake numbers.</div>
          <div className="viz" style=${{marginTop:0}}>
            <${se} items=${a.pops} run=${n}/>
            <div className="viz-t">${a.metric}</div>
            <${re} data=${a.d} labels=${a.labels2||Te} run=${t} name=${a.metric} height=${210}/>
          </div>
        </div>
      </div>
      <div className="j-tools"><b>Where LocalLift works this journey:</b><span>${a.tools.join(", ")}</span><a className="j-more" href=${X(a)}>See LocalLift for ${a.t}</a></div>
      <div className="sample" style=${{marginTop:"14px"}}>Sample journey, sample place and sample charts. Illustrative only.${a.doors?" The door count is real.":""}</div>
    </div>
  </div></section>`}function ua(){const e=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],s=t=>t?o`<i></i>`:null,[a,i]=E(.3);return o`<section className="band char" id="managed"><div className="wrap">
    <${M}>Fully managed<//>
    <h2 className="title" style=${{maxWidth:"15em"}}>We are not selling another <em>complicated dashboard.</em></h2>
    <p className="lede">We provide the intelligence and we help you act on it. Your team stays focused on customers, and the visibility work keeps moving every day.</p>
    <div className="m-grid">
      <ul className="not-list">
        <li>One team across Google, Maps, AI answers and content.</li>
        <li>Written reports you can read in minutes and forward to ownership.</li>
        <li>One recommended next step each week, in plain language.</li>
        <li>No new platform for your team to log in to or learn.</li>
      </ul>
      <div>
        <p className="sched-hint">Swipe to see the full week.</p><div className="sched-wrap"><div className="sched" role="table" aria-label="A typical LocalLift week">
          <div className="h"></div>${e.map(t=>o`<div className="h" key=${t}>${t}</div>`)}
          <div className="n">Daily Presence</div>${e.map(t=>o`<div className="c" key=${t}>${s(!0)}</div>`)}
          <div className="n">Review Desk</div><div className="span">Ongoing</div>
          <div className="n">Weekly reads</div><div className="span">Lift Score, AI Shortlist, Map Reach, Site Read</div>
          <div className="n">Weekly Pulse</div>${e.map(t=>o`<div className="c" key=${t}>${s(t==="Fri")}</div>`)}
          <div className="n">Market Survey</div>${e.map(t=>o`<div className="c" key=${t}>${s(t==="Sun")}</div>`)}
        </div></div>
        <p className="sched-note">Snapshot and ClearView arrive monthly.</p>
      </div>
    </div>
  </div></section>`}function va(){return o`<section className="band mist" id="results"><div className="wrap">
    <${M}>Results and insights<//>
    <h2 className="title" id="insights">See the work and <em>the thinking behind it.</em></h2>
    <div className="cards">
      <a className="card" href="https://www.thesocialdm.com/blog/montage-tigard-case-study" target="_blank" rel="noopener"><span className="sample">Case study</span><h3>Montage, Tigard, Oregon</h3><p>33 reviews at 4.8 as of October 2026.</p><em>Read the case study</em></a>
      <a className="card" href="https://www.thesocialdm.com/2026-multifamily-visibility-report" target="_blank" rel="noopener"><span className="sample">Research</span><h3>2026 Multifamily Visibility Report</h3><p>Published by The SocialDM, powered by LocalLift.</p><em>Read the report</em></a>
      <a className="card" href="https://www.thesocialdm.com/blog" target="_blank" rel="noopener"><span className="sample">Insights</span><h3>Market Intelligence</h3><p>Ongoing writing on Google, Maps, AI search and local visibility.</p><em>Read the latest</em></a>
    </div>
  </div></section>`}function me({industry:e=""}){const[s,a]=g("idle");return o`<section className="band black audit" id="audit">
    <div className="audit-rings" aria-hidden="true"><span></span><span></span><span></span></div>
    <div className="wrap audit-grid">
      <div>
        <${M}>Visibility audit<//>
        <h2 className="title">See where you show up, and <em>where you don't.</em></h2>
        <p className="lede">We check Google Search, Google Maps and AI answers for your business and send a clear plan to close the gaps.</p>
      </div>
      ${s==="sent"?o`<div className="form form-done" role="status"><h3>Thanks. We have your request.</h3><p>A real person will reply within one business day. Check your inbox for a copy of what you sent.</p></div>`:o`<form className="form" method="post" action="/api/audit" onSubmit=${async t=>{t.preventDefault();const n=t.currentTarget;if(n.reportValidity()){a("sending");try{const d=await fetch("/api/audit",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(Object.fromEntries(new FormData(n)))});a(d.ok?"sent":"error")}catch{a("error")}}}}>
        <label htmlFor="biz">Business name<input id="biz" name="business" required maxLength="120" placeholder="Your business" autoComplete="organization"/></label>
        <label htmlFor="city">City<input id="city" name="city" required maxLength="80" placeholder="Your city" autoComplete="address-level2"/></label>
        <label htmlFor="ind">Industry<select id="ind" name="industry" required defaultValue=${e}><option value="" disabled>Select your industry</option>${F.map(t=>o`<option key=${t.t}>${t.t}</option>`)}<option>Other</option></select></label>
        <label htmlFor="mail">Work email<input id="mail" name="email" type="email" required maxLength="160" placeholder="you@company.com" autoComplete="email"/></label>
        <p className="form-hp" aria-hidden="true"><label>Leave this empty<input name="website" tabIndex="-1" autoComplete="off"/></label></p>
        <button className="btn red" type="submit" disabled=${s==="sending"}>${s==="sending"?"Sending":"Get Your Visibility Audit"}</button>
        ${s==="error"&&o`<p className="form-flag" role="alert">That did not go through. Please try again, or email <a href="mailto:info@thesocialdm.com">info@thesocialdm.com</a>.</p>`}
      </form>`}
    </div>
  </section>`}function ya(){const e=U(null),s=U(null);return L(()=>{const a=()=>{if(!e.current||!s.current)return;s.current.style.fontSize="100px";const t=s.current.getBoundingClientRect().width;s.current.style.fontSize=100*e.current.clientWidth/t*.995+"px"};a(),document.fonts&&document.fonts.ready&&document.fonts.ready.then(a);const i=new ResizeObserver(a);return i.observe(e.current),()=>i.disconnect()},[]),o`<div className="giant" ref=${e} aria-hidden="true"><span className="giant-in" ref=${s}>L<span className="giant-pin"><span className="gr"></span><span className="gr b"></span><svg viewBox="0 0 24 34" preserveAspectRatio="xMidYMid meet"><path d="M12 0C5.4 0 0 5.4 0 12c0 8.6 12 22 12 22s12-13.4 12-22C24 5.4 18.6 0 12 0z" fill="#E22319"/><circle cx="12" cy="12" r="4.6" fill="#000"/></svg></span>calLift<sup>™</sup></span></div>`}function he(){return o`<${React.Fragment}><div className="sdm-band"><div className="wrap"><span>LocalLift is built and run by The SocialDM.</span><a className="btn ghost" href="https://www.thesocialdm.com/">Back to The SocialDM</a></div></div><footer className="foot"><div className="wrap">
    <div className="foot-grid">
      <div>
        <${fe} h=${36}/>
        <div><a className="by" href="https://www.thesocialdm.com/" target="_blank" rel="noopener"><img src=${Pe} alt=""/><span>Developed by The SocialDM.<br/>Visit thesocialdm.com</span></a></div>
      </div>
      <div><h3>LocalLift</h3><ul><li><a href="/#platform">Platform</a></li><li><a href="/#intelligence">Intelligence</a></li><li><a href="/#managed">Fully managed</a></li><li><a href="/#audit">Visibility audit</a></li></ul></div>
      <div><h3>Industries</h3><ul>${F.map(e=>o`<li key=${e.t}><a href=${X(e)}>${e.t}</a></li>`)}</ul></div>
      <div><h3>The SocialDM</h3><ul><li><a href="https://www.thesocialdm.com/about" target="_blank" rel="noopener">About</a></li><li><a href="https://www.thesocialdm.com/blog" target="_blank" rel="noopener">Market Intelligence</a></li><li><a href="https://www.thesocialdm.com/research-insights" target="_blank" rel="noopener">Research and Insights</a></li><li><a href="https://www.thesocialdm.com/contact" target="_blank" rel="noopener">Contact</a></li></ul></div>
    </div>
    <${ya}/>
    <div className="foot-base"><span>LocalLift™ by The SocialDM™. Phoenix, Arizona.</span><span>All maps, scores and sample businesses are illustrative.</span></div>
  </div></footer><//>`}function wa(){const[e,s]=g("Weekly Pulse");return o`<div><${te}/><main id="main"><${Ve}/><${_e}/><${Ue}/><${Qe} goTool=${i=>{s(i);const t=document.getElementById("intelligence");t&&t.scrollIntoView({behavior:A?"auto":"smooth"})}}/><${Ke} tool=${e} setTool=${s}/><${pa}/><${Ge}/><${ua}/><${va}/><${pe} items=${ue.Home}/><${me}/></main><${he}/></div>`}const fa={Multifamily:"multifamily","Build to Rent":"build-to-rent",Medical:"medical","Med Spa":"med-spa","Real Estate":"real-estate","Hair Salons":"hair-salons",Hospitality:"hospitality",Portfolios:"portfolios"};function X(e){return"/industries/"+fa[e.t]+"/"}const Re={Multifamily:{plural:"apartment communities",sample:"Sample community",h1:["Renters decide who to tour ","before they call."],sub:"LocalLift shows how your communities appear when renters search Google, scan Google Maps and ask AI assistants, then works to keep every property visible and accurate through lease up and beyond.",card:"Communities, lease ups and stabilized assets.",pains:[["Specials go stale online.","A concession ends on your website but lives on in your Google profile and in AI answers. Renters arrive expecting a price you no longer offer."],["Rank depends on the street.","A community can lead the map from its leasing office and vanish a mile away, right where your next renter works."],["AI builds the shortlist.","Renters ask AI assistants which communities allow large dogs or sit near the office. If you are not named, you are not toured."]],does:[["Market Survey","Every Sunday, competitor asking rents, effective rents and specials, side by side with yours."],["Map Reach","Weekly Google Maps rank across the neighborhoods your renters come from, not only from the leasing office."],["AI Shortlist","The renter questions that matter, asked every week, with the communities AI names instead of you."],["Site Read","Checks that your pricing, specials and pet policy read the same on your website, your Google profile and in AI answers."],["Review Desk","Resident review responses in your voice, written with fair housing in mind."],["Daily Presence","A Google post every day about your community, your neighborhood and what is happening this week."]]},"Build to Rent":{plural:"build to rent communities",sample:"Sample build to rent community",h1:["Renters want the yard. ","Help them find yours."],sub:"Build to rent is still new to many searchers. LocalLift helps Google and AI assistants explain your community clearly, so renters who want a house without buying one find you.",card:"Single family rental communities, from first phase to fully leased.",pains:[["The category needs explaining.","Many renters do not search for build to rent by name. They search for homes for rent with a yard, and your community has to show up for that."],["AI answers fill the gap.","When someone asks how build to rent differs from renting a house, the answer shapes who they tour. You want to be the example."],["Lease up moves fast.","New phases, new pricing and new amenities change often. Every listing has to keep up, or renters see last month's story."]],does:[["AI Shortlist","Weekly checks on whether AI assistants name your community for the questions renters actually ask."],["Site Read","Checks that phases, pricing and amenities read the same on your website, your Google profile and in AI answers."],["Map Reach","Google Maps rank across the neighborhoods and commute routes renters care about."],["Daily Presence","Daily Google posts that explain the community, the homes and the neighborhood in plain language."],["Market Survey","What nearby rentals and other communities are offering, every Sunday."],["Weekly Pulse","One page every Friday on what moved and the one next step for your lease up."]]},Medical:{plural:"medical practices",sample:"Sample practice",h1:["Patients check you ","before they call."],sub:"After a referral, many patients search the practice, compare ratings and ask AI who is well reviewed nearby. LocalLift helps keep your hours and locations accurate where patients look.",card:"Practices, specialists and groups with several locations.",pains:[["Details drift across listings.","Old hours, a moved suite or a retired provider can linger on Google and in AI answers, and patients call the wrong place."],["Reviews carry the decision.","Patients read how a practice answers reviews. Silence reads as neglect, and a careless reply can expose private details."],["Specialists compete street by street.","A patient searching from home sees a different list than one searching from the hospital campus."]],does:[["Site Read","Checks that hours, locations, providers and services match across your website, your Google profile and AI answers."],["Review Desk","Review responses in your voice that never confirm someone is a patient and never discuss care."],["AI Shortlist","Whether AI assistants name your practice when patients ask who is well reviewed for your specialty nearby."],["Map Reach","Google Maps rank across the neighborhoods your patients drive from."],["Snapshot","Your monthly Google report: searches, views, calls and direction requests."],["Weekly Pulse","One page every Friday, short enough to share with the practice manager."]]},"Med Spa":{plural:"med spas",sample:"Sample med spa",h1:["First time clients read everything. ","Make it worth reading."],sub:"Someone choosing a first treatment studies photos, reviews and every answer an AI assistant gives. LocalLift works to keep your med spa visible and current across all of it.",card:"Med spas, aesthetics studios and wellness clinics.",pains:[["Reputation is the product.","Clients choose the med spa that looks established. Thin photos and unanswered reviews send them to the name that looks busier."],["Offers change monthly.","Seasonal pricing and new treatments need to read the same on your website, your Google profile and in AI answers."],["Near work matters.","Many clients book close to the office, not home. Your map rank needs to hold where they spend the day."]],does:[["AI Shortlist","Whether AI assistants name your med spa when people ask who has the best reputation nearby."],["Review Desk","Thoughtful review responses in your voice, written with client privacy in mind."],["Daily Presence","Daily Google posts on treatments, aftercare tips, your team and seasonal care."],["Map Reach","Google Maps rank across the office districts and neighborhoods your clients come from."],["Site Read","Checks that treatments, pricing and offers match everywhere a client looks."],["Snapshot","Your monthly Google report: searches, views, calls and website clicks."]]},"Real Estate":{plural:"real estate agents",sample:"Sample agent",h1:["Sellers pick the agent ","who looks current."],sub:"Before a homeowner calls, they search your name, read your reviews and ask AI who knows their part of town. LocalLift helps make sure the answer includes you.",card:"Agents, teams and brokerages.",pains:[["Activity signals expertise.","A Google profile with no recent posts looks retired, even when your calendar is full."],["Neighborhoods are the battleground.","Sellers want the agent who knows their streets. Your visibility has to hold neighborhood by neighborhood."],["AI names a few agents.","When a homeowner asks who the best listing agent nearby is, a short list forms in seconds."]],does:[["AI Shortlist","Whether AI assistants name you when homeowners ask who knows their neighborhood best."],["Map Reach","Google Maps rank across every neighborhood you want listings from."],["Review Desk","Client review responses in your voice, so every reply adds to your reputation."],["Daily Presence","Daily Google posts on listings, sales, market notes and the neighborhoods you serve."],["Snapshot","Your monthly Google report: profile views, calls and website clicks."],["Weekly Pulse","One page every Friday on what moved and the one next step."]]},"Hair Salons":{plural:"hair salons",sample:"Sample salon",h1:["New neighbors need a salon ","by Saturday."],sub:"People new to the area search, scan photos and check hours on their phone, then book the salon that looks open and active. LocalLift works to keep your salon in that first look.",card:"Salons, barbers and independent stylists.",pains:[["Hours decide the booking.","If Saturday hours are wrong anywhere, a ready client books somewhere else."],["Photos do the selling.","Searchers judge the work before they read a word. Fresh photos and recent posts show the chairs are full."],["Specialties get asked about.","People ask AI assistants which salon is best with curly hair or color correction nearby. You want to be named for what you do best."]],does:[["Map Reach","Google Maps rank across the neighborhoods around your salon, street by street."],["Review Desk","Review responses in your voice, so happy clients feel thanked and new ones see you care."],["Daily Presence","Daily Google posts on cuts, color, your stylists and seasonal looks."],["Snapshot","Your monthly Google report: searches, calls and direction requests."],["AI Shortlist","Whether AI assistants name your salon for the specialties you are known for."],["Site Read","Checks that hours, services and prices match everywhere."]]},Hospitality:{plural:"hotels and stays",sample:"Sample hotel",h1:["Travelers plan the trip ","in an AI answer."],sub:"Guests ask which stay fits a quiet weekend, check the walk to dinner on Google Maps, then book the place that kept appearing. LocalLift works to keep your property in that answer.",card:"Boutique hotels, inns and short stay properties.",pains:[["Booking sites own the first click.","Your own Google profile and website need to give travelers a reason to book with you directly."],["Every trip has a reason.","Anniversaries, conferences, game weekends. AI answers match stays to reasons, and you want to match more of them."],["Recent beats beautiful.","Travelers trust recent photos and recent replies over polished pictures from three years ago."]],does:[["AI Shortlist","Whether AI assistants recommend your property for the trips travelers describe."],["Review Desk","Guest review responses in your voice, posted promptly."],["Snapshot","Your monthly Google report: searches, views, calls and website clicks."],["Daily Presence","Daily Google posts on rooms, dining, events and what is happening nearby."],["Map Reach","Google Maps rank from the places guests start their search: the station, the stadium, the old town."],["Site Read","Checks that amenities, policies and rates read the same everywhere."]]},Portfolios:{plural:"portfolios",sample:"Sample portfolio",h1:["One clear read ","on every property."],sub:"Owners and operators see every property side by side, on the same measures, with one recommended move for each. LocalLift turns a stack of reports into one decision.",card:"Owners, operators and asset managers.",pains:[["Every site reports differently.","Different vendors and different measures make properties hard to compare, and the weakest one hides."],["Problems surface late.","A property can slip behind its local competitors for weeks before occupancy or leads show it."],["Attention is limited.","You cannot fix everything at once. You need to know which move counts most this week."]],does:[["Lift Score","The same score on every property, so you can see which are getting easier to find and which are slipping."],["Weekly Pulse","One page per property every Friday, with one recommended next step for each."],["Market Survey","Competitor pricing and specials around every property, every Sunday."],["AI Shortlist","Which properties AI assistants name, and which they skip."],["Snapshot","Monthly Google results for every property, in one consistent format."],["ClearView","Monthly social results across the portfolio: what posted, what performed, what changes next."]]}};function ga({d:e}){const[s,a,i]=E(.15),t=e.labels||De;return o`<div ref=${s}>
      <p className="journey-who">${e.who}</p>
      <div className="journey">
        <div className="track"><span className="traveler"></span></div>
        ${e.s.map((n,d)=>o`<div className="j-step" key=${d}><h3>${t[d]}</h3><p>${n}</p></div>`)}
      </div>
      <div className="ia">
        <div>
          ${e.doors?o`<div className="ia-city">Multifamily doors we work across</div><div className="ia-big"><i className="live-dot"></i><span><${J}/>+</span></div><div className="ia-sub">doors and counting</div>`:o`<div className="ia-big"><${P} to=${+e.big[0]} run=${a}/></div><div className="ia-sub">${e.big[1]}</div>`}
          ${e.doors?o`<div className="ia-city" style=${{margin:"20px 0 -6px"}}>Sample figures</div>`:null}<div className="ia-stats">${e.stats.map(n=>o`<div key=${n[1]}><strong>${n[0]}</strong><span>${n[1]}</span></div>`)}</div>
        </div>
        <div>
          <div className="ia-city">${e.city}. Fake numbers.</div>
          <div className="viz" style=${{marginTop:0}}>
            <${se} items=${e.pops} run=${i}/>
            <div className="viz-t">${e.metric}</div>
            <${re} data=${e.d} labels=${e.labels2||Te} run=${a} name=${e.metric} height=${210} hi=${e.labels2?e.d.indexOf(Math.max(...e.d)):null}/>
          </div>
        </div>
      </div>
      <div className="sample" style=${{marginTop:"14px"}}>Sample journey, sample place and sample charts. Illustrative only.${e.doors?" The door count is real.":""}</div>
  </div>`}function $a({d:e,c:s}){const a=s.does.map(c=>c[0]),[i,t]=g(a[0]),n=q.find(c=>c.n===i),d=s.does.find(c=>c[0]===i);return o`<div className="console" style=${{marginTop:"40px"}}>
      <div className="console-bar"><span>LocalLift Intelligence / ${s.sample}</span><span>Illustrative panels. A separate sample from the chart above.</span></div>
      <div className="console-body">
        <div className="rail" role="group" aria-label="LocalLift tools">
          ${a.map(c=>{const r=q.find(m=>m.n===c);return o`<button key=${c} aria-pressed=${c===i} onClick=${()=>t(c)}><span>${c}</span><small>${r.c}</small></button>`})}
        </div>
        <div className="panel fade" key=${i}>
          <div className="panel-head"><h3>${n.n}</h3><span className="sample">${n.c}</span></div>
          <p className="panel-desc">${d[1]}</p>
          <div className="panel-body">${n.b({ind:!0})}</div>
        </div>
      </div>
    </div>`}function pe({items:e,dark:s}){return!e||!e.length?null:o`<section className=${"band "+(s?"char":"white")} id="faq"><div className="wrap faq-wrap">
    <div><${M}>Questions<//><h2 className="title">Answers, <em>before you ask.</em></h2></div>
    <div className="faq">${e.map((a,i)=>o`<details key=${i} open=${i===0}><summary>${a[0]}</summary><p>${a[1]}</p></details>`)}</div>
  </div></section>`}function ba({name:e}){const s=F.find(i=>i.t===e),a=Re[e];return o`<div><${te}/><main id="main">
    <section className="hero ind-hero"><${oe}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><a href="/industries/">Industries</a><span>/</span><span aria-current="page">${e}</span></nav>
        <h1>${a.h1[0]}<em>${a.h1[1]}</em></h1>
        <p className="sub">${a.sub}</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a><a className="btn ghost" href="#journey">See the journey</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <div className="statement"><div className="wrap statement-in"><span>Be found.</span><span>Be understood.</span><span>Be chosen.</span>${s.doors?o`<${qe}/>`:null}</div></div>
    <section className="band char"><div className="wrap">
      <${M}>The visibility problem for ${a.plural}<//>
      <h2 className="title" style=${{maxWidth:"16em"}}>${e==="Portfolios"?"Where a portfolio loses sight, ":"Where the customer slips away, "}<em>and why.</em></h2>
      <div className="pains">${a.pains.map((i,t)=>o`<article className="pain" key=${t}><b>0${t+1}</b><h3>${i[0]}</h3><p>${i[1]}</p></article>`)}</div>
    </div></section>
    <section className="band white" id="journey"><div className="wrap">
      <${M}>The customer journey<//>
      <h2 className="title" style=${{maxWidth:"15em"}}>${e==="Portfolios"?"Four moments ":"Four moments decide "}<em>${e==="Portfolios"?"shape the decision.":"who gets chosen."}</em></h2>
      <${ga} d=${s}/>
    </div></section>
    <section className="band mist" id="intelligence"><div className="wrap">
      <${M}>What LocalLift does for ${a.plural}<//>
      <h2 className="title" style=${{maxWidth:"15em"}}>The tools that matter here, <em>run for you.</em></h2>
      <p className="lede">We run the tools and tell you what they mean. You get the answer and one next step, not another login.</p>
      <div className="does">${a.does.map(i=>{const t=q.find(n=>n.n===i[0]);return o`<div className="do" key=${i[0]}><small>${t.c}</small><h3>${i[0]}</h3><p>${i[1]}</p></div>`})}</div>
      <${$a} d=${s} c=${a}/>
    </div></section>
    <${pe} items=${ue[e]}/>
    <section className="band white" style=${{paddingTop:0}}><div className="wrap">
      <${M}>Other industries<//>
      <div className="others">${F.filter(i=>i.t!==e).map(i=>o`<a key=${i.t} href=${X(i)}>${i.t}</a>`)}</div>
    </div></section>
    <${me} industry=${e}/>
  </main><${he}/></div>`}function ka(){return o`<div><${te}/><main id="main">
    <section className="hero ind-hero"><${oe}/>
      <div className="wrap hero-in">
        <nav className="crumbs" aria-label="Breadcrumb"><a href="/">LocalLift</a><span>/</span><span aria-current="page">Industries</span></nav>
        <h1>Built for businesses people <em>search for nearby.</em></h1>
        <p className="sub">Every customer takes a different path to the same decision. LocalLift follows that path across Google Search, Google Maps and AI answers for eight kinds of local business.</p>
        <div className="cta-row"><a className="btn red" href="#audit">Get Your Visibility Audit</a></div>
      </div>
      <div className="sample hero-cap">Illustrative map</div>
    </section>
    <section className="band white"><div className="wrap">
      <${M}>Choose your industry<//>
      <h2 className="title">Eight industries. <em>One loop.</em></h2>
      <div className="ind-cards">${F.map(e=>o`<a className="card" key=${e.t} href=${X(e)}><span className="sample">Industry</span><h3>${e.t}</h3><p>${Re[e.t].card}</p><em>See LocalLift for ${e.t}</em></a>`)}</div>
    </div></section>
    <${Ge}/>
    <${pe} items=${ue.Industries} dark=${!0}/>
    <${me}/>
  </main><${he}/></div>`}const ue={Home:[["What is LocalLift?","LocalLift is a local visibility service from The SocialDM. We show how your business appears across Google Search, Google Maps and AI answers, then do the work to strengthen it: daily Google posts, review responses, content and weekly reporting."],["How do you know what AI assistants say about my business?","Every week we ask the leading AI assistants the questions your customers ask, and record who gets named. You see where you appear, where you do not, and who is named instead."],["Do I need to learn a new platform?","No. There is no dashboard to log in to. Our team runs the tools and sends written reports you can read in minutes and forward to ownership."],["What do I receive each week?","A Weekly Pulse every Friday with one recommended next step, plus weekly reads on your map rank, AI answers and listing accuracy. Snapshot and ClearView reports arrive monthly."],["Does LocalLift replace my website or my ads?","No. LocalLift works alongside them. It strengthens how you appear in organic search, on Google Maps and in AI answers, where many local decisions start."],["Are the numbers on this site real?","The door count, the weekly post count and the case study are real. Every number, chart, business and city in the samples is made up to show what our reports look like."],["How do I get started?","Request a Visibility Audit with the form on this page. A real person replies within one business day."]],Industries:[["Which industries does LocalLift work with?","Multifamily, build to rent, medical practices, med spas, real estate agents, hair salons, hospitality and portfolios of many properties."],["Is the service different for each industry?","The loop is the same: discover, compare, strengthen and measure. The questions we track, the competitors we watch and the content we write change for each industry."],["My industry is not listed. Can you still help?","If customers search for you nearby, the same approach applies. Contact The SocialDM and we will tell you honestly whether LocalLift fits."],["Do you work with groups and multi location businesses?","Yes. Portfolio reporting puts every location side by side on the same measures, with one recommended move for each."]],Multifamily:[["How does LocalLift help apartment communities?","We track how renters find your community on Google Search, Google Maps and AI answers, correct or flag what is wrong or out of date, and keep your Google presence active every day. Every Friday you get one page on what moved and one next step."],["Do you track competitor rents and specials?","Yes. Market Survey compares asking rents, effective rents and specials at your competitors every Sunday, side by side with yours."],["Are review responses written with fair housing in mind?","Yes. Every response is written in your voice, stays neutral and never references a protected characteristic or a resident's personal details."],["Do you work with lease ups as well as stabilized communities?","Yes. Lease ups need visibility fast and change often. Stabilized communities need to hold their place against newer competitors. The weekly loop covers both."],["How large is your multifamily portfolio?","LocalLift works across more than 7,900 doors, and counting."]],"Build to Rent":[["What makes build to rent visibility different?","Many renters do not yet search for build to rent by name. Your community has to appear for the searches they do make, like homes for rent with a yard, and be explained clearly when they ask AI assistants."],["Do you support communities still in lease up?","Yes. We keep phases, pricing and amenities current on your Google profile, flag what needs changing on your website, and track what AI answers say."],["Can you control what AI assistants say about us?","No one can control AI answers directly. We track what they say every week, work to correct the sources they draw on, and publish clear content so the answers improve over time."],["Do you track nearby rentals and other communities?","Yes. Market Survey watches nearby offers every Sunday so you know what renters are comparing you with."]],Medical:[["Is your review response process safe for patient privacy?","Responses never confirm that someone is a patient and never discuss care. We do not need access to patient records."],["Can you fix wrong hours, addresses or provider details?","Yes. Site Read checks your details across your website, your Google profile and AI answers every week, and we correct or flag what is out of date."],["Do you work with practices that have several locations?","Yes. Each location is tracked on its own, and portfolio reporting shows every location side by side."],["Will this replace our website or patient marketing?","No. LocalLift works alongside them and focuses on how patients find and judge your practice before they call."]],"Med Spa":[["How do you help a med spa get recommended by AI assistants?","We track the questions clients ask every week, see which med spas are named, and strengthen the reviews, posts and details AI answers draw on."],["Can you promote our monthly offers?","Yes. Current offers run as separate Google offer posts, and Site Read checks that the offer reads the same everywhere."],["Do your posts make claims about treatment results?","No. Posts and review replies stay factual, avoid promising outcomes and respect client privacy."],["How soon will we see changes?","Some fixes, like correct hours or a current offer, show within days. Map rank and AI answers move over weeks, which is why we report every week."]],"Real Estate":[["Do you work with individual agents or teams?","Both. LocalLift works for a single agent, a team or a brokerage with many profiles."],["Can you help me show up in specific neighborhoods?","Yes. Map Reach measures your Google Maps rank across the neighborhoods you choose, and your posts and content are written for those same areas."],["Do I need to write the posts myself?","No. We write and publish daily Google posts on your listings, sales and market notes. You can review them whenever you like."],["How do you handle client reviews?","Review Desk answers reviews in your voice, so each reply adds to your reputation instead of sitting unanswered."]],"Hair Salons":[["Does LocalLift work for a single salon?","Yes. LocalLift runs for you, so one salon gets the same weekly work without adding to the front desk."],["Do you need our photos?","Your own photos work best. Share them with us and we will put them to work in your daily Google posts."],["How do you handle a negative review?","Calmly and in your voice. We thank the client, acknowledge the concern and invite them to talk with you directly."],["Will our hours and services stay correct online?","Site Read checks hours, services and prices across your website, your Google profile and AI answers every week, and we fix or flag what we find."]],Hospitality:[["Can LocalLift help us earn more direct bookings?","We strengthen your own Google profile and website so travelers have a reason to book with you directly, and we report the calls and website clicks that come from Google."],["How do you respond to guest reviews?","In your voice, and promptly. Thoughtful replies show future guests that someone is paying attention."],["Do you track how AI assistants recommend hotels?","Yes. Every week we ask the trip questions your guests ask and record which properties are named."],["Do you work with groups of properties?","Yes. Portfolio reporting shows every property side by side on the same measures."]],Portfolios:[["How do you compare properties in different markets?","Each property is measured against its own local market, then scored on the same Lift Score, so a portfolio view is a fair comparison."],["Can ownership read the reports directly?","Yes. Every report is written to be read in minutes and forwarded as it is."],["How many properties can you cover?","From a handful to a full portfolio. Each property gets the same weekly read and one recommended move."],["Do property teams need to change how they work?","No. There is no new login. Teams receive one clear next step each week, and our team does the visibility work."]]},Fe={home:wa,industries:ka};F.forEach(e=>{Fe["ind:"+e.t]=()=>o`<${ba} name=${e.t}/>`});var ve=Fe[window.__PAGE__],Ee=document.getElementById("root");ve&&(A?ReactDOM.createRoot(Ee).render(React.createElement(ve)):ReactDOM.hydrateRoot(Ee,React.createElement(ve)))})();
