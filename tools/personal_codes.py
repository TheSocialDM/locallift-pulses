"""Personal access codes for a LocalLift Live property app.
Patches the gate in live/<app>/v3/index.html so access works with:
  - personal links ?p=<code>&n=<Name> (hash sha256('<salt>:p:'+code) must be in live/<app>/access.json "staff")
  - the old team invite/code, until access.json "staffOnly" is true
Removed people lose access on their next open or within 5 minutes.
access.json "notes" shows a one time message to everyone or to chosen people.
Usage: python3 tools/personal_codes.py live/montage-r8x2 montage ll-"""
import sys,re
app,salt,pre=sys.argv[1],sys.argv[2],sys.argv[3]
p=app+'/v3/index.html';s=open(p).read()
if 'const PQ=' in s and "sha('"+salt+":p:'" in s:
    print('already patched for salt',salt);sys.exit(0)
start=s.index("fetch('../data.json?t='+Date.now(),{cache:'no-store'}).then(r=>r.json()).then(j=>{window.__llHash")
end=s.index("document.addEventListener('submit',async e=>{if(e.target.id!=='gf')return;",start)
new=r"""const PQ=(()=>{try{return (new URLSearchParams(location.search).get('p')||'').replace(/[^a-f0-9]/gi,'').toLowerCase()}catch(x){return ''}})();
const getAcc=()=>fetch('../access.json?t='+Date.now(),{cache:'no-store'}).then(r=>{if(!r.ok)throw 0;return r.json()});
const okH=(h,team,acc)=>!!h&&((!!team&&h===team&&!acc.staffOnly)||(acc.staff||[]).indexOf(h)>-1);
const lockOut=()=>{try{WIPE.concat([K]).forEach(k=>localStorage.removeItem(k))}catch(x){};shut('This phone no longer has access to LocalLift Live. If that is a mistake, ask your manager for a new link.')};
const showNote=(h,acc)=>{try{const L=(acc.notes||[]).filter(n=>n&&n.id&&(n.to==='all'||(Array.isArray(n.to)&&n.to.indexOf(h)>-1))&&(!n.until||new Date().toISOString().slice(0,10)<=n.until)&&!get('__PRE__note-'+n.id));if(!L.length)return;const n=L[0];const d=document.createElement('div');d.id='llnote';d.setAttribute('role','dialog');d.innerHTML='<div class="nbx"><p class="nk">Message from The SocialDM</p><h3></h3><p class="nb"></p><button type="button">Got it</button></div>';d.querySelector('h3').textContent=n.title||'';d.querySelector('.nb').textContent=n.body||'';d.querySelector('button').onclick=()=>{try{localStorage.setItem('__PRE__note-'+n.id,'1')}catch(x){};d.remove()};const st=document.createElement('style');st.textContent='#llnote{position:fixed;inset:0;z-index:60;background:rgba(0,0,0,.45);display:flex;align-items:flex-end;justify-content:center;font-family:-apple-system,system-ui,sans-serif}#llnote .nbx{background:#fff;color:#1c1c1e;width:100%;max-width:520px;border-radius:22px 22px 0 0;padding:22px 22px 28px;box-sizing:border-box}#llnote .nk{margin:0;font:600 12px/1 -apple-system,system-ui,sans-serif;letter-spacing:.6px;text-transform:uppercase;color:#1a73e8}#llnote h3{margin:8px 0 6px;font:700 21px/1.25 -apple-system,system-ui,sans-serif}#llnote .nb{margin:0 0 18px;font:400 16px/1.45 -apple-system,system-ui,sans-serif;color:#3a3a3c;white-space:pre-line}#llnote button{width:100%;min-height:48px;border:0;border-radius:14px;background:#1a73e8;color:#fff;font:700 16px -apple-system,system-ui,sans-serif}@media(prefers-color-scheme:dark){#llnote .nbx{background:#1c1c1e;color:#fff}#llnote .nb{color:#d1d1d6}}';document.head.appendChild(st);document.body.appendChild(d)}catch(x){}};
Promise.all([fetch('../data.json?t='+Date.now(),{cache:'no-store'}).then(r=>r.json()),getAcc().catch(()=>({}))]).then(async([j,acc])=>{window.__llHash=j.teamCodeHash||null;window.__llAcc=acc;const have=get(K);
 if(!window.__llHash&&!(acc.staff||[]).length){open_();return}
 const q=new URLSearchParams(location.search),nm=(q.get('n')||'').replace(/[^A-Za-z' ]/g,'').slice(0,20);
 if(PQ.length>=10){const h=await sha('__SALT__:p:'+PQ);if((acc.staff||[]).indexOf(h)>-1){try{localStorage.setItem(K,h);if(nm&&!get('__PRE__me'))localStorage.setItem('__PRE__me',nm)}catch(x){}if(have!==h){try{localStorage.setItem('__PRE__invited','1')}catch(x){};location.reload();return}open_();showNote(h,acc);return}}
 try{const inv=q.get('invite');if(!acc.staffOnly&&inv&&inv.length>=16&&window.__llHash&&window.__llHash.indexOf(inv)===0){localStorage.setItem(K,window.__llHash);if(nm&&!get('__PRE__me'))localStorage.setItem('__PRE__me',nm);if(have!==window.__llHash){try{localStorage.setItem('__PRE__invited','1')}catch(x){};location.reload();return}open_();showNote(window.__llHash,acc);return}}catch(x){}
 if(okH(have,window.__llHash,acc)){open_();showNote(have,acc);return}
 if(have)lockOut();else shut()
}).catch(()=>{if(get(K))open_();else shut('Connect to the internet to sign in.')});
const reCheck=()=>{const have=get(K);if(!have||document.visibilityState!=='visible')return;Promise.all([fetch('../data.json?t='+Date.now(),{cache:'no-store'}).then(r=>r.json()),getAcc()]).then(([j,acc])=>{window.__llAcc=acc;if(!okH(have,j.teamCodeHash||null,acc))lockOut()}).catch(()=>{})};
setInterval(reCheck,300000);document.addEventListener('visibilitychange',reCheck);
"""
new=new.replace('__PRE__',pre).replace('__SALT__',salt)
s=s[:start]+new+s[end:]
# manual code form: also accept a personal code
old="const h=await sha('"+salt+":'+c);if(h===window.__llHash){"
assert s.count(old)==1,old
s=s.replace(old,"const h0=await sha('"+salt+":'+c),hp=await sha('"+salt+":p:'+c.toLowerCase()),A=window.__llAcc||{},h=((A.staff||[]).indexOf(hp)>-1)?hp:h0;if((h===h0&&h0===window.__llHash&&!A.staffOnly)||h===hp){")
# manifest for personal links too
s=s.replace("if(q0.get('invite')){const base=","if(q0.get('invite')||q0.get('p')){const base=",1)
open(p,'w').write(s);print('ok')
