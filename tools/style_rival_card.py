"""Apple style light 'A rival just moved' card and one change per rival and row (Nov 23 2026)."""
import re,pathlib
p=pathlib.Path('live/montage-r8x2/v3/index.html'); v=p.read_text()
old="const newC=()=>CHG().filter(c=>!seenC[c.id]).sort((a,b)=>(b.flip?1:0)-(a.flip?1:0));"
assert old in v
v=v.replace(old,"const newC=()=>{const s=new Set();return CHG().filter(c=>!seenC[c.id]).sort((a,b)=>String(b.verifiedIso||'').localeCompare(String(a.verifiedIso||''))).filter(c=>{const k=c.rival+'|'+c.row;if(s.has(k)){markSeen(c.id);return false}s.add(k);return true}).sort((a,b)=>(b.flip?1:0)-(a.flip?1:0))};")
css='''
/* ===== rival card, Apple light (Nov 23 2026) ===== */
.w.dark.chg{background:#fff!important;color:#1d1d1f;box-shadow:0 1px 2px rgba(0,0,0,.04),0 8px 24px rgba(0,0,0,.06)!important;border:0}
.chg .ci{border-top-color:#ececf0}.chg .ft2 span{color:#86868b!important}
.w.dark.chg .wt b{color:#1d1d1f;font-size:18px;letter-spacing:-.02em}
.w.dark.chg .wt b .thi,.w.dark.chg .wt b .mci2{color:#b46e26}
.w.dark.chg .wt span{color:#86868b;font-size:13px;font-weight:600}
.w.dark.chg .wt:after,.w.dark.chg .wt b:after{background:#b46e26}
.chg .cr small{color:#86868b;letter-spacing:.04em;font-size:11px}
.chg .pill.them,.chg .pill.us{background:#f5f5f7;border:0;color:#1d1d1f;font-weight:700}
.chg .pill.us{background:#e8f6ee;color:#1a7f45}.chg .pill.us:before{background:#34c759}
.chg .pill.them{background:#fdecea;color:#b3261e}.chg .pill.them:before{background:#ff3b30}
.chg b.hl{color:#1d1d1f;font-size:19px;letter-spacing:-.02em;font-weight:700}
.chg .ft2 s{color:#a1a1a6}.chg .ft2{color:#6e6e73}
.chg .ft2 strong{color:#1d1d1f;font-size:22px;letter-spacing:-.02em}
.chg p{color:#515154!important;font-size:14px;line-height:1.45}
.chg .say3{background:#faf6f1;border-left:3px solid #b46e26;color:#1d1d1f;font-size:14.5px;line-height:1.45;padding:10px 12px;border-radius:12px}
.chg .say3 b{color:#b46e26}
.chg .bt .go3{background:#b46e26;color:#fff;border-radius:12px}
.chg .bt .ok3{background:#f5f5f7;color:#1d1d1f;border-radius:12px}
.chg .cmini{background:#f9f9fb;border:1px solid #ececf0;color:#1d1d1f;border-radius:14px}
.chg .cmini small{color:#86868b}.chg .cmini b{color:#1d1d1f;font-weight:700}.chg .cmini em{color:#515154;font-weight:600}
@media (prefers-color-scheme:dark){
.w.dark.chg{background:#1c1c1e!important;color:#f5f5f7}
.chg .ci{border-top-color:#2c2c2e}.chg .ft2 span{color:#98989d!important}.w.dark.chg .wt b,.chg b.hl,.chg .ft2 strong,.chg .cmini b{color:#f5f5f7}
.w.dark.chg .wt span,.chg .cr small,.chg .cmini small{color:#98989d}
.chg p,.chg .cmini em{color:#c7c7cc!important}.chg .ft2 s{color:#8e8e93}
.chg .say3{background:#2c2c2e;color:#f5f5f7;border-left-color:#e0a463}.chg .say3 b{color:#e0a463}
.chg .pill.us{background:rgba(52,199,89,.16);color:#5fd38a}.chg .pill.them{background:rgba(255,69,58,.16);color:#ff6961}
.chg .bt .go3{background:#e0a463;color:#1d140d}.chg .bt .ok3{background:#2c2c2e;color:#f5f5f7}
.chg .cmini{background:#2c2c2e;border-color:#3a3a3c}}
'''
i=v.find('</style>'); v=v[:i]+css+v[i:]
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-23k'",v)
import re as _r
n0=v.count('esc(c.headline)'); v=v.replace('esc(c.headline)',"esc(String(c.headline).replace(/\\b(\\d) beds\\b/g,'$1 bedrooms').replace(/\\b1 bedrooms\\b/g,'1 bedrooms'))"); print('headlines',n0)
p.write_text(v); pathlib.Path('live/montage-r8x2/v3/version.txt').write_text('2026-11-23k\n')
print('ok')
