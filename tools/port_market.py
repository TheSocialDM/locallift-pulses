"""Port the Market tab / Ask about Montage (built Nov 23 evening in the private preview) into the live v3 app.
Market numbers come from data.json "market" (refreshed by the daily run); the copy in code is only a fallback."""
import re,json,pathlib,sys
app=pathlib.Path('live/montage-r8x2'); v=(app/'v3/index.html').read_text()
blk=pathlib.Path('/home/claude/prev/market_block.js').read_text()
assert 'data-v="market"' not in v, 'already ported'
# 1 nav tab after Tour
nav_btn='<button role="tab" data-v="market" aria-selected="false"><svg viewBox="0 0 24 24"><path d="M4 19V5M4 19h16"/><path d="M7 15l4-4 3 3 5-6"/></svg>Market</button>'
m=re.search(r'(<button role="tab" data-v="tourv"[^>]*>.*?</button>)',v,re.S); assert m
v=v.replace(m.group(1),m.group(1)+'\n  '+nav_btn,1)
# 2 block: live wording, data driven
blk=blk.replace('(private preview)','(live)')
blk=blk.replace('const HX={','const HX0={',1)
blk=blk.replace("const ex=HX.ex;","const hx=()=>{const m=(typeof D!=='undefined'&&D&&D.market&&D.market.cards)?D.market:null;if(!m)return HX0;const o=Object.assign({},HX0,m);o.ex=(m.ex||[]).map(x=>{const b=HX0.ex.find(y=>y.k===x.k);return Object.assign({},x,{re:b?b.re:/$^/})});return o};\nconst HX=new Proxy({},{get:(t,k)=>hx()[k]});\nconst exF=()=>hx().ex;const ex={find:f=>exF().find(f)};")
blk=blk.replace("const exO=['why','edge','specials','src','price','ops','reviews','ai'].map(k=>ex.find(x=>x.k===k)).filter(Boolean);",
 "const EXO=['why','edge','specials','src','price','ops','reviews','ai'];const exOf=()=>EXO.map(k=>exF().find(x=>x.k===k)).filter(Boolean);")
blk=blk.replace('${exO.map(','${exOf().map(')
assert 'exO.' not in blk
blk=blk.replace("'In the live app this answers from all of Montage’s weekly data. In this preview, try one of the questions below.<span class=\"aks\">Preview</span>'","'I do not have that one yet. Try one of these questions, or search Objections and answers.<span class=\"aks\">LocalLift Live</span>'")
blk=blk.replace("<p class=\"mcd\">In the live app this prints or saves as a PDF from the phone or laptop.</p>","")
blk=blk.replace("<span class=\"aks\">Websites checked 11/23 · leads Oct 26 to Nov 22</span>","<span class=\"aks\">${esc2(HX.briefSrc||'Websites checked 11/23 · leads Oct 26 to Nov 22')}</span>")
blk=blk.replace("s:'Preview'","s:'LocalLift Live'")
blk=blk.replace("const line=()=>`<button class=\"akline\" data-v2=\"market\"><span class=\"akl\"><span>MARKET</span><span class=\"akp new\">New</span></span><b>Leads in 4 weeks: Google search 24, direct 13, Google Ads 10.</b>",
 "const line=()=>`<button class=\"akline\" data-v2=\"market\"><span class=\"akl\"><span>MARKET</span><span class=\"akp new\">New</span></span><b>${esc2(HX.line||'Leads in 4 weeks: Google search 24, direct 13, Google Ads 10.')}</b>")
assert 'Preview' not in blk and 'preview' not in blk.lower().replace('(live)',''), [l for l in blk.split('\n') if 'review' in l.lower() and 'preview' in l.lower()][:3]
anchor="document.addEventListener('click',e=>{try{if(e.target.closest('#raOk'))"
i=v.index(anchor); j=v.index('\n}\n</script>',i)
v=v[:j]+'\n'+blk.rstrip()+'\n'+v[j:]
v=v.replace('grid-template-columns:repeat(5,1fr);padding:6px;z-index:5}','grid-template-columns:repeat(6,1fr);padding:6px;z-index:5}',1)
v=v.replace('</style>','@media (max-width:350px){nav button{font-size:9.5px}nav svg{width:21px;height:21px}}\n</style>',1)
# 3 objections subtitle
v=v.replace('Type what they said. Get the answer fast.','Type what they said, or ask about the market.')
# 4 see what renters see on the assistant card
old="<small>Mia welcomes people who open your page, then points them to you.</small></div><em>›</em></section>"
assert old in v
v=v.replace(old,"<small>Mia welcomes people who open your page, then points them to you.</small><span class=\"mcsee\" data-mc=\"prospect\" role=\"button\">${I(\"eye\")}See what renters see ›</span></div><em>›</em></section>")
v=v.replace('</style>','.mcsee{display:inline-flex;align-items:center;gap:4px;margin-top:6px;font-size:13px;font-weight:700;color:#b46e26}.mcsee .mci2{width:15px;height:15px}@media (prefers-color-scheme:dark){.mcsee{color:#e0a463}}\n</style>',1)
# 5 version bump
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-23j'",v)
(app/'v3/index.html').write_text(v); (app/'v3/version.txt').write_text('2026-11-23j\n')
# 6 data.json market
d=json.loads((app/'data.json').read_text())
src=blk  # parse HX0 values via node
print('ok',len(v))
