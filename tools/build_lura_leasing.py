"""Builds team/lura/leasing/ (agent page, card sample, qr.svg) from team/montage/leasing in Lura brand.
Prices and specials come from live/lura-x5r9/data.json (talk, compete.us). The Specials by email opt in is
left out: its delivery automation is Montage only, and no form ships without automated delivery."""
import os,re,json,io,segno
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
SRC=os.path.join(R,'team/montage/leasing');DST=os.path.join(R,'team/lura/leasing')
os.makedirs(os.path.join(DST,'card'),exist_ok=True)
D=json.load(open(os.path.join(R,'live/lura-x5r9/data.json')))
T=D['talk'];U=D['compete']['us'];chk=T['checked']
pr={l:v for v,l in T['prices']}
SITE='https://www.luravegas.com'
TEL='+17029356015';PH='(702) 935-6015'
MAPS='https://www.google.com/maps/search/?api=1&amp;query=Lura+Vegas+Apartments+3240+W+Harmon+Ave+Las+Vegas+NV'
FONT='<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">'
COL={'#21170f':'#0d2233','#6e6155':'#5f6b74','#e6dccf':'#d6e2ea','#b46e26':'#00608a','#2a1d14':'#12304a','#f3ece2':'#edf3f7','#e3d6c6':'#cfdbe3',
 'rgba(20,12,6,':'rgba(6,16,24,','rgba(30,20,12,':'rgba(6,16,24,','rgba(42,29,20,':'rgba(13,34,51,','rgba(33,23,15,':'rgba(13,34,51,',
 '#e0a463':'#8fd0ec','#d8cbbb':'#cfdbe3','#7e4815':'#004466','#e9e0d4':'#e1eaf0','#efe4d6':'#e1eaf0'}
def recolor(t):
    for a,b in COL.items(): t=t.replace(a,b)
    return t
def mia(t,up):
    # keep the Mia guide, point it at Lura
    t=re.sub(r'data-property="[^"]*"','data-property="Lura"',t)
    t=t.replace('the Montage leasing team','the Lura leasing team')
    t=t.replace('https://www.montagetigard.com/scheduletour',SITE+'/scheduletour').replace('https://www.montagetigard.com/floorplans',SITE+'/floorplans')
    t=t.replace('tel:+19713977861','tel:'+TEL).replace('data-color="#b46e26"','data-color="#00608a"')
    return t
