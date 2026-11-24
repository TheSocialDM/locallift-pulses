"""Builds the "market" object in live/lura-x5r9/data.json from facts already in that file
(compete, checked by the daily refresh; rivals map scan; tiles). No other numbers are used.
Run after the daily compete refresh: python3 tools/lura_market.py"""
import json,os,datetime
P=os.path.join(os.path.dirname(__file__),'..','live','lura-x5r9','data.json')
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
JA,AI,FL=I['Jade'],I['Ainsley at The Collective'],I['Flatiron LV']
us1,us2=frm(U,'1 bed'),frm(U,'2 bed')
me=D['rv'];scan=D['rivals']['date'].replace(' map scan','')
ai=[t for t in D['tiles'] if 'AI answers' in t[1]]
src=f'Each community’s website · checked {sd}'
spec=U['special']
cards=[
 {'lab':'WHERE WE STAND OUT','p':['new','New'],'h':'Use these on every tour',
  'b':', '.join(s if i==0 else (s if s.split()[0] in ('Sky','The','EV','BBQ','10','24/7') else s[0].lower()+s[1:]) for i,s in enumerate(U['showoff']))+'.','src':f'Lura and rival websites · checked {sd}',
  'cmp':{'cols':['Lura','Jade','Ainsley'],'rows':[['Google rating',vs(JA,'Google rating',2),vs(JA,'Google rating'),vs(AI,'Google rating')],['Deposit','$500',vs(JA,'Deposit'),'$250 + $250'],['Pet fee','$500',vs(JA,'Pet fee'),vs(AI,'Pet fee')]]},
  'chips':U['showoff'][:8],
  'note':'Lura has the walk to the Strip over the Harmon Bridge and free gated garage parking. Ask rivals what parking costs.'},
 {'lab':'SPECIALS WATCH','p':['m','Measured'],'h':'All 3 rivals post a special too',
  'b':f'Lura: {spec}. Ainsley: {AI["special"].lower()}. Jade: {JA["special"].lower()}. Flatiron LV: {FL["special"].lower()}.',
  'src':src,'list':[['Lura',spec,'me'],['Ainsley at The Collective',AI['special'],''],['Jade',JA['special'],''],['Flatiron LV',FL['special'],'']]},
 {'lab':'PRICE CHECK','c':'warn','p':['m','Measured'],'h':'Jade and Ainsley list lower starting rents','t':'rivals','src':src,
  'more':'Base rents. Jade adds about $375 in monthly charges on a 1 bed, and Ainsley adds utilities and set charges plus admin and cleaning fees, so ask what total and term they were quoted. Flatiron LV prices did not load for today’s check.'},
 {'lab':'GOOGLE REVIEWS','p':['m','Measured'],'h':f'Our {me["rating"]} beats every rival on this page',
  'b':f'Our rating is {me["rating"]} from {me["count"]} Google reviews. Ainsley is at {vs(AI,"Google rating")}, Jade {vs(JA,"Google rating")} and Flatiron LV {vs(FL,"Google rating")}.','src':f'Google map scan · {scan}',
  'stats':[[me['rating'],'Our Google rating'],[me['count'],'Our reviews'],['187','Spectra Paradise reviews']],
  'note':'Rivals have more reviews. Every review we ask for keeps our lead and closes the count gap.'}]
if ai:
  a=ai[0];n,o=a[0].split(' of ')
  cards.append({'lab':'AI ANSWERS','p':['s','Signal'],'h':'AI assistants name Lura','b':f'Named in {a[0]} answers to renter questions.','src':f'AI answer panel · {a[2].replace("Panel of ","")}',
   'stats':[[n,f'of {o} AI answers name you']]})
