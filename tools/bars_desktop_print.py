"""Blue metric bars on the leads table, 'Use it on your computer' card, Print or save as PDF (Nov 24 2026)."""
import re,pathlib
p=pathlib.Path('live/montage-r8x2/v3/index.html'); v=p.read_text()
old="const rows=k=>k.t==='rivals'?tbl(HX.rvh,HX.rv):k.t==='src'?tbl(HX.srh,HX.sr):'';"
assert old in v
v=v.replace(old,r"""const numv=s=>+String(s).replace(/[^\d.]/g,'')||0;
const barT=(h,r)=>{const mx=Math.max(1,...r.map(x=>numv(x[1])));return '<div class="akbar"><div class="abh"><span>'+h[0]+'</span><span>'+h[1]+'</span><span>'+h[2]+'</span></div>'+r.map(x=>`<div class="abr"><div class="abt"><span class="abn">${x[0]}</span><span class="abv">${x[1]}</span><span class="abl${numv(x[2])?'':' z'}">${x[2]}</span></div><i style="width:${Math.max(4,Math.round(numv(x[1])/mx*100))}%"></i></div>`).join('')+'</div>'};
const rows=k=>k.t==='rivals'?tbl(HX.rvh,HX.rv):k.t==='src'?barT(HX.srh,HX.sr):'';""")
# desktop + print card
js=r"""
const deskLink=()=>{let n='';try{n=localStorage.getItem('ll-me')||''}catch(e){};const h=(typeof D!=='undefined'&&D&&D.teamCodeHash)||'';return 'https://live.thesocialdm.com/montage'+(h?('?invite='+h.slice(0,16)+(n?'&n='+encodeURIComponent(n):'')):'')};
const deskCard=()=>`<section class="w dsk"><div class="dskh"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg><div><b>Use it on your computer too</b><small>Same app on the leasing desk computer. Open the link, then bookmark it.</small></div></div><div class="dskb"><button data-dsk="mail">Email me the link</button><button data-dsk="copy">Copy link</button><button data-dsk="print">Print or save PDF</button></div></section>`;
document.addEventListener('click',e=>{const b=e.target.closest('[data-dsk]');if(!b)return;const k=b.dataset.dsk,l=deskLink();
 if(k==='print'){window.print();return}
 if(k==='copy'){(navigator.clipboard?navigator.clipboard.writeText(l):Promise.reject()).then(()=>{b.textContent='Copied'},()=>{prompt('Copy this link',l)});setTimeout(()=>b.textContent='Copy link',2000);return}
 if(k==='mail'){let m='';try{m=localStorage.getItem('ll-deskmail')||''}catch(x){};location.href='mailto:'+encodeURIComponent(m)+'?subject='+encodeURIComponent('LocalLift Live on my computer')+'&body='+encodeURIComponent('Open this on your work computer, then bookmark it:\n'+l)}});
"""
anchor="document.addEventListener('click',e=>{try{if(e.target.closest('#raOk'))"
i=v.index(anchor); j=v.index('\n}\n</script>',i); v=v[:j]+'\n'+js+v[j:]
# place card at the bottom of More (Help stays where it is) and on Market
v=v.replace("V.score()+V.rivals(),","V.score()+V.rivals()+deskCard(),",1)
assert 'V.rivals()+deskCard(),' in v
v=v.replace("V.market=()=>`<div class=\"lt\">Market</div>`+askBox()+HX.cards.map(card).join('')+V.rivals();","V.market=()=>`<div class=\"lt\">Market<button class=\"prt\" data-dsk=\"print\" aria-label=\"Print or save as PDF\"><svg viewBox=\"0 0 24 24\"><path d=\"M7 9V4h10v5M7 17H5a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v4a2 2 0 0 1-2 2h-2\"/><rect x=\"7\" y=\"14\" width=\"10\" height=\"6\" rx=\"1\"/></svg>Print</button></div>`+askBox()+HX.cards.map(card).join('')+V.rivals()+deskCard();",1)
assert 'class=\"prt\"' in v
css='''
/* ===== metric bars, desktop and print (Nov 24 2026) ===== */
.akbar{display:grid;gap:12px;margin-top:6px}
.abh{display:grid;grid-template-columns:1fr 64px 52px;font-size:12.5px;color:#86868b;font-weight:600}
.abh span:nth-child(n+2),.abt span:nth-child(n+2){text-align:right}
.abr{display:grid;gap:6px}
.abt{display:grid;grid-template-columns:1fr 64px 52px;align-items:baseline;font-size:16px;color:#1d1d1f}
.abv{font-variant-numeric:tabular-nums}.abl{font-weight:800;font-variant-numeric:tabular-nums;color:#1a73e8}.abl.z{color:#a1a1a6;font-weight:600}
.abr i{display:block;height:8px;border-radius:99px;background:linear-gradient(90deg,#1a73e8,#4c8df6)}
.lt .prt{float:right;display:inline-flex;align-items:center;gap:6px;margin-top:6px;border:0;border-radius:99px;background:#eef4fe;color:#1a5fd0;font:700 14px -apple-system,system-ui,sans-serif;padding:8px 14px;cursor:pointer}.lt .prt svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8}@media print{.lt .prt{display:none}}@media (prefers-color-scheme:dark){.lt .prt{background:#22324d;color:#a9c8ff}}
.dsk{background:#fff}.dskh{display:flex;gap:12px;align-items:flex-start}
.dskh svg{flex:none;width:30px;height:30px;stroke:#1a73e8;fill:none;stroke-width:1.8;stroke-linecap:round}
.dskh b{display:block;font-size:17px;color:#1d1d1f}.dskh small{display:block;font-size:14.5px;color:#515154;line-height:1.4;margin-top:2px}
.dskb{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}
.dskb button{border:0;border-radius:12px;min-height:46px;font:700 15px -apple-system,system-ui,sans-serif;background:#eef4fe;color:#1a5fd0;cursor:pointer}
.dskb button:first-child{grid-column:1/-1;background:#1a73e8;color:#fff}
@media (prefers-color-scheme:dark){.abt{color:#f5f5f7}.abl{color:#7fb0ff}.dsk{background:#1c1c1e}.dskh b{color:#f5f5f7}.dskh small{color:#c7c7cc}.dskb button{background:#22324d;color:#a9c8ff}}
@media print{nav,.dock,#dock,.fab,.mcbar,#sch,.dsk,.akmore2,header .pv,.pv{display:none!important}body{background:#fff!important}.w,.ak{box-shadow:none!important;break-inside:avoid;border:1px solid #ddd}.akbody.clip>*{display:block!important}}
'''
k=v.find('</style>'); v=v[:k]+css+v[k:]
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-24a'",v)
p.write_text(v); pathlib.Path('live/montage-r8x2/v3/version.txt').write_text('2026-11-24a\n'); print('ok')
