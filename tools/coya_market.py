"""Builds the "market" object in live/coya-3zep/data.json from facts already in that file
(compete, checked by the daily refresh; rivals map scan; tiles). No other numbers are used.
Run after the daily compete refresh: python3 tools/coya_market.py"""
import json,os,datetime
P=os.path.join(os.path.dirname(__file__),'..','live','coya-3zep','data.json')
D=json.load(open(P))
C=D['compete'];U=C['us'];I={x['name']:x for x in C['items']}
def frm(it,lab):
    for v,l in it['from']:
        if l==lab: return v
    return 'Ask'
def vs(it,row,col=1):
    for r in it.get('vs',[]):
        if r[0]==row: return r[col]
    return 'Not posted'
iso=C['checkedIso'];md=datetime.date.fromisoformat(iso);sd=f'{md.month}/{md.day}'
JA,AI,GL=I['Jade'],I['Ainsley at The Collective'],I['Green Leaf Lotus']
us1,us2=frm(U,'1 bed'),frm(U,'2 bed')
me=D['rv'];scan=D['rivals']['date'].replace(' map scan','')
ai=[t for t in D['tiles'] if 'AI answers' in t[1]]
src=f'COYA and Ainsley websites checked {sd} · Jade special confirmed, prices not confirmed today'
spec=U['special']
lc1=lambda x:x[:1].lower()+x[1:]
KEEPCAP=('Sky','Club','Co','EV','BBQ','10','24','Pet','Reserved','Gated','Smart','Full','Resort')
sh=lambda s:s if s.split()[0] in KEEPCAP else s[0].lower()+s[1:]
cards=[
 {'lab':'WHERE WE STAND OUT','p':['new','New'],'h':'Use these on every tour',
  'b':', '.join(s for s in U['showoff'][:8])+'.','src':f'COYA and Ainsley websites checked {sd} · ratings from the Google scan of {scan}',
  'cmp':{'cols':['COYA','Jade','Ainsley'],'rows':[['Google rating',vs(JA,'Google rating',2),vs(JA,'Google rating'),vs(AI,'Google rating')],['Pet fee','$0',vs(JA,'Pet fee'),vs(AI,'Pet fee')],['Pet rent','$50/mo',vs(JA,'Pet rent'),vs(AI,'Pet rent')]]},
  'chips':U['showoff'][:8],
  'note':'COYA has the Sky Lounge with Strip views, a pet spa and dog park, and a $0 pet fee. Ask rivals what they charge at move in.'},
 {'lab':'SPECIALS WATCH','p':['m','Measured'],'h':'Ainsley and Jade lead with free weeks',
  'b':f'COYA: {spec}. Ainsley: {lc1(AI["special"])}. Jade: {lc1(JA["special"])}. Green Leaf Lotus: not read today.',
  'src':src,'list':[['COYA',spec,'me'],['Ainsley at The Collective',AI['special'],''],['Jade',JA['special'],''],['Green Leaf Lotus','Not read today. Ask what they were quoted','']]},
 {'lab':'PRICE CHECK','c':'warn','p':['m','Measured'],'h':'Jade and Ainsley list lower starting base rents','t':'rivals','src':src,
  'more':'Base rents. Jade adds about $375 in monthly charges on a 1 bed, and Ainsley adds about $162 a month in required charges plus a $300 admin fee, a $250 cleaning fee and a $65 membership fee, so ask what total and term they were quoted. Jade prices are as last listed and not confirmed today. Green Leaf Lotus prices were not read today.'},
 {'lab':'GOOGLE REVIEWS','p':['m','Measured'],'h':f'Our {me["rating"]} beats every rival on this page',
  'b':f'Our rating is {me["rating"]} from {me["count"]} Google reviews. Green Leaf Lotus is at {vs(GL,"Google rating")}, Ainsley {vs(AI,"Google rating")} and Jade {vs(JA,"Google rating")}.','src':f'Google map scan · {scan}',
  'stats':[[me['rating'],'Our Google rating'],[me['count'],'Our reviews'],['244','Ainsley reviews']],
  'note':'Rivals have more reviews. Every review we ask for keeps our lead and closes the count gap.'}]
if ai:
  a=ai[0];n,o=a[0].split(' of ')
  cards.append({'lab':'AI ANSWERS','p':['s','Signal'],'h':'AI assistants name COYA','b':f'Named in {a[0]} answers to renter questions, up from 10 a week earlier.','src':f'AI answer panel · {a[2].replace("Panel of ","")}',
   'stats':[[n,f'of {o} AI answers name you']]})