# ---------- agent page
t=open(os.path.join(SRC,'index.html')).read()
head,body=t.split('<body>',1)
script_mia=re.search(r'<script src="\.\./\.\./\.\./guide/guide\.js.*?</script>',body,re.S).group(0)
css=re.search(r'<style>(.*?)</style>',head,re.S).group(1)
css=re.sub(r'\.opt[^{]*\{[^}]*\}\n?','',css)  # opt in styles not needed
css=css.replace('live/montage-r8x2/hero.jpg','live/lura-x5r9/hero.jpg')
css=recolor(css)
css+="h1,h2,h3{font-family:Poppins,Inter,system-ui,sans-serif;font-weight:600;letter-spacing:-.01em}.plan b,.plan .pr,.offer small{font-family:Poppins,Inter,system-ui,sans-serif}.hero .logo{height:58px;width:auto}.me img{width:70%;height:auto}.ft img{height:64px;width:auto}\n"
sp=U.get('specialShort') or T['offer']
offer_p='Plus up to $2,000 in Look and Lease savings. Move in by Dec 28. The leasing team confirms which homes qualify.' if 'Look and Lease' in T['offer'] else 'The leasing team confirms which homes qualify.'
plans=[('1 bedroom',pr.get('1 bed base rent from')),('2 bedroom',pr.get('2 bed base rent from')),('Penthouse',pr.get('penthouse base rent from'))]+[(m[1],m[0]) for m in T.get('more',[])]
plan_html=''.join(f'<div class="plan"><b>{n}</b><div class="pr">{v}<i>starting at</i></div><span>Base rent</span></div>' for n,v in plans if v)
show=U['showoff']
page=f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Lura in Las Vegas · Your leasing team</title>
<meta property="og:title" content="Lura in Las Vegas · Homes, today's special and your tour">
<meta property="og:description" content="See available homes, current specials and book your tour at Lura in Las Vegas.">
<meta property="og:image" content="https://thesocialdm.github.io/locallift-pulses/live/lura-x5r9/hero.jpg">
<meta property="og:type" content="website">
<meta name="description" content="Your leasing team at Lura in Las Vegas. Book a tour, see homes and today's specials.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONT}
<style>{css}</style></head><body>
<main class="pf">
  <div class="hero"><img class="logo" src="../../../live/lura-x5r9/logo-white.png" alt="Lura"></div>
  <section class="card">
    <div class="me"><img src="../../../live/lura-x5r9/logo-white.png" alt=""></div>
    <h1 id="who">Lura Leasing Team</h1>
    <div class="role" id="role">Your leasing contacts at <b>Lura in Las Vegas</b></div>
    <div class="btns">
      <a href="tel:{TEL}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>Call</a>
      <a href="{SITE}/scheduletour" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>Tour</a>
      <a href="{MAPS}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>Directions</a>
      <a href="{SITE}/floorplans" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11 12 4l9 7v9H3z"/><path d="M9 20v-6h6v6"/></svg>Homes</a>
    </div>
    <div class="stack">
      <a class="btn cu" href="{SITE}/scheduletour" target="_blank" rel="noopener" id="bkt">Book my tour</a>
      <a class="btn" id="vcf" href="#" download="Lura-Leasing.vcf">Save Lura to my contacts</a>
      <button class="btn" id="share" type="button">Send this to a roommate</button>
      <a class="btn" href="{SITE}/" target="_blank" rel="noopener">Visit luravegas.com</a>
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
    <p class="sub">1, 2 and 3 bedrooms and penthouse homes. See every available home with one tap.</p>
    <div class="plans" id="plans">{plan_html}</div>
    <p class="asof" id="asof">Starting base rents from luravegas.com on {chk}, 2026, and they change often. <a href="{SITE}/floorplans" target="_blank" rel="noopener">See every home live</a></p>
  </section>

  <section class="sec">
    <h2>Life at Lura</h2>
    <p class="sub">{', '.join(s if (i==0 or s.split()[0] in ('Sky','The','EV','BBQ')) else s[0].lower()+s[1:] for i,s in enumerate(show[:5]))}.</p>
    <div class="gal">
      <figure><img src="../../../live/lura-x5r9/shots/outside.jpg" alt="Lura apartment with city views at night"><figcaption>City views</figcaption></figure>
      <figure><img src="../../../live/lura-x5r9/shots/lounge.jpg" alt="Lura Sky Lounge"><figcaption>Sky Lounge</figcaption></figure>
      <figure><img src="../../../live/lura-x5r9/shots/kitchen.jpg" alt="Lura apartment kitchen"><figcaption>Kitchens</figcaption></figure>
      <figure><img src="../../../live/lura-x5r9/shots/cowork.jpg" alt="The Hive coworking at Lura"><figcaption>The Hive coworking</figcaption></figure>
    </div>
  </section>

  <section class="sec">
    <h2>Nearby</h2>
    <ul class="near">
      <li>The Las Vegas Strip<span>walk over the Harmon Bridge</span></li>
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

  <div class="ft"><img src="../../../live/lura-x5r9/logo-umber.png" alt="Lura"><br>Lura · 3240 W Harmon Ave, Las Vegas, NV<br>{PH} · Equal Housing Opportunity<br>Powered by LocalLift</div>
