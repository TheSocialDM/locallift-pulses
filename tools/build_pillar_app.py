"""Build a Pillar Communities LocalLift Live app from the Huxley Scottsdale v3 (live/huxley-h7k2/v3, the first Pillar app,
with Ava as page assistant and every fix through Nov 25 2026). Swaps every Huxley content block (objections, events,
rival names, phone, links, storage keys, salt), maps the Pillar red palette to the property's own colors.
Usage: python3 tools/build_pillar_app.py cuvee|elevation-santan [APPV]
Add a property: add a CFG entry (key, folder, salt, storage prefix, colors, KIT, EV, rivals for {r1}/{r2})."""
import re,sys,os,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
KEY=sys.argv[1]

KIT_CUVEE=r"""const KIT=[
[LI('money'),'Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp}. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}. Which home would you like to look at first?',''],
['The move in costs are too high.','Let me pull up the full move in cost for the home you like so you see the exact number before you decide.','Use the Lease Cost Calculator on the website or ask your manager. Never quote a fee from memory.']],'o'],
[LI('swap'),'Comparing',[
['Broadstone Westgate gives 12 weeks free.','They do advertise up to 12 weeks free with a move in by Nov 30. Let’s compare the total you’d pay on the same lease term and size. Here you get {sp}, a rooftop terrace over Westgate and two resort style pools.','Agree first, then compare totals on the same lease term. Never knock them.'],
['Glen 91 is cheaper.','Their average 1 bedroom asks a bit less, at {r2}. Let’s compare what you get side by side: our two story fitness center, rooftop terrace, game lawn with a putting green and pet spa.','Agree first, then compare. Never knock them.'],
['I’m also looking at Prose Desert River.','Great to compare. Ask what total monthly price they quoted and which homes their special covers. Here you have {sp}.','If they mention a special there, ask what they were quoted.'],
['I want to shop around.','Of course. Can I send you today’s offer and the homes you liked so you can compare side by side?','Get their email or number before they leave.']],'o'],
[LI('ruler'),'Size and fit',[
['Will my furniture fit?','Let’s find out together. I can pull the exact room sizes from the floor plan, and you’re welcome to measure. What’s the biggest piece you’re bringing?','Never guess a measurement. Use the floor plan.'],
['The homes feel small.','Let me show you a few floor plans side by side so you can pick the layout that works best. Which rooms matter most to you?','Check today’s availability on the website before you promise a plan.'],
['We need more room.','Let me check which 2 bedroom homes are open today.','Check availability before you promise a home.']],'o'],
[LI('clock'),'Not ready yet',[
['I’ll think about it.','Totally fair. What’s the one thing holding you back? If it’s price, let’s pull up your exact total together right now.','Find the real reason, then answer that one thing.'],
['I need to talk to my partner first.','Of course. Can I send you both today’s offer and photos of the home you liked? When could you come back together?','Get a return time and their contact.'],
['I’m not moving for a few months.','That works. Specials can change, so let’s at least find your favorite home now. What’s your ideal move date?','Never promise today’s special will still be here.'],
['I’m worried about getting approved.','I understand. Our manager can walk you through our written screening criteria so you know exactly what to expect before you apply.','Never guess if someone will qualify. Share the written criteria.'],
['I want a shorter lease.','Let me check what lease terms we have for the home you like.','Confirm lease terms and prices with your manager.']],'o'],
[LI('sound'),'The spot',[
['Is it noisy on game nights?','We’re close to Westgate and State Farm Stadium. Let me show you homes on different sides of the building so you can pick what fits you.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes sit on a different side or a higher floor.','']],'o'],
[LI('chat'),'First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the rooftop terrace in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Our 1 bedroom homes start at {b1} and 2 bedroom homes at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
[LI('card'),'Fees and specials',[
['What are the fees?','Let’s pull up the full cost for the home you like together, so there are no surprises.','Use the Lease Cost Calculator on the website. Never quote a fee from memory.'],
['Is the special still going?','Yes, today it’s {sp}. Want to see which homes and lease terms qualify?','Check which homes and terms qualify with your manager.'],
['Is internet included?','Let me check exactly what’s included for the home you like.','Never promise internet is included.']],'q'],
[LI('cal'),'Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
[LI('paw'),'Pets',[
['I have a dog.','Bring them! We have a dog park with areas for large and small dogs and a pet spa with a grooming station. Up to 2 pets per home. Let me pull up our full pet policy for you.','Assistance animals are not pets: no pet rent or fees. Send those requests to your manager. Weight limits and breed restrictions apply.'],
['What does a pet cost?','Let me pull up our current pet fees and policy so you get the exact numbers.','Never quote pet fees from memory.']],'q'],
[LI('home'),'The community',[
['Where do I park?','We have covered parking, and garage parking you can rent. Let me check what’s available for the home you like.','Check parking availability and price with the office.'],
['What do I get here?','A two story fitness center with a yoga room and spin, two resort style pools with firepits and cabanas, a game room and a game lawn with a putting green.',''],
['What’s around here?','We’re next to the Westgate Entertainment District and State Farm Stadium, with Tanger Outlets close by.','Say close by or minutes away. Drive times change with traffic.'],
['What do residents do for fun?','Sunsets on the rooftop terrace over Westgate, the game room with air hockey and shuffleboard, and the pools.','']],'q'],
[LI('shield'),'Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
[LI('ok'),'Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""

KIT_ES=r"""const KIT=[
[LI('money'),'Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp}. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}. Which home would you like to look at first?',''],
['The move in costs are too high.','Let me pull up the full move in cost for the home you like so you see the exact number before you decide.','Use the Lease Cost Calculator on the website or ask your manager. Never quote a fee from memory.']],'o'],
[LI('swap'),'Comparing',[
['The Flats is right across the way.','They are close by, and they advertise up to 8 weeks free on select homes. Let’s compare the total you’d pay on the same lease term and size. Here you get {sp}, a fourth floor sky lounge and a two level fitness center.','Agree first, then compare totals on the same lease term. Never knock them.'],
['Redstone is cheaper.','Their average 1 bedroom asks less, at {r2}. Let’s compare what you get side by side: the sky lounge, two gated dog parks and garages on select homes.','Agree first, then compare. Never knock them.'],
['SanTan by Baron gives a free garage.','They do advertise a garage offer with their special. Ask what total they were quoted. Here you have {sp}, and single and double car garages on select homes.','If they mention a special there, ask what they were quoted.'],
['I want to shop around.','Of course. Can I send you today’s offer and the homes you liked so you can compare side by side?','Get their email or number before they leave.']],'o'],
[LI('ruler'),'Size and fit',[
['Will my furniture fit?','Let’s find out together. I can pull the exact room sizes from the floor plan, and you’re welcome to measure. What’s the biggest piece you’re bringing?','Never guess a measurement. Use the floor plan.'],
['The homes feel small.','Our ceilings run 9 to 11 feet, so homes feel open. Let me show you a few floor plans side by side. Which rooms matter most to you?','Check today’s availability on the website before you promise a plan.'],
['Do you have studios?','Yes, studios start at {st}. Want to see one?','Check availability before you promise a home.']],'o'],
[LI('clock'),'Not ready yet',[
['I’ll think about it.','Totally fair. What’s the one thing holding you back? If it’s price, let’s pull up your exact total together right now.','Find the real reason, then answer that one thing.'],
['I need to talk to my partner first.','Of course. Can I send you both today’s offer and photos of the home you liked? When could you come back together?','Get a return time and their contact.'],
['I’m not moving for a few months.','That works. Specials can change, so let’s at least find your favorite home now. What’s your ideal move date?','Never promise today’s special will still be here.'],
['I’m worried about getting approved.','I understand. Our manager can walk you through our written screening criteria so you know exactly what to expect before you apply.','Never guess if someone will qualify. Share the written criteria.'],
['I want a shorter lease.','For shorter lease terms, let me check with the office for the home you like.','The website says to call the office for shorter terms. Confirm prices with your manager.']],'o'],
[LI('sound'),'The spot',[
['Is it noisy here?','Let’s step inside and listen. Our corridors are climate controlled, and I can show you homes on different floors and sides.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes sit on a different side or a higher floor.','']],'o'],
[LI('chat'),'First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the sky lounge in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Studios start at {st}, 1 bedroom homes at {b1} and 2 bedroom homes at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
[LI('card'),'Fees and specials',[
['What are the fees?','Let’s pull up the full cost for the home you like together, so there are no surprises.','Use the Lease Cost Calculator on the website. Never quote a fee from memory.'],
['Is the special still going?','Yes, today it’s {sp}. Want to see which homes and lease terms qualify?','Check which homes and terms qualify with your manager.'],
['Is internet included?','Each home comes with a Cox modem already installed. Let me check exactly what’s included for the home you like.','Never promise internet service is included.']],'q'],
[LI('cal'),'Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
[LI('paw'),'Pets',[
['I have a dog.','Bring them! We have two gated dog parks and a pet wash and grooming room. Up to 2 pets per home. Let me pull up our full pet policy for you.','Assistance animals are not pets: no pet rent or fees. Send those requests to your manager.'],
['What does a pet cost?','Let me pull up our current pet fees and policy so you get the exact numbers.','Never quote pet fees from memory.']],'q'],
[LI('home'),'The community',[
['Where do I park?','We have covered parking, plus single and double car garages on select homes. Let me check what’s available for the home you like.','Check garage availability with the office.'],
['I work from home.','You’ll like the lounge with built in workstations and the resident conference center.',''],
['What’s around here?','You can walk to SanTan Village for shopping, restaurants and entertainment.',''],
['What do residents do for fun?','The fourth floor sky lounge, the resort style pool and spa with cabanas, and the fire pit and grills.','']],'q'],
[LI('shield'),'Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
[LI('ok'),'Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""

# EV rows: [date label, title, place, 0, END key (month+1)*40+day, Jan to Sep +12, official url]
CFG={
 'cuvee':dict(name='Cuvee',full='Cuvee',folder='cuvee-c6v2',salt='cuvee',pre='llcv',v='c1',app='cuvee',
   phone=('(833) 897-3859','+18338973859','8338973859'),city='Glendale, AZ',city2='Glendale',
   kit=KIT_CUVEE,r1=('Broadstone Westgate','1 bed average'),r2=('Glen 91','1 bed average'),
   syn='|broadstone|westgate|glen 91|glen|prose|desert river|',
   ev="""const EV=[['Nov 27 and 28','Glendale Glitters kickoff weekend','Murphy Park, Historic Downtown Glendale, 5 to 10 pm, free',0,508,'https://www.glendaleaz.gov/Explore/Special-Events/Glendale-Glitters'],['Nov 27 to Jan 1','Glendale Glitters holiday lights','Murphy Park, Historic Downtown Glendale, nightly 5 to 10 pm, free',0,561,'https://www.glendaleaz.gov/Explore/Special-Events/Glendale-Glitters']];""",
   cm={'#c8241d':'#7b2340','#9a1b16':'#5a1830','#a81f19':'#6a1e37','#7a1712':'#46121f','#f2a49f':'#e3a6b8','#fbe9e7':'#f8e9ee','#fbefed':'#faf0f3'},
   rgba='rgba(123,35,64,',dark='#ff8fb0'),
 'elevation-santan':dict(name='Elevation SanTan',full='Elevation SanTan',folder='elevation-santan-e3t8',salt='elevation-santan',pre='lles',v='e1',app='elevation_santan',
   phone=('(480) 605-0338','+14806050338','4806050338'),city='Gilbert, AZ',city2='Gilbert',
   kit=KIT_ES,r1=('The Flats At SanTan','1 bed average'),r2=('Redstone at SanTan Village','1 bed average'),
   syn='|flats|the flats|redstone|baron|santan by baron|town commons|zaterra|',
   ev="""const EV=[['Sat, Dec 5','Tumbleweed Tree Lighting and Parade of Lights','Downtown Chandler, from 4:30 pm, parade 6:45 pm, tree lighting about 8 pm, free',0,525,'https://www.chandleraz.gov/explore/special-events/tumbleweed-tree-lighting-ceremony'],['Dec 11 to 22','Riparian After Dark holiday lights','Riparian Preserve at Water Ranch, 5:30 to 9 pm, $5 tickets online',0,542,'https://www.gilbertaz.gov/departments/parks-and-recreation/special-events-and-permits/riparian-after-dark']];""",
   cm={'#c8241d':'#2b5f87','#9a1b16':'#1d4361','#a81f19':'#245273','#7a1712':'#132f45','#f2a49f':'#9cc3e0','#fbe9e7':'#e8f1f8','#fbefed':'#eef5fa'},
   rgba='rgba(43,95,135,',dark='#8cc4ef'),
}
C=CFG[KEY]
APPV=sys.argv[2] if len(sys.argv)>2 else '2026-11-25'+C['v'][0]+'1'
t=open(os.path.join(R,'live/huxley-h7k2/v3/index.html')).read()
def sub(a,b,cnt=None):
    global t
    n=t.count(a)
    if n==0: raise SystemExit('missing: '+a[:90])
    if cnt is not None and n!=cnt: raise SystemExit(f'count {n}!={cnt}: '+a[:90])
    t=t.replace(a,b)
t=re.sub(r"const APPV='[^']*'",f"const APPV='{APPV}'",t)
# events
t,n=re.subn(r"const EV=\[.*?\]\];",lambda m:C['ev'],t,count=1,flags=re.S);assert n==1
# objections and answers
i=t.find('const KIT=[');j=t.find("let kitTab='o';",i);assert i>0 and j>i
t=t[:i]+C['kit']+'\n'+t[j:]
sub(".replace(/{bs1}/g,f('Broadstone Scottsdale Quarter','1 bed average')).replace(/{co1}/g,f('The Core Scottsdale','1 bed average'))",
    f".replace(/{{r1}}/g,f('{C['r1'][0]}','{C['r1'][1]}')).replace(/{{r2}}/g,f('{C['r2'][0]}','{C['r2'][1]}'))",1)
sub("|broadstone|the core|core scottsdale|residences kierland|kierland|",C['syn'],1)
# phone
t=t.replace("(480) 771-8082",C['phone'][0]).replace('+14807718082',C['phone'][1]).replace('4807718082',C['phone'][2])
# keys, paths, names
t=t.replace('?v=h1','?v='+C['v'])
t=re.sub(r"(['\"`])llhx-",r"\1"+C['pre']+"-",t)
t=t.replace("sha('huxley:","sha('"+C['salt']+":")
t=t.replace('huxley-h7k2',C['folder']).replace('LocalLift-Live-Huxley-flyer','LocalLift-Live-'+C['name'].replace(' ','-')+'-flyer')
t=t.replace('review/huxley','review/'+KEY).replace('meet/huxley/','meet/'+KEY+'/').replace('team/huxley/','team/'+KEY+'/').replace('live_huxley','live_'+C['app'])
t=t.replace("live.thesocialdm.com/huxley","live.thesocialdm.com/"+KEY)
t=t.replace('huxleyscottsdale.com','<<SITE>>')
t=t.replace('Huxley Scottsdale',C['full']).replace('Scottsdale, AZ',C['city'])
t=t.replace('Huxley',C['name'])
t=re.sub(r"'huxley'","'"+KEY+"'",t)
t=re.sub(r"([:=]\s*)huxley\b",r"\g<1>"+KEY,t)
t=t.replace('<<SITE>>',{'cuvee':'livecuvee.com','elevation-santan':'elevationsantan.com'}[KEY])
# colors
t=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:C['cm'].get(m.group(0).lower(),m.group(0)),t)
t=t.replace('rgba(200,36,29,',C['rgba']).replace('#ff7a6e',C['dark'])
# sweep: muted warm browns left from the FORE builds (tiles, Tour button, kit icons) move to the property hue.
# Saturated reds stay: they mean warning or "they win" everywhere in the app.
import colorsys
PH=colorsys.rgb_to_hls(*[int(C['cm']['#c8241d'][i:i+2],16)/255 for i in (1,3,5)])[0]
def sweep(m):
    h=m.group(0);r,g,b=[int(h[i:i+2],16)/255 for i in (1,3,5)];hh,l,s=colorsys.rgb_to_hls(r,g,b)
    if s<0.08 or s>0.52 or not (hh<0.12 or hh>0.93): return h
    r,g,b=colorsys.hls_to_rgb(PH,l,min(s*1.1,0.55));return '#%02x%02x%02x'%(round(r*255),round(g*255),round(b*255))
t=re.sub(r'#[0-9a-fA-F]{6}\b',sweep,t)
# ---- Editor fixes Nov 25 (gate FAIL, then fixed)
t,n=re.subn(r'<section class="w"><div class="wt"><b>🖨️ Print and place</b>.*?</section>','',t,count=1,flags=re.S)
if not os.path.isdir(os.path.join(R,'live',C['folder'],'print')): assert n==1,'print section'
sub("n.textContent=\"Prices come from each community's own website and can change daily. Lowest listed base rent; confirm lease terms before quoting.\"","n.textContent=\"Rival rents are average asking rents in the market data. Confirm lease terms before quoting.\"",1)
sub('<b>Google reviews</b><span>${esc(D.rivals.date)}</span>','<b>Review site ratings</b><span>${esc(D.rivals.date)}</span>',1)
sub('.o1,span.o1,.akl,.mctap,.lt .prt{','.o1,span.o1,.akl,.mctap{',1)
t=t.replace('</body>','<style>@media (max-width:360px){.akx span.h{white-space:normal!important;hyphens:manual;overflow-wrap:break-word}}</style></body>',1)
sub('.mcflip{background:#1c1c1e}','.mcflip{background:#1c1c1e;color:'+C['cm']['#f2a49f']+';border-color:'+C['cm']['#f2a49f']+'}',1)
os.makedirs(os.path.join(R,'live',C['folder'],'v3'),exist_ok=True)
open(os.path.join(R,'live',C['folder'],'v3','index.html'),'w').write(t)
open(os.path.join(R,'live',C['folder'],'v3','version.txt'),'w').write(APPV+'\n')
print('built',KEY,len(t),'APPV',APPV)
bad=re.findall(r'(?i)huxley|scottsdale|kierland|broadstone scottsdale|the core|raintree|miele|billiards|h7k2|llhx|\(480\) 771|\bmia\b|montage|fora\b|vegas',t)
print('leftovers',collections.Counter(b.lower() for b in bad))
