"""Builds the "market" object in live/fora-50r1/data.json from facts already in that file
(compete, checked by the daily refresh; rivals map scan; tiles). No other numbers are used.
Run after the daily compete refresh: python3 tools/fora_market.py"""
import json,os,datetime
P=os.path.join(os.path.dirname(__file__),'..','live','fora-50r1','data.json')
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
PE,PO,MA=I['The Pearl at St. Rose'],I['Positano'],I['Marlowe South Las Vegas']
us1,us2=frm(U,'1 bed'),frm(U,'2 bed')
me=D['rv'];scan=D['rivals']['date'].replace(' map scan','')
ai=[t for t in D['tiles'] if 'AI answers' in t[1]]
src=f'Each community’s website · checked {sd}'
spec=U['special']
KEEPCAP=('Sky','Speakeasy','Four','BBQ','9','Smart','Full','Free','Premium','Coworking','Resident','Resort','Dog','Walk')
sh=lambda s:s if s.split()[0] in ('Sky','BBQ','9') else s[0].lower()+s[1:]
show=', '.join(s if i==0 else sh(s) for i,s in enumerate(U['showoff']))
cards=[
 {'lab':'WHERE WE STAND OUT','p':['new','New'],'h':'Use these on every tour',
  'b':show+'.','src':f'Fora and rival websites · checked {sd}',
  'cmp':{'cols':['Fora','Pearl','Positano'],'rows':[['Google rating',vs(PE,'Google rating',2),vs(PE,'Google rating'),vs(PO,'Google rating')],['1 bed size','805 sq ft',vs(PE,'1 bed size'),'735 sq ft'],['2 bed size','1,150 sq ft',vs(PE,'2 bed size'),vs(PO,'2 bed size')]]},
  'chips':U['showoff'][:8],
  'note':'Fora homes are larger than The Pearl and Positano plan for plan, and covered parking is free. Marlowe lists covered parking at $25 a month.'},
 {'lab':'SPECIALS WATCH','p':['m','Measured'],'h':'The Pearl matches our offer',
  'b':f'Fora: {spec}. The Pearl at St. Rose: {PE["special"].lower()}. Positano: {PO["special"].lower()}. Marlowe South Las Vegas: {MA["special"].lower()}.',
  'src':src,'list':[['Fora',spec,'me'],['The Pearl at St. Rose',PE['special'],''],['Positano',PO['special'],''],['Marlowe South Las Vegas',MA['special'],'']]},
 {'lab':'PRICE CHECK','c':'warn','p':['m','Measured'],'h':'The Pearl and Positano list lower starting rents','t':'rivals','src':src,
  'more':'Base rents on smaller homes: their 1 and 2 bedrooms are 70 to 185 square feet smaller than ours. Positano adds mandatory monthly charges on top. Marlowe prices did not load for today’s check.'},
 {'lab':'GOOGLE REVIEWS','p':['m','Measured'],'h':f'Our {me["rating"]} beats The Pearl and Positano',
  'b':f'Our rating is {me["rating"]} from {me["count"]} Google reviews. The Pearl at St. Rose is at {vs(PE,"Google rating")}, Positano {vs(PO,"Google rating")} and Marlowe South Las Vegas {vs(MA,"Google rating")}.','src':f'Google map scan · {scan}',
  'stats':[[me['rating'],'Our Google rating'],[me['count'],'Our reviews'],['266','The Pearl reviews']],
  'note':'The Pearl has more reviews and holds the top three at more map points. Every review we ask for closes the count gap.'}]
if ai:
  a=ai[0];n,o=a[0].split(' of ')
  cards.append({'lab':'AI ANSWERS','p':['s','Signal'],'h':'AI assistants name Fora','b':f'Named in {a[0]} answers to renter questions.','src':f'AI answer panel · {a[2].replace("Panel of ","")}',
   'stats':[[n,f'of {o} AI answers name you']]})
