"""Show a clear fallback in the app when data.json has no current special.
Usage: python3 tools/special_fallback.py live/stillwater-k4p7/v3/index.html"""
import sys
p=sys.argv[1];s=open(p).read()
NOSP="'No special posted today. Check with the office before quoting one.'"
a="esc(D.talk.offer)";b="esc((D.talk.offer||'').trim()||"+NOSP+")"
c="esc(U.special)";d="esc((U.special||'').trim()||"+NOSP+")"
if a in s or c in s:
    s=s.replace(a,b).replace(c,d);open(p,'w').write(s);print('fallback added')
else: print('already has fallback')
