"""Build the Lura LocalLift Live app (live/lura-x5r9/v3/index.html).

Method (same as Stillwater, one step further): the Stillwater app is the three way port of Montage v3
(tools/build_stillwater.py). Lura starts from that port, takes the Montage changes made after it
(gate code box accepts personal codes, 8256c9e), swaps every Stillwater content block for Lura
(objections, events, rivals, phone, links, storage keys, salt), maps the teal palette to Lura blue
and grey, then sweeps any remaining teal or warm color into the Lura hue.
Usage: python3 tools/build_lura.py [APPV]"""
import re,subprocess,sys,os,colorsys,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
APPV=sys.argv[1] if len(sys.argv)>1 else '2026-11-24u2'
FOLDER='lura-x5r9'
def gs(ref,p): return subprocess.run(['git','-C',R,'show',f'{ref}:{p}'],capture_output=True,text=True,check=True).stdout
t=open(os.path.join(R,'live/stillwater-k4p7/v3/index.html')).read()  # current Stillwater port (keeps its latest fixes)
def sub(a,b,cnt=None):
    global t
    n=t.count(a)
    if n==0: raise SystemExit('missing: '+a[:90])
    if cnt is not None and n!=cnt: raise SystemExit(f'count {n}!={cnt}: '+a[:90])
    t=t.replace(a,b)
def rsub(pat,rep,cnt=1):
    global t
    t2,n=re.subn(pat,rep,t,flags=re.S)
    if n!=cnt: raise SystemExit(f'regex {n}!={cnt}: '+pat[:90])
    t=t2