ex=[
 {'k':'edge','q':'Where do we stand out against rivals?','a':'From the Fora website: '+show+f'.<ul><li>Google rating: {me["rating"]} on {me["count"]} reviews, above The Pearl at St. Rose and Positano.</li><li>Bigger homes: our 1 bed is 805 sq ft and our B1 2 bed is 1,150 sq ft, against 708 and 965 at The Pearl.</li><li>Free covered parking. Marlowe lists covered parking at $25 a month.</li><li>Pets: $50 a month and a $500 pet fee, no weight limits, up to 3 pets.</li></ul>','s':f'Fora and rival websites · checked {sd}'},
 {'k':'ops','q':'Who showed the tour? Pending service requests?','a':'Tour agents and service requests live in your property management system, which is not connected to this app. Tours you log in Tour mode are on your desk list.','s':'LocalLift Live'},
 {'k':'why','q':'Why are tours not signing?','a':f'We cannot see each person’s reason, but here is what they see when they compare you:<ul><li>The Pearl and Positano list lower starting base rents. 1 beds: The Pearl {frm(PE,"1 bed")}, Positano {frm(PO,"1 bed")}, ours {us1}.</li><li>The Pearl runs a similar no rent until 2027 offer, and Positano posts six weeks free on select 2 bedrooms.</li></ul>What wins them back: {spec}, bigger homes, free covered parking, the speakeasy lounge, our {me["rating"]} rating and a total cost check on the same size and term.','s':src},
 {'k':'specials','q':'What specials are rivals running?','a':f'The Pearl at St. Rose: {PE["special"].lower()}. Positano: {PO["special"].lower()}. Marlowe South Las Vegas: {MA["special"].lower()}. Fora: {spec}.','s':src},
 {'k':'rivals','q':'Who are we up against?','a':f'The Pearl at St. Rose, 0.35 miles away (1 beds from {frm(PE,"1 bed")}, no rent until 2027), Positano down Jeffreys St (1 beds from {frm(PO,"1 bed")}, six weeks free on select 2 bedrooms) and Marlowe South Las Vegas on S Las Vegas Blvd (prices did not load today). Fora 1 beds start at {us1}.','s':src},
 {'k':'price','q':'Are we priced right?','a':f'1 bed from: Fora {us1}, The Pearl {frm(PE,"1 bed")}, Positano {frm(PO,"1 bed")}.<br>2 bed from: Fora {us2}, The Pearl {frm(PE,"2 bed")}, Positano {frm(PO,"2 bed")}.<br>Marlowe prices did not load for today’s check.<br>These are base rents, and our homes are larger. Fora’s website shows totals with $170 in required monthly fees, Positano adds its own mandatory charges, and specials differ, so compare totals on the same size and lease term.','s':src},
 {'k':'reviews','q':'How are our reviews?','a':f'{me["rating"]} stars from {me["count"]} Google reviews, 128 of them answered. The Pearl at St. Rose {vs(PE,"Google rating")}, Positano {vs(PO,"Google rating")}, Marlowe South Las Vegas {vs(MA,"Google rating")}. The Pearl holds the top three at the most map points near us. Every review request counts.','s':f'Google map scan · {scan}'}]
if ai: ex.append({'k':'ai','q':'Is AI sending renters our way?','a':f'AI assistants named Fora in {ai[0][0]} answers to renter questions, and all three name Fora first for apartments with a speakeasy lounge in Las Vegas.','s':f'AI answer panel · {ai[0][2].replace("Panel of ","")}'})
rows=[['Fora',us1,us2],['The Pearl at St. Rose',frm(PE,'1 bed'),frm(PE,'2 bed')],['Positano',frm(PO,'1 bed'),frm(PO,'2 bed')],['Marlowe South Las Vegas','Ask','Ask']]
D['market']={'rvh':['Community','1 bed from','2 bed from'],'rv':rows,'srh':['Source','Visits','Leads'],'sr':[],
 'pts':[f'Our offer: {spec}.',
  'The Pearl and Positano list lower starting base rents on smaller homes, so compare size and total on the same lease term.',
  f'Our {me["rating"]} Google rating is above The Pearl and Positano. Lead with the speakeasy lounge, bigger homes and free covered parking.'],
 'cards':cards,'ex':ex,'line':'Specials today: The Pearl no rent until 2027, Positano six weeks free on select 2 bedrooms.',
 'briefSrc':f'Websites checked {sd} · Google scan {scan}','checked':C['checked'],'checkedIso':iso}
json.dump(D,open(P,'w'),ensure_ascii=False,indent=1)
print(json.dumps(D['market'],ensure_ascii=False)[:400])