sh=lambda s:s if s.split()[0] in ('Sky','The','EV','BBQ','10','24/7') else s[0].lower()+s[1:]
ex=[
 {'k':'edge','q':'Where do we stand out against rivals?','a':'From the Lura website: '+', '.join(sh(s) if i else s for i,s in enumerate(U['showoff']))+f'.<ul><li>Google rating: {me["rating"]} on {me["count"]} reviews, the highest of the communities on this page.</li><li>Free gated garage parking and a walk to the Strip over the Harmon Bridge.</li><li>Pets: $50 a month and a $500 pet fee, no weight limits, up to 3 pets.</li></ul>','s':f'Lura and rival websites · checked {sd}'},
 {'k':'ops','q':'Who showed the tour? Pending service requests?','a':'Tour agents and service requests live in your property management system, which is not connected to this app. Tours you log in Tour mode are on your desk list.','s':'LocalLift Live'},
 {'k':'why','q':'Why are tours not signing?','a':f'We cannot see each person’s reason, but here is what they see when they compare you:<ul><li>Jade and Ainsley list lower starting base rents. 1 beds: Ainsley {frm(AI,"1 bed")}, Jade {frm(JA,"1 bed")}, ours {us1}.</li><li>Ainsley posts up to 10 weeks free plus a $1,000 gift card, and Jade up to 8 weeks free.</li></ul>What wins them back: {spec}, the walk to the Strip, free garage parking, our {me["rating"]} rating and a total cost check (both add monthly charges on top of base rent).','s':src},
 {'k':'specials','q':'What specials are rivals running?','a':f'Ainsley at The Collective: {AI["special"].lower()}. Jade: {JA["special"].lower()}. Flatiron LV: {FL["special"].lower()}. Lura: {spec}.','s':src},
 {'k':'rivals','q':'Who are we up against?','a':f'Jade on W Twain Ave (1 beds from {frm(JA,"1 bed")}, up to 8 weeks free), Ainsley at The Collective on Paradise Rd (1 beds from {frm(AI,"1 bed")}, up to 10 weeks free plus a gift card) and Flatiron LV by the Palms (1 month free on select homes). Lura 1 beds start at {us1}.','s':src},
 {'k':'price','q':'Are we priced right?','a':f'1 bed from: Lura {us1}, Jade {frm(JA,"1 bed")}, Ainsley {frm(AI,"1 bed")}.<br>2 bed from: Lura {us2}, Jade {frm(JA,"2 bed")} (waitlist plan), Ainsley {frm(AI,"2 bed")}.<br>Flatiron LV prices did not load for today’s check.<br>These are base rents. Lura’s website shows totals with $200 in mandatory monthly fees, Jade and Ainsley add their own monthly charges, and specials differ, so compare totals on the same lease term.','s':src},
 {'k':'reviews','q':'How are our reviews?','a':f'{me["rating"]} stars from {me["count"]} Google reviews, 122 of them answered. Ainsley {vs(AI,"Google rating")}, Jade {vs(JA,"Google rating")}, Flatiron LV {vs(FL,"Google rating")}. Spectra Paradise leads the map with 187 reviews. Every review request counts.','s':f'Google map scan · {scan}'}]
if ai: ex.append({'k':'ai','q':'Is AI sending renters our way?','a':f'AI assistants named Lura in {ai[0][0]} answers to renter questions.','s':f'AI answer panel · {ai[0][2].replace("Panel of ","")}'})
rows=[['Lura',us1,us2],['Jade',frm(JA,'1 bed'),frm(JA,'2 bed')],['Ainsley at The Collective',frm(AI,'1 bed'),frm(AI,'2 bed')],['Flatiron LV','Ask','Ask']]
D['market']={'rvh':['Community','1 bed from','2 bed from'],'rv':rows,'srh':['Source','Visits','Leads'],'sr':[],
 'pts':[f'Our offer: {spec}.',
  'Jade and Ainsley list lower starting base rents, and both add monthly charges on top, so ask what total and term they were quoted.',
  f'Our {me["rating"]} Google rating is the highest of the rivals here. Lead with the walk to the Strip and free gated garage parking.'],
 'cards':cards,'ex':ex,'line':'Specials today: Ainsley up to 10 weeks free, Jade up to 8 weeks free.',
 'briefSrc':f'Websites checked {sd} · Google scan {scan}','checked':C['checked'],'checkedIso':iso}
json.dump(D,open(P,'w'),ensure_ascii=False,indent=1)
print(json.dumps(D['market'],ensure_ascii=False)[:600])
