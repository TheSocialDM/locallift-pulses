"""Builds team/coya/leasing/ (agent page, card sample, qr.svg) from team/montage/leasing in COYA brand.
Prices and specials come from live/coya-3zep/data.json (talk, compete.us). The Specials by email opt in is
left out: its delivery automation is Montage only, and no form ships without automated delivery."""
import os,re,json,io,segno
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
SRC=os.path.join(R,'team/montage/leasing');DST=os.path.join(R,'team/coya/leasing')
os.makedirs(os.path.join(DST,'card'),exist_ok=True)
D=json.load(open(os.path.join(R,'live/coya-3zep/data.json')))
T=D['talk'];U=D['compete']['us'];chk=T['checked']
pr={l:v for v,l in T['prices']}
SITE='https://www.coyaliving.com'
TEL='+17026056291';PH='(702) 605-6291'
MAPS='https://www.google.com/maps/search/?api=1&amp;query=COYA+Apartments+3475+W+Desert+Inn+Rd+Las+Vegas+NV'
FONT='<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
COL={'#21170f':'#2e1d1e','#6e6155':'#6c6a66','#e6dccf':'#e8dfdb','#b46e26':'#633f40','#2a1d14':'#3f2728','#f3ece2':'#f6f3f0','#e3d6c6':'#e3d9d5',
 'rgba(20,12,6,':'rgba(20,12,12,','rgba(30,20,12,':'rgba(20,12,12,','rgba(42,29,20,':'rgba(46,29,30,','rgba(33,23,15,':'rgba(46,29,30,',
 '#e0a463':'#dcbfc0','#d8cbbb':'#e3d9d5','#7e4815':'#4f3132','#e9e0d4':'#efe9e6','#efe4d6':'#efe9e6'}
def recolor(t):
    for a,b in COL.items(): t=t.replace(a,b)
    return t
def mia(t,up):
    # keep the Mia guide, point it at COYA
    t=re.sub(r'data-property="[^"]*"','data-property="COYA"',t)
    t=t.replace('the Montage leasing team','the COYA leasing team')
    t=t.replace('https://www.montagetigard.com/scheduletour',SITE+'/scheduletour').replace('https://www.montagetigard.com/floorplans',SITE+'/floorplans')
    t=t.replace('tel:+19713993242','tel:'+TEL).replace('data-color="#b46e26"','data-color="#633f40"')
    return t
