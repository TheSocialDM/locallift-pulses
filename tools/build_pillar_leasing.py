"""Build team/<key>/leasing/ (agent page and QR card) for a Pillar app from the Huxley leasing page, with Ava.
Prices and offer refresh live from live/<folder>/data.json.
Usage: python3 tools/build_pillar_leasing.py cuvee|elevation-santan"""
import os,re,io,sys,json,segno
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
K=sys.argv[1]
C={'cuvee':dict(folder='cuvee-c6v2',name='Cuvee',full='Cuvee',site='livecuvee.com',tel='+18338973859',ph='(833) 897-3859',
     addr='7200 N. 91st Ave, Glendale, AZ',vadr=';;7200 N 91st Ave;Glendale;AZ;85305;USA',maps='Cuvee+Apartments+7200+N+91st+Ave+Glendale+AZ+85305',
     col='#7b2340',dk='#5a1830',lt='#e3a6b8',area='Glendale',
     life='Rooftop terrace over Westgate, two resort style pools with firepits, a two story fitness center, a game room and a pet spa.',
     gal=[('pool','Cuvee pool and spa','Pool and spa'),('rooftop','Cuvee rooftop terrace','Rooftop terrace'),('gym','Cuvee fitness center','Fitness center'),('kitchen','Cuvee apartment kitchen','Kitchens')],
     near='<li>Westgate Entertainment District<span>dining and entertainment, close by</span></li><li>State Farm Stadium<span>close by</span></li><li>Tanger Outlets<span>shopping, minutes by car</span></li>',
     sub='1 and 2 bedroom homes.',offP='Limited time. The leasing team confirms which homes and lease terms qualify.',
     cardline='Your home near Westgate',cardam='Rooftop terrace · Two pools · Game room · Pet spa',cardshot='rooftop'),
   'elevation-santan':dict(folder='elevation-santan-e3t8',name='Elevation SanTan',full='Elevation SanTan',site='elevationsantan.com',tel='+14806050338',ph='(480) 605-0338',
     addr='2045 E. Boston St, Gilbert, AZ',vadr=';;2045 E Boston St;Gilbert;AZ;85295;USA',maps='Elevation+San+Tan+2045+E+Boston+St+Gilbert+AZ+85295',
     col='#2b5f87',dk='#1d4361',lt='#9cc3e0',area='Gilbert',
     life='Fourth floor sky lounge, resort style pool and spa with cabanas, two level fitness center, two gated dog parks and garages on select homes.',
     gal=[('lounge','Elevation SanTan clubhouse lounge','Clubhouse'),('lobby','Elevation SanTan lobby lounge','Lobby lounge'),('gym','Elevation SanTan fitness center','Fitness center'),('kitchen','Elevation SanTan apartment kitchen','Kitchens')],
     near='<li>SanTan Village<span>shopping, dining and entertainment, a short walk</span></li><li>Loop 202<span>minutes away</span></li>',
     sub='Studio, 1 and 2 bedroom homes.',offP='On select homes and lease terms, while supplies last. The leasing team confirms which homes qualify.',
     cardline='Your home by SanTan Village',cardam='Sky lounge · Pool and spa · Two level gym · Dog parks',cardshot='lounge')}[K]
SRC=os.path.join(R,'team/huxley/leasing');DST=os.path.join(R,'team',K,'leasing')
os.makedirs(os.path.join(DST,'card'),exist_ok=True)
D=json.load(open(os.path.join(R,'live',C['folder'],'data.json')));T=D['talk']
def conv(s):
    s=s.replace('huxley-h7k2',C['folder']).replace('llhx-','ll'+('cv' if K=='cuvee' else 'es')+'-').replace('meet/huxley/','meet/'+K+'/').replace('team/huxley/','team/'+K+'/')
    s=s.replace('data-llprop="huxley"','data-llprop="'+K+'"')
    s=s.replace('Huxley+Scottsdale+8555+E+Raintree+Dr+Scottsdale+AZ+85260',C['maps']).replace(';;8555 E Raintree Dr;Scottsdale;AZ;85260;USA',C['vadr'])
    s=s.replace('8555 E. Raintree Dr, Scottsdale, AZ',C['addr']).replace('+14807718082',C['tel']).replace('(480) 771-8082',C['ph'])
    s=s.replace('huxleyscottsdale.com',C['site'])
    for a,b in {'#C8241D':C['col'].upper(),'#c8241d':C['col'],'#9a1b16':C['dk'],'#f2a49f':C['lt']}.items(): s=s.replace(a,b)
    s=s.replace('Huxley-Scottsdale-Leasing.vcf',C['full'].replace(' ','-')+'-Leasing.vcf')
    s=s.replace('Huxley Scottsdale',C['full']).replace(' at Huxley · Scottsdale',' at '+C['name']+' · '+C['area']).replace('Huxley',C['name']).replace('Scottsdale',C['area'])
    return s
