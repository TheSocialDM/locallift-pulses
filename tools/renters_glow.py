"""'See what renters see' as a big glowing blue button (Nov 24 2026)."""
import re,pathlib
p=pathlib.Path('live/montage-r8x2/v3/index.html'); v=p.read_text()
assert 'class="mcsee"' in v or "class=\\\"mcsee\\\"" in v
css='''
/* ===== See what renters see, glowing button (Nov 24 2026) ===== */
.mcsee{display:flex!important;width:100%;justify-content:center;align-items:center;gap:8px!important;margin-top:12px!important;padding:13px 16px;min-height:50px;border-radius:14px;
 background:linear-gradient(135deg,#1a73e8,#4c8df6)!important;color:#fff!important;font-size:16.5px!important;font-weight:800!important;letter-spacing:-.01em;
 box-shadow:0 0 0 0 rgba(26,115,232,.55),0 6px 18px rgba(26,115,232,.35);animation:mcglow 2.4s ease-in-out infinite;cursor:pointer}
.mcsee .mci2,.mcsee svg{width:20px!important;height:20px!important;stroke:#fff!important;color:#fff!important}
@keyframes mcglow{0%,100%{box-shadow:0 0 0 0 rgba(26,115,232,.5),0 6px 18px rgba(26,115,232,.3)}50%{box-shadow:0 0 0 8px rgba(26,115,232,0),0 8px 26px rgba(26,115,232,.55)}}
@media (max-width:360px){.mcsee{font-size:14px!important;padding:12px 6px;gap:5px!important;white-space:nowrap}.mcsee svg,.mcsee .mci2{width:17px!important;height:17px!important}}
@media (prefers-reduced-motion:reduce){.mcsee{animation:none}}
@media (prefers-color-scheme:dark){.mcsee{background:linear-gradient(135deg,#2f6fe0,#5b9bff)!important;color:#fff!important}}
'''
i=v.rfind('</style>'); j=v.rfind('</style>',0,i)
k=v.find('</style>'); v=v[:k]+css+v[k:]
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-24c'",v)
p.write_text(v); pathlib.Path('live/montage-r8x2/v3/version.txt').write_text('2026-11-24c\n'); print('ok')