ex=[
 {'k':'edge','q':'Where do we stand out against rivals?','a':'From the COYA website: '+', '.join(sh(s) if i else s for i,s in enumerate(U['showoff']))+f'.<ul><li>Google rating: {me["rating"]} on {me["count"]} reviews, the highest of the communities on this page.</li><li>Pets: $50 a month, a $300 refundable pet deposit and no pet fee, no weight limits, up to 3 pets.</li><li>Every 2 bedroom has two baths.</li></ul>','s':f'COYA and Ainsley websites checked {sd} · ratings from the Google scan of {scan}'},
 {'k':'ops','q':'Who showed the tour? Pending service requests?','a':'Tour agents and service requests live in your property management system, which is not connected to this app. Tours you log in Tour mode are on your desk list.','s':'LocalLift Live'},
 {'k':'why','q':'Why are tours not signing?','a':f'We cannot see each person’s reason, but here is what they see when they compare you:<ul><li>Jade and Ainsley list lower starting base rents. 1 bedroom from: Ainsley {frm(AI,"1 bed")}, Jade {frm(JA,"1 bed")}, ours {us1}.</li><li>Ainsley posts up to 10 weeks free plus a $1,000 gift card, and Jade up to 8 weeks free.</li></ul>What wins them back: {spec}, the Sky Lounge with Strip views, our {me["rating"]} rating and a total cost check (both add charges on top of base rent).','s':src},
 {'k':'specials','q':'What specials are rivals running?','a':f'Ainsley at The Collective: {lc1(AI["special"])}. Jade: {lc1(JA["special"])}. Green Leaf Lotus: not read today. COYA: {spec}.','s':src},
 {'k':'rivals','q':'Who are we up against?','a':f'Green Leaf Lotus around the corner on Procyon St, Jade on W Twain Ave (1 bedroom from {frm(JA,"1 bed")}, up to 8 weeks free) and Ainsley at The Collective on Paradise Rd (1 bedroom from {frm(AI,"1 bed")}, up to 10 weeks free plus a gift card). COYA’s 1 bedroom starts at {us1}.','s':src},
 {'k':'price','q':'Are we priced right?','a':f'1 bed from: COYA {us1}, Jade {frm(JA,"1 bed")}, Ainsley {frm(AI,"1 bed")}.<br>2 bed from: COYA {us2}, Jade {frm(JA,"2 bed")} (waitlist plan), Ainsley {frm(AI,"2 bed")}.<br>Jade prices are as last listed and not confirmed today. Green Leaf Lotus prices were not read today.<br>These are base rents. COYA’s website shows totals with $204 in required monthly fees, Jade and Ainsley add their own charges, and specials differ, so compare totals on the same lease term.','s':src},
 {'k':'reviews','q':'How are our reviews?','a':f'{me["rating"]} stars from {me["count"]} Google reviews, every one answered. Green Leaf Lotus {vs(GL,"Google rating")}, Ainsley {vs(AI,"Google rating")}, Jade {vs(JA,"Google rating")}. Every review request counts.','s':f'Google map scan · {scan}'}]
if ai: ex.append({'k':'ai','q':'Is AI sending renters our way?','a':f'AI assistants named COYA in {ai[0][0]} answers to renter questions, including first pick on Gemini for best apartments near Chinatown Las Vegas.','s':f'AI answer panel · {ai[0][2].replace("Panel of ","")}'})
rows=[['COYA',us1,us2],['Jade (not confirmed today)',frm(JA,'1 bed'),frm(JA,'2 bed')],['Ainsley at The Collective',frm(AI,'1 bed'),frm(AI,'2 bed')],['Green Leaf Lotus','Ask','Ask']]
D['market']={'rvh':['Community','1 bed base rent from','2 bed base rent from'],'rv':rows,'srh':['Source','Visits','Leads'],'sr':[],
 'pts':[f'Our offer: {spec}.',
  'Jade and Ainsley list lower starting base rents, and both add charges on top, so ask what total and term they were quoted.',
  f'Our {me["rating"]} Google rating is the highest of the rivals here. Lead with the Sky Lounge Strip views, the pet spa and a $0 pet fee.'],
 'cards':cards,'ex':ex,'line':'Specials today: Ainsley up to 10 weeks free, Jade up to 8 weeks free.',
 'briefSrc':f'COYA and Ainsley websites checked {sd} · Jade prices not confirmed today · Google scan {scan}','checked':C['checked'],'checkedIso':iso}
json.dump(D,open(P,'w'),ensure_ascii=False,indent=1)
print(json.dumps(D['market'],ensure_ascii=False)[:300])
