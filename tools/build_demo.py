"""Build the prospect demo (live/<app>/demo/) from the real staff app (v3).
Nothing in the demo sends: no gate, no analytics, no activity alerts, no uploads,
separate lldemo- storage, resident names hidden, deep links (#kit #tour ...) kept.
Usage: python3 tools/build_demo.py live/montage-r8x2   (or live/stillwater-k4p7)"""
import re,sys,pathlib
app=pathlib.Path(sys.argv[1]); s=(app/'v3/index.html').read_text()
PRE=re.search(r"const K='([a-z]+)-team'",s).group(1)   # ll (Montage) or llsw (Stillwater)
DPRE={'ll':'lldemo'}.get(PRE,PRE+'demo')   # separate demo storage per property
HINTBG='rgba(28,20,14,.92)' if PRE=='ll' else 'rgba(10,29,34,.92)'
HINTBG={'coya-3zep':'rgba(46,29,30,.92)','fora-50r1':'rgba(31,31,32,.92)'}.get(app.name,HINTBG)   # property tint for the swipe hint
def must(old,new,count=1):
    global s
    assert old in s, 'missing: '+old[:70]; s=s.replace(old,new,count)
s,_n=re.subn(r'<title>(LocalLift Live · [^<]*)</title>',r'<meta name="robots" content="noindex">\n<title>\1 · live demo</title>',s,count=1);assert _n==1
s=re.sub(r'<link rel="manifest"[^>]*>\s*','',s)
s=re.sub(r'<meta name="(apple-mobile-web-app-capable|mobile-web-app-capable|apple-mobile-web-app-title)"[^>]*>\s*','',s)
s=re.sub(r'<link rel="apple-touch-icon"[^>]*>\s*','',s)
must('<body class="gated">','<body>')
s=re.sub(r'<div id="gate">.*?</div>\s*(?=<script>)','',s,count=1,flags=re.S)
s=re.sub(r"<script>\s*\(function\(\)\{\s*const K='"+PRE+r"-team'.*?</script>\s*",'',s,count=1,flags=re.S)
assert PRE+'-team' not in s
s=re.sub(r'<script async src="https://www.googletagmanager.com/gtag/js[^"]*"></script>\s*','',s)
s=s.replace("gtag('config','G-FC39M4P67G',{send_page_view:false});","")
s=re.sub(r"(['\"`])"+PRE+"-",r"\g<1>"+DPRE+"-",s)
s=re.sub(r'class="pv">[^<]*','class="pv">Live demo · Tap anything. Nothing here posts, uploads or sends on its own.',s,count=1)
must("fetch(SNAPHOOK,{method:'POST',mode:'no-cors',body:fd});","await new Promise(r=>setTimeout(r,700));")
must("const vidPost=(a)=>fetch(VIDHOOK,{method:'POST',body:new URLSearchParams(a)});","const vidPost=(a)=>Promise.resolve({json:()=>Promise.resolve({link:'demo'})});")
s=re.sub(r"await new Promise\(\(res,rej\)=>\{const x=new XMLHttpRequest\(\);x\.open\('POST',j\.link\).*?x\.send\(f\)\}\);",
 "for(let p=10;p<=100;p+=15){b.textContent='Sending... '+p+'%';await new Promise(r=>setTimeout(r,160))}",s,count=1,flags=re.S)