# ---------- agent page
t=open(os.path.join(SRC,'index.html')).read()
head,body=t.split('<body>',1)
script_mia=re.search(r'<script src="\.\./\.\./\.\./guide/guide\.js.*?</script>',body,re.S).group(0)
css=re.search(r'<style>(.*?)</style>',head,re.S).group(1)
css=re.sub(r'\.opt[^{]*\{[^}]*\}\n?','',css)  # opt in styles not needed
css=css.replace('live/montage-r8x2/hero.jpg','live/coya-3zep/hero.jpg')
css=recolor(css)
css+="h1,h2,h3{font-family:Montserrat,Inter,system-ui,sans-serif;font-weight:600;letter-spacing:-.01em}.plan b,.plan .pr,.offer small{font-family:Montserrat,Inter,system-ui,sans-serif}.hero .logo{height:50px;width:auto}.me img{width:78%;height:auto}.ft img{height:52px;width:auto}.near li{align-items:baseline}\n"
sp=U.get('specialShort') or T['offer']
offer_p='First Responder or Preferred Employer savings stack on top. The leasing team confirms which homes qualify.' if 'Look and Lease' in T['offer'] else 'The leasing team confirms which homes qualify.'
plans=[('1 bedroom',pr.get('1 bed base rent from')),('2 bedroom',pr.get('2 bed base rent from')),('3 bedroom',pr.get('3 bed base rent from'))]+[(m[1],m[0]) for m in T.get('more',[])]
plan_html=''.join(f'<div class="plan"><b>{n}</b><div class="pr">{v}<i>starting at</i></div><span>Base rent</span></div>' for n,v in plans if v)
show=U['showoff']
page=f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>COYA in Las Vegas · Your leasing team</title>
<meta property="og:title" content="COYA in Las Vegas · Homes, today's special and your tour">
<meta property="og:description" content="See available homes, current specials and book your tour at COYA in Las Vegas.">
<meta property="og:image" content="https://thesocialdm.github.io/locallift-pulses/live/coya-3zep/hero.jpg">
<meta property="og:type" content="website">
<meta name="description" content="Your leasing team at COYA in Las Vegas. Book a tour, see homes and today's specials.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONT}
<style>{css}</style></head><body>
<main class="pf">
  <div class="hero"><img class="logo" src="../../../live/coya-3zep/logo-white.png" alt="COYA"></div>
  <section class="card">
    <div class="me"><img src="../../../live/coya-3zep/logo-white.png" alt=""></div>
    <h1 id="who">COYA Leasing Team</h1>
    <div class="role" id="role">Your leasing contacts at <b>COYA in Las Vegas</b></div>
    <div class="btns">
      <a href="tel:{TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>Call</a>
      <a href="{SITE}/scheduletour" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>Tour</a>
      <a href="{MAPS}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>Directions</a>
      <a href="{SITE}/floorplans" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11 12 4l9 7v9H3z"/><path d="M9 20v-6h6v6"/></svg>Homes</a>
    </div>
    <div class="stack">
      <a class="btn cu" href="{SITE}/scheduletour" target="_blank" rel="noopener" id="bkt">Book my tour</a>
      <a class="btn" id="vcf" href="#" download="COYA-Leasing.vcf">Save COYA to my contacts</a>
      <button class="btn" id="share" type="button">Send this to a roommate</button>
      <a class="btn" href="{SITE}/" target="_blank" rel="noopener">Visit coyaliving.com</a>
    </div>
  </section>

  <section class="offer" id="offer">
    <small>Current specials</small>
    <h2 id="offH">{sp}</h2>
    <p id="offP">{offer_p}</p>
    <a class="btn" href="{SITE}/floorplans" target="_blank" rel="noopener">See available homes</a>
  </section>

  <section class="sec">
    <h2>Homes available now</h2>
    <p class="sub">Studio, 1, 2 and 3 bedroom homes, and every 2 bedroom has two baths. See every available home with one tap.</p>
    <div class="plans" id="plans">{plan_html}</div>
    <p class="asof" id="asof">Starting base rents from coyaliving.com on {chk}, 2026, and they change often. <a href="{SITE}/floorplans" target="_blank" rel="noopener">See every home live</a></p>
  </section>

  <section class="sec">
    <h2>Life at COYA</h2>
    <p class="sub">Sky Lounge with Strip views, resort style pool, 24 hour fitness center, co working space and a pet spa.</p>
    <div class="gal">
      <figure><img src="../../../live/coya-3zep/shots/view.jpg" alt="COYA lounge with Strip views"><figcaption>Strip views</figcaption></figure>
      <figure><img src="../../../live/coya-3zep/shots/lounge.jpg" alt="COYA Sky Lounge"><figcaption>Sky Lounge</figcaption></figure>
      <figure><img src="../../../live/coya-3zep/shots/kitchen.jpg" alt="COYA apartment kitchen"><figcaption>Kitchens</figcaption></figure>
      <figure><img src="../../../live/coya-3zep/shots/gym.jpg" alt="COYA 24 hour fitness center"><figcaption>24 hour fitness</figcaption></figure>
    </div>
  </section>

  <section class="sec">
    <h2>Nearby</h2>
    <ul class="near">
      <li>Chinatown<span>Spring Mountain Road</span></li>
      <li>The Las Vegas Strip<span>minutes east</span></li>
    </ul>
  </section>

  <section class="sec" style="text-align:center">
    <h2>Toured today?</h2>
    <p class="sub">Keep this page. Your next steps are all here.</p>
    <div class="stack">
      <a class="btn cu" href="{SITE}/floorplans" target="_blank" rel="noopener">Pick my home and apply</a>
      <a class="btn" href="tel:{TEL}">Call with a question</a>
    </div>
  </section>

  <div class="ft"><img src="../../../live/coya-3zep/logo-umber.png" alt="COYA"><br>COYA · 3475 W Desert Inn Rd, Las Vegas, NV<br>{PH} · Equal Housing Opportunity<br>Powered by LocalLift</div>
