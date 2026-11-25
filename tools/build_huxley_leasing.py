"""Builds team/huxley/leasing/ (agent page and card sample) from the generated Fora leasing page, in Huxley and Pillar brand,
with Ava (Pillar page assistant). Prices and offer refresh live from live/huxley-h7k2/data.json.
Usage: python3 tools/build_huxley_leasing.py  (run tools/build_fora_leasing.py first if the Fora page changed)"""
import os,re,io,json,segno
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
SRC=os.path.join(R,'team/fora/leasing');DST=os.path.join(R,'team/huxley/leasing')
os.makedirs(os.path.join(DST,'card'),exist_ok=True)
D=json.load(open(os.path.join(R,'live/huxley-h7k2/data.json')));T=D['talk']
AVA=re.search(r'<script src="\.\./\.\./\.\./guide/guide\.js.*?</script>',open(os.path.join(R,'team/huxley/melanie/index.html')).read(),re.S).group(0)
AVA=re.sub(r'data-pro="[^"]*"','data-pro="the leasing team"',AVA).replace("or tap to call your leasing pro.","or tap to call our leasing team.")
AVA=AVA.replace('data-offer="https://www.huxleyscottsdale.com/leasingoffers"','data-offer="https://www.huxleyscottsdale.com/leasingoffers" data-name="Ava" data-intro="Hi! I\'m Ava. I\'ll get you to {pro}." data-role="your page assistant" data-tiphide="6" data-size="72" data-vw="0.42" data-sub="AI guide. Calls and tours are handled by the Huxley leasing team." data-l3="Call the leasing team" data-l2="See current specials"',1)
AVA=re.sub(r'(data-name="Ava")(.*?)\sdata-name="Ava"',r'\1\2',AVA,flags=re.S)
COL={'#1f1f20':'#1c1c1e','#6b6663':'#6b6b6b','#e6dcd5':'#e7e5e2','#7c453d':'#c8241d','#2f2f30':'#2c2c2e','#f6f2ef':'#f6f5f3','#ece4de':'#ecebe8','#e2b8a8':'#f2a49f','#5e322b':'#9a1b16','#f1e8e3':'#f3f2ef'}
def conv(s):
    card=s.startswith('<!--card')
    s=re.sub(r'<script src="(?:\.\./)+guide/guide\.js.*?</script>',lambda m:AVA.replace('"../../../','"../../../../') if card else AVA,s,flags=re.S)
    for a,b in COL.items(): s=s.replace(a,b)
    s=s.replace('family=Montserrat:wght@500;600;700&family=Questrial','family=Montserrat:wght@500;600;700&family=Inter:wght@400;500;600').replace('font-family:Questrial','font-family:Inter')
    s=s.replace('fora-50r1','huxley-h7k2').replace('llfo-','llhx-').replace('meet/fora/','meet/huxley/').replace('team/fora/','team/huxley/')
    s=s.replace('https://www.google.com/maps/search/?api=1&amp;query=Fora+Apartments+10244+Jeffreys+St+Las+Vegas+NV+89183','https://www.google.com/maps/search/?api=1&amp;query=Huxley+Scottsdale+8555+E+Raintree+Dr+Scottsdale+AZ+85260')
    s=s.replace(';;10244 Jeffreys St;Las Vegas;NV;89183;USA',';;8555 E Raintree Dr;Scottsdale;AZ;85260;USA')
    s=s.replace('10244 Jeffreys St, Las Vegas, NV','8555 E. Raintree Dr, Scottsdale, AZ').replace('10244 Jeffreys St, Las Vegas','8555 E. Raintree Dr, Scottsdale')
    s=s.replace('+17252094665','+14807718082').replace('(725) 209-4665','(480) 771-8082')
    s=s.replace('foravegas.com','huxleyscottsdale.com')
    s=s.replace('Fora in Las Vegas','Huxley Scottsdale').replace('Fora Leasing (Las Vegas)','Huxley Scottsdale Leasing').replace('Fora Leasing Team (Las Vegas)','Huxley Scottsdale Leasing Team')
    s=s.replace('Las Vegas','Scottsdale').replace('Fora','Huxley').replace('Huxley-Leasing.vcf','Huxley-Scottsdale-Leasing.vcf')
    return s