assert 'x.open(' not in s
# activity alert script -> swipe hint
hint=r'''<div id="sch" aria-hidden="true" style="position:fixed;left:50%;bottom:calc(150px + env(safe-area-inset-bottom));transform:translateX(-50%);z-index:60;display:flex;align-items:center;gap:8px;background:'''+HINTBG+r''';color:#fff;border-radius:99px;padding:9px 16px 9px 12px;font:700 14px/1.2 -apple-system,system-ui,sans-serif;white-space:nowrap;box-shadow:0 10px 26px rgba(0,0,0,.35);pointer-events:none;opacity:0;transition:opacity .35s">Swipe up for more ↓</div>
<script>
(function(){const H=document.getElementById('sch');let used=false,last=null;
const tgt=()=>{const sh=document.getElementById('sh'),b=document.getElementById('box');return(sh&&sh.classList.contains('on')&&b)?b:document.scrollingElement};
const more=t=>t.scrollHeight-t.clientHeight-t.scrollTop>80;
const check=()=>{const t=tgt();if(t!==last){last=t;used=false}H.style.opacity=(!used&&more(t))?1:0};
document.addEventListener('scroll',e=>{const t=tgt();if((e.target===t||(t===document.scrollingElement&&e.target===document))&&t.scrollTop>30){used=true;H.style.opacity=0}},true);
const mo=new MutationObserver(()=>{last=tgt();used=false;setTimeout(check,350)});
const start=()=>{['sh','box','view'].forEach(id=>{const el=document.getElementById(id);if(el)mo.observe(el,{childList:true,attributes:id==='sh',attributeFilter:id==='sh'?['class']:undefined})});setTimeout(check,900)};
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();window.addEventListener('resize',check)})();
</script>'''
n0=len(s)
s=re.sub(r"<script>\s*\(function\(\)\{\s*const HOOK='https://hook\.us2\.make\.com/484kbydspt3pewlyjq42utapf29y50mx'.*?</script>",lambda m:hint,s,count=1,flags=re.S)
assert '484kbydspt3pewlyjq42utapf29y50mx' not in s
# demo data: hide resident names and review cards, plus deep links
dl=r'''const DL=h=>{if(!h)return;try{close()}catch(e){};const nav=v=>{const b=document.querySelector('nav button[data-v='+v+']');if(b)b.click()};const clk=q=>{const b=document.querySelector(q);if(b)b.click()};const later=f=>setTimeout(f,150);
if(h==='today')nav('today');else if(h==='kit'){nav('tourv');later(()=>clk('#bKit'))}else if(h==='tour'){nav('tourv');later(()=>clk(document.querySelector('#bTour2')?'#bTour2':'#bTour'))}else if(h==='reviews')nav('reviews');
else if(['movein','renew','work','event'].includes(h)){nav('reviews');later(()=>clk('[data-m='+h+']'))}else if(h==='qr'){nav('reviews');later(()=>{clk('[data-m=movein]');later(()=>clk('#qr'))})}
else if(h==='snap'){nav('social');later(()=>clk('#bCap'))}else if(h==='shoot'){nav('social');later(()=>{const e=document.getElementById('hold');if(e)e.scrollIntoView({block:'start'})})}
else if(h==='desk'){nav('tourv');later(()=>clk('#bDesk'))}else if(h==='rivals')nav('tourv');else if(h==='card'){later(()=>clk('#mcBtn'))}else if(h==='alert'){nav('today');later(()=>{try{raShow(true)}catch(e){}})}};
window.addEventListener('hashchange',()=>DL(location.hash.slice(1)));setTimeout(()=>DL(location.hash.slice(1)),1500);
'''
must("fetch('../data.json?t='+Date.now(),{cache:'no-store'}).then(r=>r.json()).then(j=>{D=j",
 dl+"fetch('../data.json?t='+Date.now(),{cache:'no-store'}).then(r=>r.json()).then(j=>{const bad=x=>/review|resident|\\b[A-Z][a-z]+ [A-Z]\\.|star/i.test(JSON.stringify(x));if(j.feed)j.feed=j.feed.filter(x=>!(x.src||'').match(/review/i)&&!bad(x));if(j.followups)j.followups=j.followups.filter(x=>!bad(x));if(j.team){j.team.shoutouts=[]};D=j")
# no self reload on version change
s=s.replace("fetch('version.txt?t='","fetch('no-version.txt?t='")
s=re.sub(r"const (SNAPHOOK|VIDHOOK)='[^']*';",r"const \1='';",s)
assert 'hook.us2.make.com' not in s and 'fetch(SNAPHOOK' not in s and 'fetch(VIDHOOK' not in s
# live "Or send from my own phone" opens Messages; the demo keeps the practice message (nothing sends)
s=s.replace("/*llsendlive*/location.href='sms:?&body='+encodeURIComponent(txt());box.innerHTML='<h3>Opening Messages</h3><p>Your text is filled in. Tap Send in Messages.</p>","box.innerHTML='<h3>Ready to send</h3><p>In the live app this opens your phone\\'s Messages with the text filled in, and you tap Send. This preview does not open Messages.</p>")
(app/'demo/index.html').write_text(s)
print('demo built', len(s))
