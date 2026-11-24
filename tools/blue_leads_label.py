"""Leads card heading in Google blue to match its bars (Nov 24 2026)."""
import re,pathlib
p=pathlib.Path('live/montage-r8x2/v3/index.html'); v=p.read_text()
old='const card=k=>{const rich=k.chips||k.cmp||k.list||k.stats;return `<section class="ak">'
assert old in v
v=v.replace(old,'const card=k=>{const rich=k.chips||k.cmp||k.list||k.stats;return `<section class="ak${k.t===\'src\'?\' akblue\':\'\'}">')
css='''.akblue .akl span:first-child{color:#1a73e8!important}.akblue .akl .akp{background:#1a73e8!important;color:#fff!important}.akblue h4{color:#0b4cc0!important}
@media (prefers-color-scheme:dark){.akblue .akl span:first-child{color:#7fb0ff!important}.akblue .akl .akp{background:#2f6fe0!important}.akblue h4{color:#a9c8ff!important}}
'''
i=v.find('</style>'); v=v[:i]+css+v[i:]
v=re.sub(r"const APPV='[^']*'","const APPV='2026-11-24b'",v)
p.write_text(v); pathlib.Path('live/montage-r8x2/v3/version.txt').write_text('2026-11-24b\n'); print('ok')