t=conv(open(os.path.join(SRC,'index.html')).read())
plans=''.join(f'<div class="plan"><b>{l.replace(" from","").replace("bed","bedroom")}</b><div class="pr">{v}<i>starting at</i></div><span>Rent</span></div>' for v,l in T['prices'])
t=re.sub(r'<div class="plans" id="plans">.*?</div></div>\s*\n?','<div class="plans" id="plans">'+plans+'</div>\n',t,count=1,flags=re.S) if False else t
i=t.find('<div class="plans" id="plans">');j=t.find('<p class="asof"',i);t=t[:i]+'<div class="plans" id="plans">'+plans+'</div>\n    '+t[j:]
t=re.sub(r'<h2 id="offH">.*?</h2>','<h2 id="offH">Up to 11 weeks free</h2>',t,flags=re.S)
t=re.sub(r'<p id="offP">.*?</p>','<p id="offP">Limited time, on select lease terms. The leasing team confirms which homes qualify.</p>',t,flags=re.S)
t=t.replace("var m={'1 bed base rent from':'1 bedroom','2 bed base rent from':'2 bedroom','3 bed base rent from':'3 bedroom'}","var m={'1 bed from':'1 bedroom','2 bed from':'2 bedroom'}")
t=t.replace('<span>Base rent</span>','<span>Rent</span>')
t=re.sub(r"\$\('#offP'\)\.textContent=/2027/.*?:'The leasing team confirms which homes qualify.'","$('#offP').textContent='Limited time, on select lease terms. The leasing team confirms which homes qualify.'",t,flags=re.S)
t=re.sub(r'<p class="sub">1, 2 and 3 bedroom homes\.','<p class="sub">1 and 2 bedroom homes.',t)
t=re.sub(r'Starting base rents from huxleyscottsdale\.com on [A-Za-z]+ \d+',f"Starting rents from huxleyscottsdale.com on {T['checked']}",t)
t=t.replace("Starting base rents from huxleyscottsdale.com on '","Starting rents from huxleyscottsdale.com on '")
t=re.sub(r'(<h2>Life at Huxley</h2>\s*<p class="sub">).*?(</p>)',r'\1Work from home lounge, rooftop deck with grills, billiards room, resort style pool and spa, and a pet spa.\2',t,flags=re.S)
G=[('pool','Huxley pool and spa','Pool and spa'),('rooftop','Huxley rooftop deck','Rooftop deck'),('work','Huxley work from home lounge','Work lounge'),('kitchen','Huxley apartment kitchen','Kitchens')]
gal=''.join(f'<figure><img src="../../../live/huxley-h7k2/shots/{a}.jpg" alt="{b}"><figcaption>{c}</figcaption></figure>' for a,b,c in G)
t=re.sub(r'<div class="gal">.*?</div>','<div class="gal">'+gal+'</div>',t,count=1,flags=re.S)
t=re.sub(r'<ul class="near">.*?</ul>','<ul class="near"><li>Scottsdale Quarter<span>shopping and dining, minutes by car</span></li><li>Kierland Commons<span>shopping and dining, minutes by car</span></li><li>Loop 101<span>minutes away</span></li></ul>',t,count=1,flags=re.S)
t=t.replace('.me img{width:78%;height:auto}','.me img{width:84%;height:auto}').replace('.hero .logo{height:22px;width:auto}','.hero .logo{height:22px;width:auto}')
t=t.replace('</style>','.near li span{white-space:normal!important;text-align:right;max-width:55%}</style>',1)
t=t.replace("var s=u&&u.specialShort||'';","var s=(u&&u.specialShort||'').replace(/ on select lease terms/,'');s=s.charAt(0).toUpperCase()+s.slice(1);")
open(os.path.join(DST,'index.html'),'w').write(t)
QURL='https://thesocialdm.github.io/locallift-pulses/team/huxley/leasing/?src=qr'
q=segno.make(QURL,error='m');b=io.BytesIO();q.save(b,kind='svg',dark='#1c1c1e',light='#fff',border=2,xmldecl=False,svgns=True,svgclass='segno',lineclass='qrline',omitsize=True);qsvg=b.getvalue().decode()
open(os.path.join(DST,'qr.svg'),'w').write(qsvg)
c=open(os.path.join(SRC,'card/index.html')).read()
c=re.sub(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41 41".*?</svg>',qsvg,c,flags=re.S)
c='<!--card-->'+c
c=c.replace('Your home near Henderson','Your home in North Scottsdale').replace('Speakeasy · Sky Lounge · Pool · Free parking','Rooftop deck · Pool and spa · Work lounge · Pet spa').replace('shots/lounge.jpg','shots/rooftop.jpg')
c=conv(c)[len('<!--card-->'):]
open(os.path.join(DST,'card/index.html'),'w').write(c)
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import lead_track
for f in ['index.html','card/index.html']: lead_track.agent_file(os.path.join(DST,f),'huxley')
for f in ['index.html','card/index.html']:
    s=open(os.path.join(DST,f)).read()
    print(f,len(s),'leftovers',re.findall(r'(?i)fora|vegas|nevada|henderson|jeffreys|green valley|strip|speakeasy|\bmia\b|725|7c453d|questrial|2027|3 bed',s))