</main>
<div class="toast" id="toast" role="status"></div>
<script>
(function(){{try{{var q=new URLSearchParams(location.search),n=(q.get('by')||'').replace(/[^A-Za-z .'\\-]/g,'').trim();if(!n||/^team$/i.test(n)){{try{{n=sessionStorage.getItem('llsw-by')||''}}catch(x){{}}}}if(!n||/^team$/i.test(n))return;n=n.replace(/\\b\\w/g,function(c){{return c.toUpperCase()}}).slice(0,30);try{{sessionStorage.setItem('llsw-by',n)}}catch(x){{}}
document.getElementById('who').textContent=n+' at Lura';document.getElementById('role').innerHTML='Your leasing consultant at <b>Lura in Las Vegas</b>';document.getElementById('bkt').textContent='Book my tour with '+n;document.title=n+' at Lura · Las Vegas';window.llBy=n}}catch(x){{}}}})();
(function(){{
var $=function(s){{return document.querySelector(s)}};
var toast=function(m){{var t=$('#toast');t.textContent=m;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){{t.classList.remove('show')}},3200)}};
var url=location.href.split('#')[0];
var v='BEGIN:VCARD\\r\\nVERSION:3.0\\r\\nFN:'+(window.llBy?window.llBy+', Lura Leasing (Las Vegas)':'Lura Leasing Team (Las Vegas)')+'\\r\\nORG:Lura\\r\\nTITLE:Leasing\\r\\nTEL;TYPE=WORK:{TEL}\\r\\nADR;TYPE=WORK:;;3240 W Harmon Ave;Las Vegas;NV;89103;USA\\r\\nURL:'+url+'\\r\\nEND:VCARD\\r\\n';
$('#vcf').href='data:text/vcard;charset=utf-8,'+encodeURIComponent(v);
$('#share').addEventListener('click',function(){{var d={{title:'Lura in Las Vegas',text:'Take a look at Lura with me.',url:url}};if(navigator.share){{navigator.share(d).catch(function(){{}})}}else{{navigator.clipboard.writeText(url).then(function(){{toast('Link copied. Paste it in a text.')}},function(){{toast(url)}})}}}});
// live prices and special from the morning refresh
fetch('../../../live/lura-x5r9/data.json',{{cache:'no-store'}}).then(function(r){{return r.json()}}).then(function(d){{var t=d&&d.talk,u=d&&d.compete&&d.compete.us;if(!t)return;
 var s=u&&u.specialShort||'';if(s&&!/no special/i.test(s)){{$('#offH').textContent=s;$('#offP').textContent=/Look and Lease/.test(t.offer||'')?'Plus up to $2,000 in Look and Lease savings. Move in by Dec 28. The leasing team confirms which homes qualify.':'The leasing team confirms which homes qualify.'}}else if(/no special/i.test(t.offer||'')){{$('#offH').textContent='Ask about this month\\'s specials';$('#offP').textContent='Specials change often. The leasing team will share what is available today.'}}
 var m={{'1 bed base rent from':'1 bedroom','2 bed base rent from':'2 bedroom','penthouse base rent from':'Penthouse'}},h='';(t.prices||[]).forEach(function(p){{if(m[p[1]])h+='<div class="plan"><b>'+m[p[1]]+'</b><div class="pr">'+p[0]+'<i>starting at</i></div><span>Base rent</span></div>'}});(t.more||[]).forEach(function(p){{h+='<div class="plan"><b>'+p[1]+'</b><div class="pr">'+p[0]+'<i>starting at</i></div><span>Base rent</span></div>'}});if(h)$('#plans').innerHTML=h;
 if(t.checked)$('#asof').firstChild.textContent='Starting base rents from luravegas.com on '+t.checked+', 2026, and they change often. '}}).catch(function(){{}});
}})();
</script>
{mia(script_mia,3)}
</body></html>
'''
open(os.path.join(DST,'index.html'),'w').write(page)
# ---------- QR (agent page, team link)
QURL='https://thesocialdm.github.io/locallift-pulses/team/lura/leasing/?src=qr'
q=segno.make(QURL,error='m');b=io.BytesIO();q.save(b,kind='svg',dark='#0d2233',light='#fff',border=2,xmldecl=False,svgns=True,svgclass='segno',lineclass='qrline',omitsize=True)
qsvg=b.getvalue().decode()
open(os.path.join(DST,'qr.svg'),'w').write(qsvg)
# ---------- card sample
c=open(os.path.join(SRC,'card/index.html')).read()
c=re.sub(r'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 41 41".*?</svg>',qsvg,c,flags=re.S)
c=c.replace('meet/montage/','meet/lura/').replace('live/montage-r8x2','live/lura-x5r9').replace('shots/lobby.jpg','shots/lounge.jpg')
c=c.replace('<title>Montage Leasing · QR business card (sample)</title>','<title>Lura Leasing · QR business card (sample)</title>')
c=c.replace('Montage leasing card (sample)','Lura leasing card (sample)')
c=c.replace('open the live Montage profile for your leasing consultant','open the live Lura profile for your leasing consultant')
c=c.replace('<b id="cn">Montage Leasing Team</b><span>Montage in Tigard</span>','<b id="cn">Lura Leasing Team</b><span>Lura in Las Vegas</span>')
c=c.replace('<span class="ph">(971) 397-7861</span><span>13155 SW 68th Parkway, Tigard</span>',f'<span class="ph">{PH}</span><span>3240 W Harmon Ave, Las Vegas</span>')
c=c.replace('<b>Your home near Washington Square</b><span>Sky lounge · Pool and spa · Golf simulator · Coworking</span>','<b>Your home by the Strip</b><span>Sky Lounge · Pool · Free garage parking · Coworking</span>')
c=c.replace('Open the live Montage profile','Open the live Lura profile').replace('alt="Montage"','alt="Lura"')
c=c.replace('<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">',FONT)
c=recolor(c);c=mia(c,4)
c=c.replace('.front .logo{height:8%;position:absolute;top:10%;left:7%}','.front .logo{height:22%;position:absolute;top:8%;left:6%}')
c=c.replace('h1{font:700 20px Montserrat,sans-serif;margin:0}','h1{font:600 21px Poppins,Inter,sans-serif;margin:0}')
open(os.path.join(DST,'card/index.html'),'w').write(c)
for f in ['index.html','card/index.html']:
    s=open(os.path.join(DST,f)).read()
    bad=re.findall(r'(?i)montage|stillwater|kissimmee|tigard|oregon|washington square|971|overland|steward|mercato|#b46e26|#2a1d14|#21170f|hook\.us2|Specials by email',s)
    print(f,len(s),'leftovers',bad)
