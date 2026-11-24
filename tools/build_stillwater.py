"""Build the Stillwater Lakes LocalLift Live app (live/stillwater-k4p7/v3/index.html) from the Montage app.

Method: three way merge. base = Montage v3 at a558a38 (the version Stillwater was made from on Nov 19),
ours = current Montage v3 (feature source), theirs = Stillwater v3 at a558a38 (Stillwater content).
Line level merge first; each conflicting hunk is merged again at token level. Then Montage only
code added after Nov 19 gets the same Montage to Stillwater mapping (names, links, storage keys,
colors), and a final sweep turns any remaining warm color into the Stillwater teal hue.
Usage: python3 tools/build_stillwater.py [APPV]"""
import re,subprocess,sys,os,json,colorsys,difflib,collections,tempfile
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
APPV=sys.argv[1] if len(sys.argv)>1 else '2026-11-24s2'
def gs(ref,p): return subprocess.run(['git','-C',R,'show',f'{ref}:{p}'],capture_output=True,text=True,check=True).stdout
MP='live/montage-r8x2/v3/index.html';SP='live/stillwater-k4p7/v3/index.html'
base=gs('a558a38',MP);theirs=gs('a558a38',SP);ours=gs('989f262',MP)  # Montage APPV 2026-11-24e; later Montage gate and alert changes are applied below
W=tempfile.mkdtemp()
def wr(n,s):
    p=os.path.join(W,n);open(p,'w').write(s);return p
NL='\x01NL\x01'
def tok(t): return ''.join((NL if x=='\n' else x)+'\n' for x in re.findall(r'\w+|\s|[^\w\s]',t))
def mf(o,b,t):
    r=subprocess.run(['git','merge-file','-p','--diff3',wr('o',o),wr('b',b),wr('t',t)],capture_output=True,text=True)
    return r.stdout,r.returncode
def blocks(s):
    L=s.split('\n');i=0;out=[]
    while i<len(L):
        if L[i].startswith('<<<<<<< '):
            o=[];b=[];t=[];i+=1
            while not L[i].startswith('||||||| '): o.append(L[i]);i+=1
            i+=1
            while L[i]!='=======': b.append(L[i]);i+=1
            i+=1
            while not L[i].startswith('>>>>>>> '): t.append(L[i]);i+=1
            out.append(('c',o,b,t))
        else: out.append(('l',L[i]))
        i+=1
    return out
merged,_=mf(ours,base,theirs)
res=[];nc=0
for x in blocks(merged):
    if x[0]=='l': res.append(x[1]);continue
    O,B,T=['\n'.join(y)+'\n' for y in x[1:]]
    tm,_=mf(tok(O),tok(B),tok(T))
    parts=[]
    for y in blocks(tm):
        if y[0]=='l': parts.append(y[1]);continue
        o,b,t=y[1],y[2],y[3];js=lambda a:''.join('\n' if z==NL else z for z in a)
        if re.fullmatch(r'\d{2}[a-z]\d*',js(o).strip()): parts.append(APPV.split('-')[-1]);continue   # APPV suffix
        if js(b).strip()=='' : parts+=o+t;continue        # both inserted: keep Montage feature, then Stillwater overrides
        raise SystemExit('unresolved token conflict: '+js(o)[:200]+' | '+js(t)[:200])
    h=''.join('\n' if z==NL else z for z in parts)
    res.append(h[:-1] if h.endswith('\n') else h)
t='\n'.join(res)
t=re.sub(r"const APPV='[^']*'",f"const APPV='{APPV}'",t)

# ---- color map learned from the Nov 19 conversion (base -> theirs)
TK=lambda s:re.findall(r'#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|\w+|\s|[^\w\s]',s)
b=TK(base);th=TK(theirs);cm=collections.defaultdict(collections.Counter)
for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,b,th,autojunk=False).get_opcodes():
    if op=='replace' and i2-i1==1 and j2-j1==1 and (b[i1].startswith('#') or b[i1].startswith('rgb')):
        cm[b[i1].lower().replace(' ','')][th[j1]]+=1
CM={k:v.most_common(1)[0][0] for k,v in cm.items()}

# ---- Montage only content added after Nov 19
def sub(a,bb,cnt=None):
    global t
    n=t.count(a)
    if n==0: raise SystemExit('missing: '+a[:80])
    if cnt is not None and n!=cnt: raise SystemExit(f'count {n}!={cnt}: '+a[:80])
    t=t.replace(a,bb)