t=re.sub(r"const APPV='[^']*'",f"const APPV='{APPV}'",t)
# ---- Montage change after the Stillwater port (8256c9e): gate takes personal codes
if 'Your manager has the team code.</p>' in t: sub('Your manager has the team code.</p>','Your code is in your welcome email.</p>',1)
if '<label for="gc">Team code</label>' in t: sub('<label for="gc">Team code</label><input id="gc" inputmode="numeric" autocomplete="one-time-code" required>','<label for="gc">Your code</label><input id="gc" inputmode="text" autocapitalize="none" autocorrect="off" spellcheck="false" autocomplete="one-time-code" required>',1)
# ---- fonts: Lura uses Poppins
sub('family=Belgrano&family=Montserrat:wght@500;600;700;800','family=Poppins:wght@500;600;700;800',1)
sub('#gate h2{font-family:Belgrano,Georgia,serif;font-weight:400;letter-spacing:0}','#gate h2{font-family:Poppins,-apple-system,system-ui,sans-serif;font-weight:600;letter-spacing:-.01em}',1)
sub('.desk b{font-family:Montserrat,','.desk b{font-family:Poppins,',1)
# ---- logo: Lura mark is round, not a wide wordmark
sub('.logo{height:22px;filter:brightness(0) invert(1)}','.logo{height:46px;width:auto}',1)
sub('.mclcl{position:absolute;left:12px;top:12px;height:14px;filter:brightness(0) invert(1)}','.mclcl{position:absolute;left:10px;top:8px;height:30px;width:auto}',1)
sub('#gate img{width:160px;','#gate img{width:112px;',1)
sub('.mcl{height:20px;filter:brightness(0) invert(1);margin-bottom:10px}','.mcl{height:40px;width:auto;margin-bottom:6px;flex-shrink:0}.mcc .mca,.mcc .mcph{flex-shrink:0}',1)
# ---- events (official pages)
rsub(r"const EV=\[.*?\]\];",r"""const EV=[['Dec 3 to 12','National Finals Rodeo','Thomas and Mack Center',0,492,'https://travelnevada.com/events/32227/national-finals-rodeo-las-vegas'],['Dec 3 to 12','Cowboy Christmas','Las Vegas Convention Center, South Hall, 9 am to 4 pm daily',0,492,'https://aws.nfrexperience.com/news/cowboy-christmas-gift-show-partners-with-texas-precious-metals-as-its-new-presenting-sponsor-in-2026'],['Dec 4','City holiday tree lighting','Las Vegas Civic Center, 525 S. Main St., from 5 pm, tree lit at 6:10 pm',0,484,'https://content.govdelivery.com/accounts/NVLASVEGAS/bulletins/4307e89']];""")
# ---- objections and answers (Lura, Nevada; no legal claims beyond fair housing basics)
KIT=r"""const KIT=[
['💲','Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp}, plus up to $2,000 in Look and Lease savings when you move in by Dec 28. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}, plus up to $2,000 in Look and Lease savings. Which home would you like to look at first?',''],
['The deposit is too high.','Let me pull up your full move in cost so you see the exact number. Some communities add admin and cleaning fees on top, so it’s worth comparing the total.','Use the website pricing for the exact number. Never quote from memory.']],'o'],
['⚔️','Comparing',[
['Ainsley has 10 weeks free.','They do run a big special. Ask what total monthly price they quoted, since they add set monthly charges plus admin and cleaning fees. Here you get {sp}, a walk to the Strip and free gated garage parking.','Agree first, then compare totals on the same lease term.'],
['Jade is cheaper.','Their 1 bedrooms do start lower on base rent, at {ja1}, and their monthly charges are added on top. Let’s compare totals side by side. Here you get {sp} and free gated garage parking.','Agree first, then compare. Never knock them.'],
['I’m also looking at Flatiron.','Great to compare. Ask which homes their 1 month free covers and the total monthly price. Right now we have {sp}.','If they mention a special there, ask what they were quoted.'],
['I want to shop around.','Of course. Can I email you today’s offer and the homes you liked so you can compare side by side?','Get their email before they leave.']],'o'],
['📏','Size and fit',[
['Will my furniture fit?','Let’s find out together. I can pull the exact room sizes from the floor plan, and you’re welcome to measure. What’s the biggest piece you’re bringing?','Never guess a measurement. Use the floor plan.'],
['This closet is small.','Fair point. Let me show you the walk in closets in our other plans. What do you need room for?','Don’t argue. Show the storage, then offer a fix.'],
['The homes feel small.','Let me show you one of our 2 bedrooms or a penthouse home. Which rooms matter most to you?',''],
['We need more room.','Our C2 three bedroom is 1,383 square feet. Let me check today’s pricing and move in date for you.','Check the move in date first. The website lists the C2 for a later date.'],
['I need storage.','Let me show you the closet space in each plan, and some homes have a private patio or balcony too.','']],'o'],
['⏳','Not ready yet',[
['I’ll think about it.','Totally fair. What’s the one thing holding you back? If it’s price, let’s pull up your exact total together right now.','Find the real reason, then answer that one thing.'],
['I need to talk to my partner first.','Of course. Can I send you both today’s offer and photos of the home you liked? When could you come back together?','Get a return time and their email.'],
['I’m not moving for a few months.','That works. Today’s offer needs a move in by Dec 28, and specials can change, so let’s at least find your favorite home now. What’s your ideal move date?','Never promise today’s special will still be here.'],
['I’m worried about getting approved.','I understand. Our manager can walk you through our written screening criteria so you know exactly what to expect before you apply.','Never guess if someone will qualify. Share the written criteria.'],
['I want a shorter lease.','Today’s special is on a 12 month lease. Let me check what other lease terms we have and what each one costs.','Never promise a lease term. Check with your manager.']],'o'],
['🔊','The spot',[
['Is it noisy here?','Let’s step inside, close the windows and listen. I can also show you homes on different floors and sides of the building.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes face the Strip or sit on a higher floor. We also have premium top floor homes.','']],'o'],
['👋','First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the Sky Lounge in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Our 1 bedrooms start at {b1} base rent and 2 bedrooms at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
['💳','Fees and specials',[
['What are the fees?','Our website shows the total monthly price with the required fees for every home, so let’s pull up yours together. No surprises.','Never quote a fee from memory.'],
['Is the special still going?','Yes: {sp}, plus up to $2,000 in Look and Lease savings when you move in by Dec 28. Want to see which homes qualify?','Check which homes qualify with your manager.'],
['Is internet included?','Every home is internet and cable ready with Cox. Let me show you the exact monthly cost for the home you like.','Never promise internet is included.'],
['Do you work with employers?','Ask me about our Preferred Employer Partnership Program. I’ll check the details for your employer.','Confirm the details with your manager.']],'q'],
['📅','Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
['🐾','Pets',[
['I have a big dog.','Bring them! We have no weight limits and allow up to 3 pets per home, though some breed restrictions apply. We also have outdoor pet relief areas.','Assistance animals are not pets: no pet rent or fees. Send those requests to your manager.'],
['What does a pet cost?','$50 a month pet rent per pet, a $500 one time pet fee per pet, and no pet deposit. Every pet needs a PetScreening profile.','']],'q'],
['🏡','The community',[
['Where do I park?','Parking is free in our gated garage with controlled access, and VIP parking upgrades are available. We have EV charging too.','VIP parking price is not on the website. Ask the office.'],
['I work from home.','You’ll love The Hive, our coworking space, plus the clubhouse and the Sky Lounge with Strip views.',''],
['How far is the Strip?','You can walk to the Strip over the Harmon Bridge, right from here. Want me to show you the way out?',''],
['Do you speak Spanish?','Yes, we have Spanish speaking staff on our team. I can connect you.','']],'q'],
['⚖️','Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features, like our controlled access garage.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
['🤝','Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""
i=t.find('const KIT=[');j=t.find("let kitTab='o';",i);assert i>0 and j>i
t=t[:i]+KIT+'\n'+t[j:]
sub(".replace(/{cv1}/g,f('Cielo View','1 bed from')).replace(/{mo1}/g,f('Mosaic at Lake Toho','1 bed from')).replace(/{ja1}/g,f('The Jamison','1 bed from'))",".replace(/{ja1}/g,f('Jade','1 bed from')).replace(/{ai1}/g,f('Ainsley at The Collective','1 bed from'))",1)
sub("|cielo|jamison|mosaic|","|jade|ainsley|collective|flatiron|",1)

# ---- line icons, not emoji, on the Found us tiles and the objection categories
IC={'phone':'<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 18h2"/>','pin':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>','search':'<circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/>','ai':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M18.5 15.5l.6 1.7 1.7.6-1.7.6-.6 1.7-.6-1.7-1.7-.6 1.7-.6z"/>','bldg':'<rect x="5" y="3" width="14" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>','play':'<rect x="3" y="6" width="18" height="12" rx="3"/><path d="m10 9.5 4.5 2.5-4.5 2.5z"/>','ad':'<path d="M4 10v4h3l8 4V6l-8 4z"/><path d="M18 9.5a3.5 3.5 0 0 1 0 5"/>','web':'<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>','people':'<circle cx="9" cy="8" r="3"/><path d="M3 20a6 6 0 0 1 12 0"/><circle cx="17" cy="9" r="2.5"/><path d="M15.5 14.2A5 5 0 0 1 21 19"/>','car':'<path d="M4 15l1.5-5a2 2 0 0 1 1.9-1.5h9.2a2 2 0 0 1 1.9 1.5L20 15v3H4z"/><circle cx="7.5" cy="15" r="1.2"/><circle cx="16.5" cy="15" r="1.2"/>','home':'<path d="M3 11 12 4l9 7v9H3z"/><path d="M9 20v-6h6v6"/>','chat':'<path d="M4 5h16v11H9l-5 4z"/>','money':'<circle cx="12" cy="12" r="9"/><path d="M15 9.5c-.5-1-1.6-1.5-3-1.5-1.7 0-3 .8-3 2s1.3 1.7 3 2 3 .8 3 2-1.3 2-3 2c-1.4 0-2.5-.5-3-1.5M12 6v2M12 16v2"/>','swap':'<path d="M7 7h11l-3-3M17 17H6l3 3"/>','ruler':'<rect x="3" y="8" width="18" height="8" rx="1"/><path d="M7 8v3M11 8v4M15 8v3M19 8v2"/>','clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>','sound':'<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/>','card':'<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18M7 15h3"/>','cal':'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/>','paw':'<circle cx="7" cy="10" r="1.8"/><circle cx="10.5" cy="6.5" r="1.8"/><circle cx="14.5" cy="6.5" r="1.8"/><circle cx="17.5" cy="10" r="1.8"/><path d="M12 12c-3 0-5 3-5 5 0 1.5 1.5 2 2.5 2 1 0 1.5-.5 2.5-.5s1.5.5 2.5.5c1 0 2.5-.5 2.5-2 0-2-2-5-5-5z"/>','shield':'<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6z"/>','ok':'<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.5 2.5L16 9.5"/>'}
import json as _j
sub("const HEARD=[","const LIC="+_j.dumps(IC)+";const LI=n=>'<svg class=\"lic\" viewBox=\"0 0 24 24\" aria-hidden=\"true\">'+LIC[n]+'</svg>';\nconst HEARD=[",1)
for e,n,lab in [('💲','money','Price'),('⚔️','swap','Comparing'),('📏','ruler','Size and fit'),('⏳','clock','Not ready yet'),('🔊','sound','The spot'),('👋','chat','First hello'),('💳','card','Fees and specials'),('📅','cal','Holds and move in'),('🐾','paw','Pets'),('🏡','home','The community'),('⚖️','shield','Careful questions'),('🤝','ok','Closing')]:
    sub(f"['{e}','{lab}',[",f"[LI('{n}'),'{lab}',[",1)
for e,n in [('📱','phone'),('📍','pin'),('🔎','search'),('🤖','ai'),('🏢','bldg'),('▶️','play'),('📣','ad'),('💻','web'),('🤝','people'),('🚗','car'),('🏠','home'),('💬','chat')]:
    sub(f"['{e}','",f"[LI('{n}'),'",1)

t=t.replace('</style>','.lic{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;vertical-align:-4px;color:#00608a}.hrd .lic{width:24px;height:24px;display:block;margin:0 auto 4px}@media (prefers-color-scheme:dark){.lic{color:#8fd0ec}}</style>',1)

# ---- phone, place, links
sub("const MC_PHONE='(689) 314-6918';","const MC_PHONE='(702) 935-6015';",1)
sub("${MC_PHONE} · Kissimmee, FL","${MC_PHONE} · Las Vegas, NV",1)
sub(' <div class="rv-tbl"><div class="rv-r rv-hd"><span class="rv-p">Plan</span><span class="rv-t">Them</span><span class="rv-m">Stillwater Lakes</span></div>${rows}</div>',' ${rows?`<div class="rv-tbl"><div class="rv-r rv-hd"><span class="rv-p">Plan</span><span class="rv-t">Them</span><span class="rv-m">Stillwater Lakes</span></div>${rows}</div>`:\'\'}',1)
# ---- event tile: Lura slate grey (no maroon)
sub('.c4{background:linear-gradient(145deg,#6b2e2e,#361717)}','.c4{background:linear-gradient(145deg,#5f6b74,#2c3a45)}',1)
# ---- names, paths, keys, salt
sub('content="Stillwater Live"','content="Lura Live"',1)
sub("short_name:'Stillwater Live'","short_name:'Lura Live'",1)
t=t.replace('?v=s2','?v=l1')
t=re.sub(r"(['\"`])llsw-",r"\1lllu-",t)
t=t.replace("sha('stillwater:","sha('lura:")
t=t.replace('stillwater-k4p7',FOLDER).replace('LocalLift-Live-Stillwater-Lakes-flyer','LocalLift-Live-Lura-flyer')
t=t.replace('review/stillwater-lakes','review/lura').replace("'stillwater-lakes'","'lura'")
t=t.replace('meet/stillwater/','meet/lura/').replace('team/stillwater/','team/lura/').replace('live_stillwater','live_lura')
t=t.replace("'https://live.thesocialdm.com/stillwater'","'https://live.thesocialdm.com/lura'")
t=t.replace("property:'stillwater'","property:'lura'").replace("app:'stillwater'","app:'lura'")
t=t.replace('Stillwater Lakes','Lura').replace('Stillwater','Lura')
t=re.sub(r"'stillwater'","'lura'",t)
# ---- colors: Stillwater teal to Lura blue and grey
CM={'#0b5560':'#00608a','#003840':'#004466','#0a1d22':'#0d2233','#0f2a31':'#12304a','#134650':'#0b4a6b','#8fbac0':'#8fd0ec',
 '#daeaec':'#dcecf5','#e9f0f1':'#edf3f7','#071518':'#07141f','#12323a':'#163a56','#1d4650':'#1d4a66','#2b3a3d':'#2c3a45','#4f5c5f':'#5f6b74'}
t=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:CM.get(m.group(0).lower(),m.group(0)),t)
LH=202/360
def conv(r,g,b_):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b_/255);hd=h*360
    if s>0.06 and (165<=hd<200 or 15<=hd<=50):
        R_,G_,B_=colorsys.hls_to_rgb(LH,l,min(s,0.9));return (round(R_*255),round(G_*255),round(B_*255))
    return None
SW=collections.Counter()
KEEP={'#fbbc04','#f9ab00','#ffb400','#f5b301','#fbbf24','#f59e0b','#ffcc00','#ffd60a','#ff9f0a','#ff9500','#e37400','#ea8600'}
def hexsw(m):
    k=m.group(0);x=k[1:]
    if k.lower() in KEEP: return k
    if len(x)==3: x=''.join(c*2 for c in x)
    n=conv(int(x[0:2],16),int(x[2:4],16),int(x[4:6],16))
    if n: v='#%02x%02x%02x'%n;SW[k+'->'+v]+=1;return v
    return k
def rgbsw(m):
    k=m.group(0);p=[q.strip() for q in m.group(2).split(',')]
    try: r,g,b_=[int(float(q)) for q in p[:3]]
    except: return k
    n=conv(r,g,b_)
    if n: v=f"{m.group(1)}({n[0]},{n[1]},{n[2]}"+(','+','.join(p[3:]) if len(p)>3 else '')+')';SW[k+'->'+v]+=1;return v
    return k
t=re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b(?![0-9a-fA-F])',hexsw,t)
t=re.sub(r'(rgba?)\(([^)]*)\)',rgbsw,t)
os.makedirs(os.path.join(R,'live',FOLDER,'v3'),exist_ok=True)
SP=os.path.join(R,'live',FOLDER,'v3','index.html')
open(SP,'w').write(t)
open(os.path.join(R,'live',FOLDER,'v3','version.txt'),'w').write(APPV+'\n')
subprocess.run([sys.executable,os.path.join(R,'tools/app_ui_fix_nov24.py'),SP],check=True)
t=open(SP).read()
print('built',len(t),'APPV',APPV,'swept',sum(SW.values()))
bad=re.findall(r'(?i)montage|tigard|oregon|stillwater|kissimmee|florida|orlando|cielo|jamison|mosaic|toho|belgrano|partin|\(689\)|689[ -]\d{3}|\(971\)',t)
print('leftovers',collections.Counter(bad))
