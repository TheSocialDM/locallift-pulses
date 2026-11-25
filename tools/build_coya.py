"""Build the COYA LocalLift Live app (live/coya-3zep/v3/index.html).
Method: the Lura app (tools/build_lura.py, latest fixes through 2026-11-24u4) is the base. Every Lura content block is
swapped for COYA (objections, rivals, phone, links, storage keys, salt), the Lura blue and grey palette maps to COYA plum,
sage and sand (from the COYA logo and coyaliving.com), then any remaining Lura blue is swept into the COYA hue.
Google blue (#1a73e8 family) stays for the lead bars. Usage: python3 tools/build_coya.py [APPV]"""
import re,subprocess,sys,os,colorsys,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
APPV=sys.argv[1] if len(sys.argv)>1 else '2026-11-24c1'
FOLDER='coya-3zep'
t=open(os.path.join(R,'live/lura-x5r9/v3/index.html')).read()
def sub(a,b,cnt=None):
    global t
    n=t.count(a)
    if n==0: raise SystemExit('missing: '+a[:90])
    if cnt is not None and n!=cnt: raise SystemExit(f'count {n}!={cnt}: '+a[:90])
    t=t.replace(a,b)
t=re.sub(r"const APPV='[^']*'",f"const APPV='{APPV}'",t)
# ---- fonts: COYA uses Montserrat headings, Lato body
sub('family=Poppins:wght@500;600;700;800','family=Montserrat:wght@500;600;700;800',1)
t=t.replace('font-family:Poppins,','font-family:Montserrat,')
# ---- logo: COYA badge is wide (about 1.7 to 1)
sub('.logo{height:46px;width:auto}','.logo{height:34px;width:auto}',1)
sub('.mclcl{position:absolute;left:10px;top:8px;height:30px;width:auto}','.mclcl{position:absolute;left:10px;top:9px;height:22px;width:auto}',1)
sub('#gate img{width:112px;','#gate img{width:150px;',1)
sub('.mcl{height:40px;width:auto;margin-bottom:6px;flex-shrink:0}','.mcl{height:30px;width:auto;margin-bottom:8px;flex-shrink:0}',1)
# ---- objections and answers (COYA, Nevada; only facts from coyaliving.com, read Nov 24 2026; no legal claims)
KIT=r"""const KIT=[
['💲','Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp}, and rents are falling on select homes. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}. Are you a first responder, or do you work for one of our partner employers? Those savings stack on top.','Confirm who qualifies with your manager.'],
['The deposit is too high.','Let me pull up your full move in cost so you see the exact number. Some communities add admin and cleaning fees on top, so it’s worth comparing the total.','Use the website pricing for the exact number. Never quote from memory.']],'o'],
['⚔️','Comparing',[
['Ainsley has 10 weeks free.','They do run a big special. Ask what total monthly price they quoted, since they add a $300 admin fee and a $250 cleaning fee at move in, plus about $162 a month in required charges and a $65 membership fee. Here you get {sp}, a $0 pet fee and the Sky Lounge with Strip views.','Agree first, then compare totals on the same lease term.'],
['Jade is cheaper.','Their 1 bedrooms do start lower on base rent, at {ja1}, and their monthly charges are added on top. Let’s compare totals side by side. Here you get {sp}, plus a pet spa and dog park.','Agree first, then compare. Never knock them.'],
['I’m also looking at Green Leaf Lotus.','Great to compare, they’re right around the corner. Ask what total monthly price and lease term they quoted. Right now we have {sp}.','If they mention a special there, ask what they were quoted.'],
['I want to shop around.','Of course. Can I email you today’s offer and the homes you liked so you can compare side by side?','Get their email before they leave.']],'o'],
['📏','Size and fit',[
['Will my furniture fit?','Let’s find out together. I can pull the exact room sizes from the floor plan, and you’re welcome to measure. What’s the biggest piece you’re bringing?','Never guess a measurement. Use the floor plan.'],
['This closet is small.','Fair point. Our homes have walk in closets, and I can show you the plans with the most storage. What do you need room for?','Don’t argue. Show the storage, then offer a fix.'],
['The homes feel small.','Let me show you one of our 2 bedrooms or our 3 bedroom. With 10 foot ceilings they feel bigger in person. Which rooms matter most to you?',''],
['We need more room.','Our C2 three bedroom is about 1,477 to 1,543 square feet. Let me check today’s pricing and move in date for you.','Check the move in date for that home first.'],
['We are roommates.','Every 2 bedroom here has two baths. Let me show you the 2 bedroom plans and split the price two ways for you.','']],'o'],
['⏳','Not ready yet',[
['I’ll think about it.','Totally fair. What’s the one thing holding you back? If it’s price, let’s pull up your exact total together right now.','Find the real reason, then answer that one thing.'],
['I need to talk to my partner first.','Of course. Can I send you both today’s offer and photos of the home you liked? When could you come back together?','Get a return time and their email.'],
['I’m not moving for a few months.','That works. Specials can change, so let’s at least find your favorite home now. What’s your ideal move date?','Never promise today’s special will still be here.'],
['I’m worried about getting approved.','I understand. Our manager can walk you through our written rental qualifications so you know exactly what to expect before you apply.','Never guess if someone will qualify. Share the written criteria.'],
['I want a shorter lease.','We do offer short term leases for a small monthly premium. Let me check which terms fit your home and what each one costs.','Check the exact premium with your manager before quoting it.']],'o'],
['🔊','The spot',[
['Is it noisy here?','Let’s step inside, close the windows and listen. I can also show you homes on different floors and sides of the building.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes sit higher or face the Strip. And everyone gets the Sky Lounge views.','']],'o'],
['👋','First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the Sky Lounge in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Our 1 bedrooms start at {b1} base rent and 2 bedrooms at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
['💳','Fees and specials',[
['What are the fees?','Our website shows the total monthly price with the required fees for every home, so let’s pull up yours together. No surprises.','Never quote a fee from memory.'],
['Is the special still going?','Yes: {sp}. Want to see which homes qualify?','Check which homes qualify with your manager.'],
['Is internet included?','Every home is internet and cable ready with Cox. Let me show you the exact monthly cost for the home you like.','Never promise internet is included.'],
['Do you work with employers?','Yes, ask me about our Preferred Employer savings. First responders get savings too, and both stack with Look and Lease.','Confirm the details with your manager.']],'q'],
['📅','Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
['🐾','Pets',[
['I have a big dog.','Bring them! We have no weight limits and allow up to 3 pets per home, though some breed restrictions apply. We also have a pet spa and a dog park.','Assistance animals are not pets: no pet rent or deposits. Send those requests to your manager.'],
['What does a pet cost?','$50 a month pet rent per pet, a $300 refundable pet deposit per pet, and no pet fee. Every pet needs a PetScreening profile.','']],'q'],
['🏡','The community',[
['Where do I park?','Residents have reserved covered parking, and the community is gated with controlled access. We have EV charging too.','Parking cost is not on the website. Ask the office.'],
['I work from home.','You’ll love our co working space, plus the Club Room and the Sky Lounge with Strip views.',''],
['How far is the Strip?','We’re in Chinatown, just west of the Strip, so it’s minutes away. Want to see the view from the Sky Lounge?','Never quote a drive time. It depends on the hour.'],
['Do you speak Spanish?','Yes, we have Spanish speaking staff on our team. I can connect you.','']],'q'],
['⚖️','Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features, like our gated, controlled access entry.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
['🤝','Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""
i=t.find('const KIT=[');j=t.find("let kitTab='o';",i);assert i>0 and j>i
# Lura already converted category emoji to icons; rebuild that step for the new KIT
KIT2=KIT
for e,n,lab in [('💲','money','Price'),('⚔️','swap','Comparing'),('📏','ruler','Size and fit'),('⏳','clock','Not ready yet'),('🔊','sound','The spot'),('👋','chat','First hello'),('💳','card','Fees and specials'),('📅','cal','Holds and move in'),('🐾','paw','Pets'),('🏡','home','The community'),('⚖️','shield','Careful questions'),('🤝','ok','Closing')]:
    assert f"['{e}','{lab}',[" in KIT2,lab
    KIT2=KIT2.replace(f"['{e}','{lab}',[",f"[LI('{n}'),'{lab}',[")
t=t[:i]+KIT2+'\n'+t[j:]
sub(".replace(/{ja1}/g,f('Jade','1 bed from')).replace(/{ai1}/g,f('Ainsley at The Collective','1 bed from'))",".replace(/{ja1}/g,f('Jade','1 bed from')).replace(/{ai1}/g,f('Ainsley at The Collective','1 bed from'))",1)
sub("|jade|ainsley|collective|flatiron|","|jade|ainsley|collective|lotus|green leaf|",1)
sub("replace('2 months free','<em>2 months free</em>')","replace('Look and Lease','<em>Look and Lease</em>')")
# ---- phone (coyaliving.com), place
sub("const MC_PHONE='(702) 935-6015';","const MC_PHONE='(702) 605-6291';",1)
# ---- event tile: COYA sage
sub('.c4{background:linear-gradient(145deg,#5f6b74,#2c3a45)}','.c4{background:linear-gradient(145deg,#7d8f8f,#465555)}',1)
# ---- names, paths, keys, salt
sub('content="Lura Live"','content="COYA Live"',1)
sub("short_name:'Lura Live'","short_name:'COYA Live'",1)
t=t.replace('?v=l1','?v=c1')
t=re.sub(r"(['\"`])lllu-",r"\1llco-",t)
t=t.replace("sha('lura:","sha('coya:")
t=t.replace('lura-x5r9',FOLDER).replace('LocalLift-Live-Lura-flyer','LocalLift-Live-COYA-flyer')
t=t.replace('review/lura','review/coya').replace("'lura'","'coya'")
t=t.replace('meet/lura/','meet/coya/').replace('team/lura/','team/coya/').replace('live_lura','live_coya')
t=t.replace("'https://live.thesocialdm.com/lura'","'https://live.thesocialdm.com/coya'")
t=t.replace("property:'lura'","property:'coya'").replace("app:'lura'","app:'coya'")
t=t.replace('Lura','COYA')
# ---- colors: Lura blue and grey to COYA plum, sage and sand
CM={'#00608a':'#633f40','#004466':'#4f3132','#0d2233':'#2e1d1e','#12304a':'#3f2728','#0b4a6b':'#563637','#8fd0ec':'#dcbfc0',
 '#dcecf5':'#efe6e4','#edf3f7':'#f6f3f0','#07141f':'#140c0c','#163a56':'#4a3031','#1d4a66':'#5a3b3c','#2c3a45':'#2b2b2b','#5f6b74':'#6c6a66',
 '#075683':'#633f40','#053f61':'#4f3132','#8fcaec':'#dcbfc0','#3d474d':'#454141','#cfdbe3':'#e3d9d5','#d6e2ea':'#e8dfdb','#e1eaf0':'#efe9e6'}
t=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:CM.get(m.group(0).lower(),m.group(0)),t)
CH=358/360
def conv(r,g,b_):
    h,l,s=colorsys.rgb_to_hls(r/255,g/255,b_/255);hd=h*360
    if s>0.06 and 188<=hd<=208.5:
        R_,G_,B_=colorsys.hls_to_rgb(CH,l,min(s,0.30 if l<0.5 else 0.28));return (round(R_*255),round(G_*255),round(B_*255))
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
# ---- Editor fixes (Nov 24): no zero count tiles; COYA plum and rose instead of blue on the renters button, Print pill, desk card and notes
sub("const mcStats=()=>`<div class=\"mcst\"><div><b>${mcN(/^Card opened/)}</b><span>Card opens</span></div><div><b>${mcN(/^QR shown|^Card opened/)}</b><span>QR shown</span></div><div><b>${mcN(/^Sent/)}</b><span>Cards sent</span></div></div>`;",
 "const mcStats=()=>{const t=[[mcN(/^Card opened/),'Card opens'],[mcN(/^QR shown|^Card opened/),'QR shown'],[mcN(/^Sent/),'Cards sent']].filter(x=>x[0]>0);return t.length?`<div class=\"mcst\" style=\"grid-template-columns:repeat(${t.length},1fr)\">${t.map(x=>`<div><b>${x[0]}</b><span>${x[1]}</span></div>`).join('')}</div>`:`<p class=\"mcst0\" style=\"margin:12px 0 0;font-size:14px;color:#6c6a66\">Show or send your card and your counts show up here.</p>`};",1)
sub('<div class="mine" style="grid-template-columns:1fr"><div><b>${row?row[1]:0}</b><span>residents opened Google from your code this month</span></div></div>',
 '${row&&+row[1]>0?`<div class="mine" style="grid-template-columns:1fr"><div><b>${row[1]}</b><span>residents opened Google from your code this month</span></div></div>`:\'\'}',1)
for a,b in [('background:linear-gradient(135deg,#1a73e8,#4c8df6)!important','background:linear-gradient(135deg,#633f40,#a06a6c)!important'),
 ('background:linear-gradient(135deg,#2f6fe0,#5b9bff)!important','background:linear-gradient(135deg,#7a5152,#b8888a)!important'),
 ('rgba(26,115,232,.55),0 6px 18px rgba(26,115,232,.35)','rgba(160,106,108,.55),0 6px 18px rgba(99,63,64,.35)'),
 ('rgba(26,115,232,.5),0 6px 18px rgba(26,115,232,.3)}50%{box-shadow:0 0 0 8px rgba(26,115,232,0),0 8px 26px rgba(26,115,232,.55)','rgba(160,106,108,.5),0 6px 18px rgba(99,63,64,.3)}50%{box-shadow:0 0 0 8px rgba(160,106,108,0),0 8px 26px rgba(99,63,64,.55)'),
 ('background:#eef4fe;color:#1a5fd0;font:700 14px','background:#efe6e4;color:#633f40;font:700 14px'),
 ('.lt .prt{background:#22324d;color:#a9c8ff}','.lt .prt{background:#3f2728;color:#dcbfc0}'),
 ('.dskh svg{flex:none;width:30px;height:30px;stroke:#1a73e8','.dskh svg{flex:none;width:30px;height:30px;stroke:#633f40'),
 ('background:#eef4fe;color:#1a5fd0;cursor:pointer','background:#efe6e4;color:#633f40;cursor:pointer'),
 ('.dskb button:first-child{grid-column:1/-1;background:#1a73e8;color:#fff}','.dskb button:first-child{grid-column:1/-1;background:#633f40;color:#fff}'),
 ('.dskb button{background:#22324d;color:#a9c8ff}','.dskb button{background:#3f2728;color:#dcbfc0}'),
 ('text-transform:uppercase;color:#1a73e8}#llnote h3','text-transform:uppercase;color:#633f40}#llnote h3'),
 ('#llnote button{width:100%;min-height:48px;border:0;border-radius:14px;background:#1a73e8','#llnote button{width:100%;min-height:48px;border:0;border-radius:14px;background:#633f40')]:
    sub(a,b)
t=t.replace('Numbers update every morning','Prices and specials update every morning')
os.makedirs(os.path.join(R,'live',FOLDER,'v3'),exist_ok=True)
SP=os.path.join(R,'live',FOLDER,'v3','index.html')
open(SP,'w').write(t)
open(os.path.join(R,'live',FOLDER,'v3','version.txt'),'w').write(APPV+'\n')
subprocess.run([sys.executable,os.path.join(R,'tools/app_ui_fix_nov24.py'),SP],check=True)
t=open(SP).read()
print('built',len(t),'APPV',APPV,'swept',sum(SW.values()))
bad=re.findall(r'(?i)montage|tigard|oregon|stillwater|kissimmee|florida|orlando|lura|fora\b|harmon|flatiron|poppins|luravegas|\(689\)|\(971\)|935-6015|#00608a|#0d2233',t)
print('leftovers',collections.Counter(bad))