# market: neutral fallback, Stillwater data comes from data.json "market"
i=t.find('const HX0={');j=t.find('const hx=',i)
t=t[:i]+r"""const HX0={name:'Stillwater Lakes',rvh:['Community','1 bed from','2 bed from'],rv:[],srh:['Source','Visits','Leads'],sr:[],pts:[],cards:[],line:'',briefSrc:'',
 ex:[{k:'edge',re:/(we have|have that|edge|stand out|better than|amenit|selling point|they don)/i},{k:'ops',re:/who showed|showed (the|them)|agent|service request|work order|maintenance|pending/i},{k:'why',re:/why|not (renting|signing|leasing)|didn|tour|traffic|lost|close/i},{k:'specials',re:/special|concession|free|deal|offer/i},{k:'src',re:/lead|source|where|google ads|facebook|zillow/i},{k:'rivals',re:/rival|competit|who are|up against|winning/i},{k:'price',re:/price|priced|rent\b|rents|deposit|fees?/i},{k:'gbp',re:/listing|calls?\b|direction|maps|gbp/i},{k:'reviews',re:/review|stars|rating/i},{k:'ai',re:/\bai\b|chatgpt|copilot|gemini|perplexity|bing/i}]};
const mOn=()=>!!(typeof D!=='undefined'&&D&&D.market&&D.market.cards&&D.market.cards.length);
"""+t[j:]
sub("const hx=()=>{const m=(typeof D!=='undefined'&&D&&D.market&&D.market.cards)?D.market:null;if(!m)return HX0;","const hx=()=>{const m=mOn()?D.market:null;if(!m)return Object.assign({},HX0,{ex:[]});")
sub("x[0]==='Montage'?'me':''","x[0]===((D&&D.property)||'Stillwater Lakes')?'me':''")
sub("<b style=\"display:block;margin-top:12px\">Where leads came from</b>${tbl(HX.srh,HX.sr)}","${HX.sr&&HX.sr.length?'<b style=\"display:block;margin-top:12px\">Where leads came from</b>'+tbl(HX.srh,HX.sr):''}")
sub("esc2(HX.briefSrc||'Websites checked 11/23 · leads Oct 26 to Nov 22')","esc2(HX.briefSrc||'')")
sub("<h3 style=\"margin-top:0\">Montage meeting brief</h3>","<h3 style=\"margin-top:0\">Stillwater Lakes meeting brief</h3>")
sub("esc2(HX.line||'Leads in 4 weeks: Google search 24, direct 13, Google Ads 10.')}</b><small>See rivals, specials and where every lead came from ›</small>","esc2(HX.line||'')}</b><small>See rivals, specials and talking points ›</small>")
sub("const line=()=>`","const line=()=>!mOn()?'':`")
sub("+askBox()+HX.cards.map(card).join('')+V.rivals()+deskCard();","+(mOn()?askBox()+HX.cards.filter(k=>k.t!=='src'||(HX.sr&&HX.sr.length)).map(card).join(''):'<section class=\"ak\"><div class=\"akh\">'+I('chart')+'Market intel</div><p style=\"margin:6px 0 0\">Market data loads with the morning refresh.</p></section>')+V.rivals()+deskCard();")
sub("const intel=()=>{const cs=HX.cards;","const intel=()=>{const cs=HX.cards;if(!mOn())return'';")
sub("Ask about Montage",'Ask about Stillwater Lakes',2)
# My card
sub("team/montage/leasing/","team/stillwater/leasing/")
sub("const MC_PHONE='(971) 397-7861';","const MC_PHONE='(689) 314-6918';")
sub("${MC_PHONE} · Tigard, OR","${MC_PHONE} · Kissimmee, FL")
sub("const mcUrl=src=>MC_LIVE+'?by='+encodeURIComponent(me||'team')+'&src='+src;","const mcUrl=src=>src==='qr'?'https://live.thesocialdm.com/meet/stillwater/'+mcSlug():MC_LIVE+'?by='+encodeURIComponent(me||'team')+'&src='+src;")
sub("live.thesocialdm.com/meet/montage/","live.thesocialdm.com/meet/stillwater/")
sub("'LocalLift Live help, Montage'","'LocalLift Live help, Stillwater Lakes'")
sub("app:'live_montage'","app:'live_stillwater'")
sub("'https://live.thesocialdm.com/montage'","'https://live.thesocialdm.com/stillwater'")
# flyer: card shows only once the Stillwater flyer exists
sub("const FLYURL='https://live.thesocialdm.com/montage-r8x2/flyer/LocalLift-Live-Montage-flyer.pdf';","const FLYURL='https://live.thesocialdm.com/stillwater-k4p7/flyer/LocalLift-Live-Stillwater-Lakes-flyer.pdf';let FLYON=false;fetch('../flyer/cover.jpg',{method:'HEAD',cache:'no-store'}).then(r=>{if(r.ok){FLYON=true;if(cur==='more')show('more')}}).catch(()=>{});")
sub("const flyCard=()=>`","const flyCard=()=>!FLYON?'':`")
sub("../flyer/LocalLift-Live-Montage-flyer.pdf","../flyer/LocalLift-Live-Stillwater-Lakes-flyer.pdf")
# objections search synonyms: Stillwater rivals
sub("|overland|steward|mercato|","|cielo|jamison|mosaic|")
# Nov 24 Montage follow ups (0e6745f, 502d4cc): no per tap Make alerts; own home screen name and icon
i=t.find("document.addEventListener('click',e=>{if(document.body.classList.contains('gated'))return;const b=e.target.closest('button,a,[role=tab]')")
j=t.find('\n',i);assert i>0 and 'llPing(\'tapped' in t[i:j]
t=t[:i]+'/* per tap alerts removed Nov 24 2026: taps are counted in analytics; Make alerts only for opens, invites and home screen installs to protect the monthly Make operations */'+t[j:]
sub('<meta name="apple-mobile-web-app-title" content="LocalLift Live">','<meta name="apple-mobile-web-app-title" content="Stillwater Live">',1)
sub('<link rel="apple-touch-icon" href="../icon-180.png">','<link rel="apple-touch-icon" href="../icon-180.png?v=s2">',1)
sub("short_name:'LocalLift Live',","short_name:'Stillwater Live',",1)
sub("icon-192.png',sizes","icon-192.png?v=s2',sizes",1)
sub("icon-512.png',sizes","icon-512.png?v=s2',sizes",1)
# storage keys
t=re.sub(r"(['\"`])ll-",r"\1llsw-",t)
# names, generic (after the specific ones above)
t=t.replace('montage-r8x2','stillwater-k4p7').replace('live_montage','live_stillwater')
t=re.sub(r'\bMontage\b','Stillwater Lakes',t)
# colors learned from Nov 19
def cmap(m):
    k=m.group(0);kk=k.lower().replace(' ','')
    return CM.get(kk,k)
