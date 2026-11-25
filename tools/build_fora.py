"""Build the Fora LocalLift Live app (live/fora-50r1/v3/index.html).

Method: Lura v3 (live/lura-x5r9/v3, which already carries every Montage and Stillwater fix and the
Nov 24 UI and no gate flash fixes) is copied, every Lura content block is swapped for Fora
(objections, events, rival names, phone, links, storage keys, salt), the Lura blue palette is mapped
to Fora charcoal, clay and sand (from foravegas.com, as matched on the MoveInLocal Fora guide), and any
remaining Lura blue is swept into the Fora clay hue. Google blue for lead metrics is kept.
Usage: python3 tools/build_fora.py [APPV]"""
import re,subprocess,sys,os,colorsys,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
APPV=sys.argv[1] if len(sys.argv)>1 else '2026-11-24f1'
FOLDER='fora-50r1'
t=open(os.path.join(R,'live/lura-x5r9/v3/index.html')).read()
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
# ---- fonts: Fora uses Montserrat headings and Questrial text
sub('family=Poppins:wght@500;600;700;800','family=Montserrat:wght@500;600;700;800&family=Questrial',1)
t=t.replace('font-family:Poppins,','font-family:Montserrat,')
# ---- logo: Fora is a wide white wordmark
sub('.logo{height:46px;width:auto}','.logo{height:17px;width:auto}',1)
sub('.mclcl{position:absolute;left:10px;top:8px;height:30px;width:auto}','.mclcl{position:absolute;left:12px;top:13px;height:11px;width:auto}',1)
sub('#gate img{width:112px;','#gate img{width:150px;',1)
sub('.mcl{height:40px;width:auto;margin-bottom:6px;flex-shrink:0}','.mcl{height:15px;width:auto;margin-bottom:12px;flex-shrink:0}',1)
# ---- events (official pages)
rsub(r"const EV=\[.*?\]\];",r"""const EV=[['Dec 3 and 4','Henderson WinterFest','City of Henderson, details on the city page',0,484,'https://www.cityofhenderson.com/residents/special-interest/winterfest/'],['Dec 3 to 12','National Finals Rodeo','Thomas and Mack Center',0,492,'https://travelnevada.com/events/32227/national-finals-rodeo-las-vegas'],['Dec 4','City holiday tree lighting','Las Vegas Civic Center, 525 S. Main St., from 5 pm, tree lit at 6:10 pm',0,484,'https://content.govdelivery.com/accounts/NVLASVEGAS/bulletins/4307e89']];""")
# ---- objections and answers (Fora, Nevada; no legal claims beyond fair housing basics)
KIT=r"""const KIT=[
[LI('money'),'Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp}, and a 2027 move in gets 1 month free. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}. Which home would you like to look at first?',''],
['The deposit is too high.','Our deposit is $500. Let me pull up your full move in cost so you see the exact number before you decide.','Use the website pricing for the exact number. Never quote from memory.']],'o'],
[LI('swap'),'Comparing',[
['The Pearl has no rent until 2027 too.','They do run a similar offer. Their homes are smaller, so compare the size you need and the total each month. Here you get {sp}, free covered parking, a speakeasy lounge and coworking studios.','Agree first, then compare totals on the same lease term.'],
['Positano is cheaper.','Their base rents do start lower, at {po1} for a 1 bedroom, on smaller homes. Let’s compare totals and square feet side by side. Here you get {sp} and free covered parking.','Agree first, then compare. Never knock them.'],
['I’m also looking at Marlowe.','Great to compare. Ask what total monthly price they quoted and what parking costs. Here covered parking is free, and we have {sp}.','If they mention a special there, ask what they were quoted.'],
['I want to shop around.','Of course. Can I email you today’s offer and the homes you liked so you can compare side by side?','Get their email before they leave.']],'o'],
[LI('ruler'),'Size and fit',[
['Will my furniture fit?','Let’s find out together. I can pull the exact room sizes from the floor plan, and you’re welcome to measure. What’s the biggest piece you’re bringing?','Never guess a measurement. Use the floor plan.'],
['This closet is small.','Fair point. Let me show you the walk in closets, and we have on site storage available too. What do you need room for?','Don’t argue. Show the storage, then offer a fix.'],
['The homes feel small.','Let me show you our B2, a 1,379 square foot 2 bedroom, or our C1 three bedroom. Which rooms matter most to you?',''],
['We need more room.','Our C1 three bedroom is 1,453 square feet. Let me check if one is still open today.','The website showed only 1 C1 left. Check before you promise it.'],
['I need storage.','We have on site storage available, plus walk in closets, and some homes have a private balcony too.','']],'o'],
[LI('clock'),'Not ready yet',[
['I’ll think about it.','Totally fair. What’s the one thing holding you back? If it’s price, let’s pull up your exact total together right now.','Find the real reason, then answer that one thing.'],
['I need to talk to my partner first.','Of course. Can I send you both today’s offer and photos of the home you liked? When could you come back together?','Get a return time and their email.'],
['I’m not moving for a few months.','That works. Our website offer for a 2027 move in is 1 month free, and specials can change, so let’s at least find your favorite home now. What’s your ideal move date?','Never promise today’s special will still be here.'],
['I’m worried about getting approved.','I understand. Our manager can walk you through our written screening criteria so you know exactly what to expect before you apply.','Never guess if someone will qualify. Share the written criteria.'],
['I want a shorter lease.','We do offer short term leases, starting at a $200 monthly premium. Let me check what terms we have for the home you like.','Confirm lease terms and prices with your manager.']],'o'],
[LI('sound'),'The spot',[
['Is it noisy here?','Let’s step inside, close the windows and listen. I can also show you homes on different floors and sides of the building.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes face the mountains or the Strip, or sit on a higher floor.','']],'o'],
[LI('chat'),'First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the speakeasy lounge in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Our 1 bedroom homes start at {b1} base rent and 2 bedroom homes at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
[LI('card'),'Fees and specials',[
['What are the fees?','Our website shows the total monthly price with the required fees for every home, so let’s pull up yours together. No surprises.','Never quote a fee from memory.'],
['Is the special still going?','Yes. Move in now and pay $0 rent until 2027, or move in during 2027 for 1 month free. Want to see which homes qualify?','Select homes already have a reduced rent and do not get the extra free month. Check with your manager.'],
['Is internet included?','Every home is Cox internet and cable ready. Let me show you the exact monthly cost for the home you like.','Never promise internet is included.'],
['Do you have furnished homes?','Yes, we have furnished home options. Let me check which homes and what they cost.','Confirm the price with your manager.'],
['Do you work with employers?','Yes. Fora advertises extra savings for Preferred Employers and First Responders. Let me check what applies to you.','Confirm which homes qualify with your manager.']],'q'],
[LI('cal'),'Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
[LI('paw'),'Pets',[
['I have a big dog.','Bring them! We have no weight limits and allow up to 3 pets per home, though some breed restrictions apply. We also have a dog park and a pet spa.','Assistance animals are not pets: no pet rent or fees. Send those requests to your manager.'],
['What does a pet cost?','$50 a month pet rent per pet and a $500 pet fee per pet. Every pet needs a PetScreening profile.','']],'q'],
[LI('home'),'The community',[
['Where do I park?','Covered parking is free, and private VIP garage parking is available. We have four EV chargers too.','VIP garage price is not on the website. Ask the office.'],
['I work from home.','You’ll love our coworking studios and the business center with Cox internet, plus the Sky Lounge with mountain views.',''],
['How far is the Strip?','Fora says it is about 20 minutes to the Strip, UNLV and Harry Reid Airport, with quick I 15 and I 215 access.','Say about. Drive times change with traffic.'],
['Is it gated?','Yes. Fora is a controlled access gated community with interior corridors and elevators.',''],
['Do you speak Spanish?','Yes, we have Spanish speaking staff on our team. I can connect you.','']],'q'],
[LI('shield'),'Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features, like our controlled access gates.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
[LI('ok'),'Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""
i=t.find('const KIT=[');j=t.find("let kitTab='o';",i);assert i>0 and j>i
t=t[:i]+KIT+'\n'+t[j:]
sub(".replace(/{ja1}/g,f('Jade','1 bed from')).replace(/{ai1}/g,f('Ainsley at The Collective','1 bed from'))",".replace(/{pe1}/g,f('The Pearl at St. Rose','1 bed from')).replace(/{po1}/g,f('Positano','1 bed from'))",1)
sub("|jade|ainsley|collective|flatiron|","|pearl|positano|marlowe|",1)
sub('Numbers update every morning.','Prices and specials update every morning.',1)
t=t.replace(".replace(/\\b1 bedrooms\\b/g,'1 bedrooms')",".replace(/\\b1 bedrooms\\b/g,'1 bedroom')")
# ---- phone (number on foravegas.com), place
t=t.replace("(702) 935-6015","(725) 209-4665").replace('+17029356015','+17252094665').replace('7029356015','7252094665')
# ---- names, paths, keys, salt
t=t.replace('?v=l1','?v=f1')
t=re.sub(r"(['\"`])lllu-",r"\1llfo-",t)
t=t.replace("sha('lura:","sha('fora:")
t=t.replace('lura-x5r9',FOLDER).replace('LocalLift-Live-Lura-flyer','LocalLift-Live-Fora-flyer')
t=t.replace('review/lura','review/fora')
t=t.replace('meet/lura/','meet/fora/').replace('team/lura/','team/fora/').replace('live_lura','live_fora')
t=t.replace("live.thesocialdm.com/lura","live.thesocialdm.com/fora")
t=t.replace('Lura','Fora')
t=re.sub(r"'lura'","'fora'",t)
t=re.sub(r"([:=]\s*)lura\b",r"\1fora",t)
# ---- colors: Lura blue and grey to Fora charcoal, clay and sand
CM={'#075683':'#7c453d','#00608a':'#7c453d','#053f61':'#5e322b','#004466':'#5e322b','#0b4a6b':'#6a3a33','#8fcaec':'#e2b8a8','#8fd0ec':'#e2b8a8',
 '#dcecf5':'#f1e4de','#edf3f7':'#f6f2ef','#e8f2f8':'#f6ece7','#3d474d':'#4a4645','#5f6b74':'#6b6663','#12304a':'#2f2f30','#0d2233':'#1f1f20',
 '#07141f':'#141414','#163a56':'#3a3a3b','#2c3a45':'#3a3637','#1d4a66':'#5a2f29','#021e2f':'#171717','#032437':'#171717'}
t=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:CM.get(m.group(0).lower(),m.group(0)),t)
def conv(r,g,b_):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b_/255);hd=h*360
    if s>0.06 and 185<=hd<208.5:
        if l<0.22: H,S=0/360,min(s,0.05)
        elif l>0.86: H,S=22/360,min(s*0.5,0.35)
        else: H,S=8/360,min(s*0.6,0.38)
        R_,G_,B_=colorsys.hls_to_rgb(H,l,S);return (round(R_*255),round(G_*255),round(B_*255))
    return None
SW=collections.Counter()
def hexsw(m):
    k=m.group(0);x=k[1:]
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

# ---- Fora Editor fixes (Nov 24): no leftover blue on buttons and pills; clay primary, sand secondary, light and dark
FX="""<style id="forafx">
.prt,.lt .prt{background:#f3e5de!important;color:#7a4038!important}
.dskh svg{stroke:#7a4038!important}
.dskb button{background:#f3e5de!important;color:#7a4038!important}
.dskb button:first-child{background:linear-gradient(135deg,#7a4038,#5e2f2a)!important;color:#fff!important}
.mcsee{background:linear-gradient(135deg,#7a4038,#5e2f2a)!important;color:#fff!important;animation-name:foglow!important}
@keyframes foglow{0%,100%{box-shadow:0 0 0 0 rgba(122,64,56,.5),0 6px 18px rgba(122,64,56,.3)}50%{box-shadow:0 0 0 8px rgba(122,64,56,0),0 6px 22px rgba(122,64,56,.45)}}
#llnote button{background:linear-gradient(135deg,#7a4038,#5e2f2a)!important}#llnote .nk{color:#7a4038!important}
.akx span:not(.l){white-space:nowrap}
.akp.s{color:#7c453d!important;background:#f3e5de!important}
.flyb a:not(:first-child),.flyb button{background:#f3e5de!important;color:#7a4038!important}
@media (prefers-color-scheme:dark){.prt,.lt .prt,.dskb button{background:#f3e5de!important;color:#7a4038!important}.dskb button:first-child,.mcsee{background:linear-gradient(135deg,#7a4038,#5e2f2a)!important;color:#fff!important}.dskh svg{stroke:#e2b8a8!important}#llnote .nk{color:#e2b8a8!important}.akp.s{background:rgba(124,69,61,.35)!important;color:#e2b8a8!important}.flyb a:not(:first-child),.flyb button{background:rgba(124,69,61,.35)!important;color:#f3e5de!important}}
@media (prefers-reduced-motion:reduce){.mcsee{animation:none!important}}
</style>"""
t=open(SP).read()
if 'id="forafx"' not in t:
    i=t.rfind('</body>');t=t[:i]+FX+t[i:]
open(SP,'w').write(t)
t=open(SP).read()
print('built',len(t),'APPV',APPV,'swept',sum(SW.values()))
bad=re.findall(r'(?i)montage|tigard|oregon|stillwater|kissimmee|florida|lura|coya|harmon|the hive|jade|ainsley|flatiron|poppins|\(702\)|702[ -]\d{3}|lllu|x5r9',t)
print('leftovers',collections.Counter(bad))