t=conv(open(os.path.join(SRC,'index.html')).read())
lab={'Studio from':'Studio','1 bed from':'1 bedroom','2 bed from':'2 bedroom'}
plans=''.join(f'<div class="plan"><b>{lab[l]}</b><div class="pr">{v}<i>starting at</i></div><span>Rent</span></div>' for v,l in T['prices'])
i=t.find('<div class="plans" id="plans">');j=t.find('<p class="asof"',i);t=t[:i]+'<div class="plans" id="plans">'+plans+'</div>\n    '+t[j:]
t=t.replace("var m={'1 bed from':'1 bedroom','2 bed from':'2 bedroom'}","var m={'Studio from':'Studio','1 bed from':'1 bedroom','2 bed from':'2 bedroom'}")
sp=D['compete']['us']['specialShort'];sp=sp[0].upper()+sp[1:]
t=re.sub(r'<h2 id="offH">.*?</h2>','<h2 id="offH">'+sp+'</h2>',t,flags=re.S)
t=re.sub(r'<p id="offP">.*?</p>','<p id="offP">'+C['offP']+'</p>',t,flags=re.S)
t=t.replace("$('#offP').textContent='Limited time, on select lease terms. The leasing team confirms which homes qualify.'","$('#offP').textContent='"+C['offP']+"'")
t=re.sub(r'<p class="sub">1 and 2 bedroom homes\.','<p class="sub">'+C['sub'],t)
t=re.sub(r'Starting rents from '+re.escape(C['site'])+r' on [A-Za-z]+ \d+',f"Starting rents from {C['site']} on {T['checked']}",t)
t=re.sub(r'(<h2>Life at '+re.escape(C['name'])+r'</h2>\s*<p class="sub">).*?(</p>)',lambda m:m.group(1)+C['life']+m.group(2),t,flags=re.S)
gal=''.join(f'<figure><img src="../../../live/{C["folder"]}/shots/{a}.jpg" alt="{b}"><figcaption>{c}</figcaption></figure>' for a,b,c in C['gal'])
t=re.sub(r'<div class="gal">.*?</div>','<div class="gal">'+gal+'</div>',t,count=1,flags=re.S)
t=re.sub(r'<ul class="near">.*?</ul>','<ul class="near">'+C['near']+'</ul>',t,count=1,flags=re.S)
t=t.replace('Take a look at '+C['name']+' with me.','Take a look at '+C['name']+' with me.')
open(os.path.join(DST,'index.html'),'w').write(t)
QURL=f'https://thesocialdm.github.io/locallift-pulses/team/{K}/leasing/?src=qr'
q=segno.make(QURL,error='m');b=io.BytesIO();q.save(b,kind='svg',dark='#1c1c1e',light='#fff',border=2,xmldecl=False,svgns=True,svgclass='segno',lineclass='qrline',omitsize=True);qsvg=b.getvalue().decode()
open(os.path.join(DST,'qr.svg'),'w').write(qsvg)
c=open(os.path.join(SRC,'card/index.html')).read()
c=re.sub(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 \d+ \d+".*?</svg>',qsvg,c,count=1,flags=re.S)
c=c.replace('shots/rooftop.jpg','shots/'+C['cardshot']+'.jpg').replace('Your home in North Scottsdale',C['cardline']).replace('Rooftop deck · Pool and spa · Work lounge · Pet spa',C['cardam']).replace('8555 E. Raintree Dr, Scottsdale',C['addr'].rsplit(', AZ',1)[0])
c=conv(c)
open(os.path.join(DST,'card/index.html'),'w').write(c)
for f in ['index.html','card/index.html']:
    s=open(os.path.join(DST,f)).read()
    print(f,len(s),'leftovers',sorted(set(re.findall(r'(?i)huxley|scottsdale|raintree|kierland|h7k2|llhx|c8241d|rooftop deck|billiards|work lounge|11 weeks',s))))