t=re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b|rgba?\([^)]*\)',cmap,t)
# sweep: remaining warm colors to Stillwater teal at the same lightness
KEEP={'#fbbc04','#f9ab00','#ffb400','#f5b301','#fbbf24','#f59e0b','#ffcc00','#ffd60a','#ff9f0a','#ff9500','#b45309','#e37400','#ea8600'}
t=re.sub(r'(?i)#b45309','#8a2f2f',t)  # amber warn label -> Stillwater maroon
def warm(r,g,b_):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b_/255);return 15<=h*360<=50 and s>0.2,h,l,s
def tealize(r,g,b_):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b_/255);s2=min(s,0.5)
    R_,G_,B_=colorsys.hls_to_rgb(188/360,l,s2);return round(R_*255),round(G_*255),round(B_*255)
SW=collections.Counter()
def hexsw(m):
    k=m.group(0);x=k[1:]
    if len(x)==3: x=''.join(c*2 for c in x)
    if k.lower() in KEEP: return k
    r,g,b_=int(x[0:2],16),int(x[2:4],16),int(x[4:6],16)
    if warm(r,g,b_)[0]:
        n='#%02x%02x%02x'%tealize(r,g,b_);SW[k+'->'+n]+=1;return n
    return k
def rgbsw(m):
    k=m.group(0);p=[q.strip() for q in m.group(2).split(',')]
    try: r,g,b_=[int(float(q)) for q in p[:3]]
    except: return k
    if warm(r,g,b_)[0]:
        n=tealize(r,g,b_);v=f"{m.group(1)}({n[0]},{n[1]},{n[2]}"+(','+','.join(p[3:]) if len(p)>3 else '')+')';SW[k+'->'+v]+=1;return v
    return k
t=re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b(?![0-9a-fA-F])',hexsw,t)
t=re.sub(r'(rgba?)\(([^)]*)\)',rgbsw,t)
open(os.path.join(R,SP),'w').write(t)
open(os.path.join(R,'live/stillwater-k4p7/v3/version.txt'),'w').write(APPV+'\n')
subprocess.run([sys.executable,os.path.join(R,'tools/personal_codes.py'),os.path.join(R,'live/stillwater-k4p7'),'stillwater','llsw-'],check=True)
t=open(os.path.join(R,SP)).read()
# gate: personal codes are hex, so a text keyboard (Montage 8256c9e)
t=t.replace('<label for="gc">Team code</label><input id="gc" inputmode="numeric" autocomplete="one-time-code" required>','<label for="gc">Your code</label><input id="gc" inputmode="text" autocapitalize="none" autocorrect="off" spellcheck="false" autocomplete="one-time-code" required>')
t=re.sub(r'(id="gmsg">For the Stillwater Lakes team\.)[^<]*<',r'\1 Your code is in your welcome email.<',t)
open(os.path.join(R,SP),'w').write(t)
print('built',len(t),'APPV',APPV);print('warm sweep',dict(SW))
bad=re.findall(r'(?i)montage|tigard|oregon|overland|steward|mercato|washington square|portland|willamette|beaverton|lake oswego|\(971\)|971[ -]\d{3}',t)+re.findall(r', OR\b|America/Los_Angeles',t)
print('leftovers',collections.Counter(bad))