</main>
<div class="toast" id="toast" role="status"></div>
<script>
(function(){{try{{var q=new URLSearchParams(location.search),n=(q.get('by')||'').replace(/[^A-Za-z .'\\-]/g,'').trim();if(!n||/^team$/i.test(n)){{try{{n=sessionStorage.getItem('llco-by')||''}}catch(x){{}}}}if(!n||/^team$/i.test(n))return;n=n.replace(/\\b\\w/g,function(c){{return c.toUpperCase()}}).slice(0,30);try{{sessionStorage.setItem('llco-by',n)}}catch(x){{}}
document.getElementById('who').textContent=n+' at COYA';document.getElementById('role').innerHTML='Your leasing consultant at <b>COYA in Las Vegas</b>';document.getElementById('bkt').textContent='Book my tour with '+n;document.title=n+' at COYA · Las Vegas';window.llBy=n}}catch(x){{}}}})();
(function(){{
var $=function(s){{return document.querySelector(s)}};
var toast=function(m){{var t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){{t.classList.remove('show')}},3200)}};
var url=location.href.split('#')[0];
var v='BEGIN:VCARD\\r\\nVERSION:3.0\\r\\nFN:'+(window.llBy?window.llBy+', COYA Leasing (Las Vegas)':'COYA Leasing Team (Las Vegas)')+'\\r\\nORG:COYA\\r\\nTITLE:Leasing\\r\\nTEL;TYPE=WORK:{TEL}\\r\\nADR;TYPE=WORK:;;3475 W Desert Inn Rd;Las Vegas;NV;89102;USA\\r\\nURL:'+url+'\\r\\nEND:VCARD\\r\\n';
$('#vcf').href='data:text/vcard;charset=utf-8,'+encodeURIComponent(v);
$('#share').addEventListener('click',function(){{var d={{title:'COYA in Las Vegas',text:'Take a look at COYA with me.',url:url}};if(navigator.share){{navigator.share(d).catch(function(){{}})}}else{{navigator.clipboard.writeText(url).then(function(){{toast('Link copied. Paste it in a text.')}},function(){{toast(url)}})}}}});
// live prices and special from the morning refresh
fetch('../../../live/coya-3zep/data.json',{{cache:'no-store'}}).then(function(r){{return r.json()}}).then(function(d){{var t=d&&d.talk,u=d&&d.compete&&d.compete.us;if(!t)return;
 var s=u&&u.specialShort||'';if(s&&!/no special/i.test(s)){{$('#offH').textContent=s;$('#offP').textContent=/Look and Lease/.test(t.offer||'')?'First Responder or Preferred Employer savings stack on top. The leasing team confirms which homes qualify.':'The leasing team confirms which homes qualify.'}}else if(/no special/i.test(t.offer||'')){{$('#offH').textContent='Ask about this month\\'s specials';$('#offP').textContent='Specials change often. The leasing team will share what is available today.'}}
 var m={{'1 bed base rent from':'1 bedroom','2 bed base rent from':'2 bedroom','3 bed base rent from':'3 bedroom'}},h='';(t.prices||[]).forEach(function(p){{if(m[p[1]])h+='<div class="plan"><b>'+m[p[1]]+'</b><div class="pr">'+p[0]+'<i>starting at</i></div><span>Base rent</span></div>'}});(t.more||[]).forEach(function(p){{h+='<div class="plan"><b>'+p[1]+'</b><div class="pr">'+p[0]+'<i>starting at</i></div><span>Base rent</span></div>'}});if(h)$('#plans').innerHTML=h;
 if(t.checked)$('#asof').firstChild.textContent='Starting base rents from coyaliving.com on '+t.checked+', 2026, and they change often. '}}).catch(function(){{}});
}})();
</script>
{mia(script_mia,3)}
</body></html>
'''
open(os.path.join(DST,'index.html'),'w').write(page)
# ---------- QR (agent page, team link)
QURL='https://thesocialdm.github.io/locallift-pulses/team/coya/leasing/?src=qr'
q=segno.make(QURL,error='m');b=io.BytesIO();q.save(b,kind='svg',dark='#2e1d1e',light='#fff',border=2,xmldecl=False,svgns=True,svgclass='segno',lineclass='qrline',omitsize=True)
qsvg=b.getvalue().decode()
open(os.path.join(DST,'qr.svg'),'w').write(qsvg)
# ---------- card sample
c=open(os.path.join(SRC,'card/index.html')).read()
c=re.sub(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41 41".*?</svg>',qsvg,c,flags=re.S)
c=c.replace('meet/montage/','meet/coya/').replace('live/montage-r8x2','live/coya-3zep').replace('shots/lobby.jpg','shots/lounge.jpg')
c=c.replace('<title>Montage Leasing · QR business card (sample)</title>','<title>COYA Leasing · QR business card (sample)</title>')
c=c.replace('Montage leasing card (sample)','COYA leasing card (sample)')
c=c.replace('open the live Montage profile for your leasing consultant','open the live COYA profile for your leasing consultant')
c=c.replace('<b id="cn">Montage Leasing Team</b><span>Montage in Tigard</span>','<b id="cn">COYA Leasing Team</b><span>COYA in Las Vegas</span>')
c=c.replace('<span class="ph">(971) 399-3242</span><span>13155 SW 68th Parkway, Tigard</span>',f'<span class="ph">{PH}</span><span>3475 W Desert Inn Rd, Las Vegas</span>')
c=c.replace('<b>Your home near Washington Square</b><span>Sky lounge · Pool and spa · Golf simulator · Coworking</span>','<b>Your home in Chinatown</b><span>Sky Lounge · Pool · Pet spa · Co working</span>')
c=c.replace('Open the live Montage profile','Open the live COYA profile').replace('alt="Montage"','alt="COYA"')
c=c.replace('<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',FONT)
c=recolor(c);c=mia(c,4)
c=c.replace('.front .logo{height:8%;position:absolute;top:10%;left:7%}','.front .logo{height:16%;position:absolute;top:9%;left:6%}')
c=c.replace('h1{font:700 20px Montserrat,sans-serif;margin:0}','h1{font:600 21px Montserrat,Inter,sans-serif;margin:0}')
open(os.path.join(DST,'card/index.html'),'w').write(c)
# lead tracking standard: lltrack.js on the agent page and card (tools/lead_track.py)
import sys;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)));import lead_track
for f in ['index.html','card/index.html']: lead_track.agent_file(os.path.join(DST,f),'coya')
for f in ['index.html','card/index.html']:
    s=open(os.path.join(DST,f)).read()
    bad=re.findall(r'(?i)montage|stillwater|kissimmee|tigard|oregon|washington square|971|overland|steward|mercato|#b46e26|#2a1d14|#21170f|hook\.us2|Specials by email',s)
    print(f,len(s),'leftovers',bad,re.findall(r'(?i)lura|harmon|luravegas|poppins|00608a|0d2233|hive|penthouse|dec 28',s))
