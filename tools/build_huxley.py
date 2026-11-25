"""Build the Huxley Scottsdale LocalLift Live app (live/huxley-h7k2/v3/index.html). First Pillar Communities app.

Method: Fora v3 (live/fora-50r1/v3, the newest FORE build with every Montage, Stillwater, Lura and COYA fix) is copied,
every Fora content block is swapped for Huxley (objections, events, rival names, phone, links, storage keys, salt),
the Fora clay palette is mapped to Pillar red and charcoal (as on the Huxley sample page for Melanie), and the page
assistant is Ava (Pillar) instead of Mia (FORE). Google blue for lead metrics is kept.
Usage: python3 tools/build_huxley.py [APPV]"""
import re,subprocess,sys,os,collections
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
APPV=sys.argv[1] if len(sys.argv)>1 else '2026-11-25h1'
FOLDER='huxley-h7k2'
t=open(os.path.join(R,'live/fora-50r1/v3/index.html')).read()
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
# ---- fonts: Montserrat headings, Inter text (as on the Huxley page for Melanie)
sub('family=Montserrat:wght@500;600;700;800&family=Questrial','family=Montserrat:wght@500;600;700;800&family=Inter:wght@400;500;600',1)
# ---- events (official pages only)
rsub(r"const EV=\[.*?\]\];",r"""const EV=[['Nov 27 to Dec 30','Holiday Lights at the Railroad Park','McCormick-Stillman Railroad Park, 5:30 to 9:30 pm, closed Dec 24 and 25',0,484,'https://therailroadpark.com/event/holiday-lights/']];""")
# ---- objections and answers (Huxley, Arizona; prices fill in live from data.json)
KIT=r"""const KIT=[
[LI('money'),'Price',[
['It’s over my budget.','Totally fair. Let’s look at what you’d really pay. Right now we have {sp} on select lease terms. Want me to pull up your exact monthly total?','Run the numbers together. Never guess.'],
['Can you do any better?','The best offer we have today is {sp}. Which home would you like to look at first?',''],
['The move in costs are too high.','Let me pull up the full move in cost for the home you like so you see the exact number before you decide.','Use the website or your manager for the exact number. Never quote a fee from memory.']],'o'],
[LI('swap'),'Comparing',[
['Broadstone gives 3 months free.','They do advertise up to 3 months free, tied to leasing within 48 hours of your tour. Let’s compare the total you’d pay on the same lease term and size. Here you get {sp}, a work from home lounge with private offices and a rooftop deck.','Agree first, then compare totals on the same lease term. Never knock them.'],
['The Core is cheaper.','Their average 1 bedroom asks less, at {co1}. Let’s compare what you get for it side by side: our rooftop deck, billiards room, pet spa and gated garage parking.','Agree first, then compare. Never knock them.'],
['I’m also looking at Residences Kierland.','Great to compare. Ask what total monthly price they quoted and which homes their special covers. Here you have {sp}.','If they mention a special there, ask what they were quoted.'],
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
['I want a shorter lease.','Let me check what lease terms we have for the home you like, since our offer is on select lease terms.','Confirm lease terms and prices with your manager.']],'o'],
[LI('sound'),'The spot',[
['Is it noisy here?','Let’s step inside, close the windows and listen. I can also show you homes on different floors and sides of the building.','Never promise it will be quiet.'],
['I don’t love this view.','Let me check which open homes sit on a different side or a higher floor.','']],'o'],
[LI('chat'),'First hello',[
['Just looking around.','Perfect, looking is the best way to start. I can show you a model and the rooftop deck in about ten minutes, no pressure. What brought you by today?','Ask one question before you show anything.'],
['On the phone: what’s your cheapest?','Our 1 bedroom homes start at {b1} and 2 bedroom homes at {b2}. Right now we have {sp}. When are you hoping to move?','Always end with a question.'],
['I only have a few minutes.','No problem, I’ll show you the one home that fits you best. How many bedrooms are you looking for?','']],'q'],
[LI('card'),'Fees and specials',[
['What are the fees?','Let’s pull up the full cost for the home you like together, so there are no surprises.','Never quote a fee from memory.'],
['Is the special still going?','Yes, today it’s {sp}. Want to see which homes and lease terms qualify?','Check which homes and terms qualify with your manager.'],
['Is internet included?','Let me check exactly what’s included for the home you like.','Never promise internet is included.']],'q'],
[LI('cal'),'Holds and move in',[
['Can you hold a home for me?','Let me check what holding options we have today.','Never promise a hold. Check with your manager.'],
['When can I move in?','Let me check the exact move in date for the home you like.','Check the move in date for that home before you say it.']],'q'],
[LI('paw'),'Pets',[
['I have a dog.','Bring them! We’re pet friendly, with a pet spa and grooming station and a dog park. Let me pull up our pet policy and fees for you.','Assistance animals are not pets: no pet rent or fees. Send those requests to your manager.'],
['What does a pet cost?','Let me pull up our current pet fees and policy so you get the exact numbers.','Never quote pet fees from memory.']],'q'],
[LI('home'),'The community',[
['Where do I park?','We have gated garage parking. Let me check what’s available for the home you like.','Parking prices are not on the website. Ask the office.'],
['I work from home.','You’ll love our work from home lounge with personal offices, plus a conference room with a Miele coffee bar.',''],
['What’s around here?','We’re a few minutes by car from Scottsdale Quarter and Kierland Commons, with quick Loop 101 access.','Say minutes by car. Drive times change with traffic.'],
['What do residents do for fun?','There’s a rooftop deck with grills, a billiards room and a resort style pool and spa.','']],'q'],
[LI('shield'),'Careful questions',[
['Is this a safe area?','Safety means different things to everyone, so I’d encourage you to look at local resources and visit at different times. I’m happy to show you the community and its features, like our gated garage.','Fair housing: never describe how safe a neighborhood is.'],
['What kind of people live here?','Everyone is welcome here. I’m happy to tell you about our amenities and community spaces.','Fair housing: never describe who lives here.'],
['How are the schools?','The school district’s website has the most current information, so that is the best place to check.','Fair housing: don’t rate schools.'],
['Is this a good place for kids?','Every home here is open to everyone. I’m happy to show you the homes and spaces that fit what you need.','Fair housing: never steer families toward or away from any home or floor.'],
['Do you take housing vouchers?','Let me connect you with my manager so you get the right details for your voucher.','Fair housing: never discourage someone using a voucher. Send voucher questions to your manager.']],'q'],
[LI('ok'),'Closing',[
['After the tour.','Which home felt most like yours? Let’s check that it’s still open today.','']],'q']];"""
i=t.find('const KIT=[');j=t.find("let kitTab='o';",i);assert i>0 and j>i
t=t[:i]+KIT+'\n'+t[j:]
sub(".replace(/{pe1}/g,f('The Pearl at St. Rose','1 bed from')).replace(/{po1}/g,f('Positano','1 bed from'))",".replace(/{bs1}/g,f('Broadstone Scottsdale Quarter','1 bed average')).replace(/{co1}/g,f('The Core Scottsdale','1 bed average'))",1)
sub("|pearl|positano|marlowe|","|broadstone|the core|core scottsdale|residences kierland|kierland|",1)
# ---- Ava (Pillar page assistant) instead of Mia (FORE)
AVA_VID="https://cms-toolkit-artifacts.artlist.io/content/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-v1/media__5/-e-x-t-e-r-n-a-l_-i-m-a-g-e_-t-o_-v-i-d-e-o-cbe46f52-fbd3-4b4a-a77d-f19fd9fa2d4b.mp4?Expires=2110767716&Key-Pair-Id=K2ZDLYDZI2R1DF&Signature=eZL0QFjrcYQDNljssVAbEPmMGEj2jl6zeZ0TgOf9k-tQPZU~WgtPep6rZOjLK91U7eebCF5MMs-2tWf9oxZQ48pgBfLyllROpACMn~~oA8IH1RAMv1MEpe3NuH17zM~UlrtdROes78Ym-djEhcBxVcyKfYiixwr1hmzqkgKC-ycsOWN1F3HlV7et1cCQKO6oBT2Z5O-499Omqu1ZnfTEc-5Z78kZfs4rQdI4ZOkOuxY~1TCfWo2KpygFo7Yr43n2qITAL~lovJIGYwP6X648esXRPtBhUz3kIgdDPcEU5RTeHECUdfN~T8Bo4SilGdFeagwoWDgaiyVGWveU03N~Jw__"
rsub(r"(const MC_VID=)(['\"])[^'\"]*\2",lambda m:m.group(1)+"'"+AVA_VID+"'")
t=t.replace('guide/mia-face.jpg','guide/ava-face.jpg').replace('guide/mia-poster.jpg','guide/ava-poster.jpg')
t=re.sub(r"\bMia\b","Ava",t)
# ---- phone (number on huxleyscottsdale.com; Google shows (480) 500-7596)
t=t.replace("(725) 209-4665","(480) 771-8082").replace('+17252094665','+14807718082').replace('7252094665','4807718082')
# ---- names, paths, keys, salt
t=t.replace('?v=f1','?v=h1')
t=re.sub(r"(['\"`])llfo-",r"\1llhx-",t)
t=t.replace("sha('fora:","sha('huxley:")
t=t.replace('fora-50r1',FOLDER).replace('LocalLift-Live-Fora-flyer','LocalLift-Live-Huxley-flyer')
t=t.replace('review/fora','review/huxley')
t=t.replace('meet/fora/','meet/huxley/').replace('team/fora/','team/huxley/').replace('live_fora','live_huxley')
t=t.replace("live.thesocialdm.com/fora","live.thesocialdm.com/huxley")
t=t.replace('foravegas.com','huxleyscottsdale.com').replace('Fora Apartments','Huxley Scottsdale')
t=t.replace('Fora','Huxley')
t=re.sub(r"'fora'","'huxley'",t)
t=re.sub(r"([:=]\s*)fora\b",r"\1huxley",t)
t=t.replace('Las Vegas, NV','Scottsdale, AZ').replace('Las Vegas','Scottsdale')
t=t.replace('id="forafx"','id="hxfx0"')
# ---- no Weekly Pulse yet for Huxley: hide the score block until one exists
sub('score:()=>D?','score:()=>D&&D.score?',1)
# ---- colors: Fora clay and sand to Pillar red, charcoal and warm stone
CM={'#7c453d':'#c8241d','#7a4038':'#c8241d','#5e322b':'#9a1b16','#5e2f2a':'#9a1b16','#6a3a33':'#a81f19','#e2b8a8':'#f2a49f',
 '#f1e4de':'#fbe9e7','#f3e5de':'#fbe9e7','#f6f2ef':'#f6f5f3','#f6ece7':'#fbefed','#4a4645':'#48484a','#6b6663':'#6b6b6b','#2f2f30':'#2c2c2e',
 '#1f1f20':'#1c1c1e','#3a3637':'#3a3a3c','#5a2f29':'#7a1712','#e6dcd5':'#e7e5e2','#ece4de':'#ecebe8','#f1e8e3':'#f3f2ef'}
t=re.sub(r'#[0-9a-fA-F]{6}\b',lambda m:CM.get(m.group(0).lower(),m.group(0)),t)
t=t.replace('rgba(124,69,61,','rgba(200,36,29,').replace('rgba(122,64,56,','rgba(200,36,29,')
os.makedirs(os.path.join(R,'live',FOLDER,'v3'),exist_ok=True)
SP=os.path.join(R,'live',FOLDER,'v3','index.html')
open(SP,'w').write(t)
open(os.path.join(R,'live',FOLDER,'v3','version.txt'),'w').write(APPV+'\n')
print('built',len(t),'APPV',APPV)
bad=re.findall(r'(?i)montage|tigard|oregon|stillwater|kissimmee|florida|lura|coya|fora\b|vegas|nevada|henderson|pearl|positano|marlowe|questrial|speakeasy|\(725\)|\(702\)|llfo|50r1|\bmia\b',t)
print('leftovers',collections.Counter(b.lower() for b in bad))
