"""Phone readable Market cards: chips, compare tables, list rows and stat tiles instead of paragraphs (Nov 23 2026)."""
import re,json,pathlib
p=pathlib.Path('live/montage-r8x2/v3/index.html'); v=p.read_text()
old=v[v.index('const card=k=>`'):]; old=old[:old.index('</section>`;')+len('</section>`;')]
new=r'''const chipsH=k=>k.chips?`<div class="akch">${k.chips.map(c=>`<span>${esc2(c)}</span>`).join('')}</div>`:'';
const cmpH=k=>k.cmp?`<div class="akx" style="grid-template-columns:minmax(0,1.1fr) repeat(${k.cmp.cols.length},minmax(0,1fr))"><span></span>${k.cmp.cols.map((c,i)=>`<span class="h${i?'':' me'}">${esc2(c)}</span>`).join('')}${k.cmp.rows.map(r=>r.map((c,i)=>`<span class="${i===0?'l':i===1?'me':''}">${esc2(c)}</span>`).join('')).join('')}</div>`:'';
const listH=k=>k.list?`<div class="akli">${k.list.map(r=>`<div class="${r[2]==='me'?'me':''}"><b>${esc2(r[0])}</b><span>${esc2(r[1])}</span></div>`).join('')}</div>`:'';
const statH=k=>k.stats?`<div class="akst">${k.stats.map(s=>`<div><b>${esc2(s[0])}</b><span>${esc2(s[1])}</span></div>`).join('')}</div>`:'';
const card=k=>{const rich=k.chips||k.cmp||k.list||k.stats;return `<section class="ak"><div class="akl ${k.c==='warn'?'wn':''}"><span>${k.lab}</span><span class="akp ${k.p[0]}">${k.p[1]}</span></div><h4>${k.h}</h4>${statH(k)}${listH(k)}${cmpH(k)}${chipsH(k)}${k.note?`<p class="akn">${esc2(k.note)}</p>`:''}${!rich&&k.b?`<p>${k.b}</p>`:''}${rows(k)}${k.more?`<p class="akn">${k.more}</p>`:''}<span class="aks">${k.src}</span></section>`};'''
v=v.replace(old,new,1)
css='''
/* ===== Market cards, phone readable (Nov 23 2026) ===== */
.ak h4{font-size:18px!important;letter-spacing:-.02em;line-height:1.25!important;margin:6px 0 10px!important;color:#1d1d1f}
.akl{font-size:12px!important}.aks{font-size:12px!important;color:#86868b!important;margin-top:10px!important}
.ak .akn{font-size:14px!important;color:#6e6e73!important;margin:10px 0 0!important}
.akst{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}@media (max-width:350px){.akst b{font-size:20px!important}.akst span{font-size:12px!important}}
.akst div{background:#f5f5f7;border-radius:14px;padding:12px 10px}.akst b{display:block;font-size:24px;letter-spacing:-.03em;color:#1d1d1f;line-height:1.1}.akst span{display:block;font-size:13px;color:#6e6e73;margin-top:3px;line-height:1.3}
.akli{display:grid;gap:0;border-radius:14px;overflow:hidden;background:#f5f5f7}
.akli div{display:grid;gap:2px;padding:11px 12px;border-top:1px solid #e8e8ed}.akli div:first-child{border-top:0}
.akli b{font-size:13px;color:#6e6e73;font-weight:700}.akli span{font-size:15.5px;color:#1d1d1f;line-height:1.35}
.akli div.me{background:#faf1e6}.akli div.me b{color:#b46e26}.akli div.me span{font-weight:700}
.akx{display:grid;gap:0;border-radius:14px;overflow:hidden;background:#f5f5f7;margin-top:10px}
.akx span,.akli div,.akli b,.akli span{border-radius:0!important}.akx span{padding:10px 8px;font-size:15px;color:#1d1d1f;text-align:center;border-top:1px solid #e8e8ed}
.akx span.h{border-top:0;font-size:12px;font-weight:700;color:#6e6e73;padding:9px 6px}.akx span.h.me{color:#b46e26}
.akx>span:first-child{border-top:0}.akx span.l{text-align:left;font-size:13.5px;color:#6e6e73;font-weight:600;padding-left:12px}
.akx span.me{font-weight:800;background:#faf1e6}.akx span.h.me{background:#faf1e6}
.akch{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}.akch span{background:#fff;border:1px solid #e3e3e8;border-radius:99px;padding:7px 11px;font-size:14px;color:#1d1d1f;font-weight:600}
@media (prefers-color-scheme:dark){.akp.m{background:rgba(52,199,89,.16)!important;color:#5fd38a!important}.akp.s{background:rgba(10,132,255,.18)!important;color:#64b5ff!important}.ak h4{color:#f5f5f7}.akst div,.akli,.akx{background:#2c2c2e}.akst b,.akli span,.akx span,.akch span{color:#f5f5f7}.akst span,.akli b,.akx span.h,.akx span.l,.ak .akn{color:#a1a1a6!important}.akli div,.akx span{border-color:#3a3a3c}.akli div.me,.akx span.me,.akx span.h.me{background:#3a2c1f}.akli div.me b,.akx span.h.me{color:#e0a463}.akch span{background:#2c2c2e;border-color:#3a3a3c}}
'''
i=v.find('</style>'); v=v[:i]+css+v[i:]
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-23l'",v)
p.write_text(v); pathlib.Path('live/montage-r8x2/v3/version.txt').write_text('2026-11-23l\n')
# data: structured fields
dp=pathlib.Path('live/montage-r8x2/data.json'); d=json.loads(dp.read_text()); cs=d['market']['cards']
def c(lab): return next(x for x in cs if x['lab']==lab)
a=c('WHERE WE STAND OUT'); a['h']='Use these on every tour'
a['cmp']={'cols':['Montage','Overland','Mercato'],'rows':[['Deposit','$400','$500','$500'],['Pet rent','$35','$50','$55']]}
a['chips']=['Pool and spa','Sky lounge','Golf simulator','Dog park','Indoor pet spa','Guest suite','Private garages','EV charging']
a['note']='No pet fee and up to 3 pets. The Steward also asks a $400 deposit.'
s=c('SPECIALS WATCH'); s['list']=[['Montage','2 months free plus a $1,000 Look and Lease bonus on select 2 bedrooms, ends Nov 30','me'],['The Overland','Up to 6 weeks free on select homes',''],['The Steward','Free rent, amount not posted',''],['Mercato Grove','No special posted','']]
g=c('GOOGLE LISTING LEADS'); g['h']='What your Google listing drove'; g['stats']=[['552','Direction requests'],['479','Website clicks'],['59','Call taps']]; g['note']='Seen 4,239 times by renters.'
ai=c('AI ANSWERS'); ai['h']='AI assistants name Montage'; ai['stats']=[['36','of 96 AI answers name you'],['43','Visits from ChatGPT'],['1','Lead from ChatGPT']]
dp.write_text(json.dumps(d,indent=1,ensure_ascii=False))
print('ok')
