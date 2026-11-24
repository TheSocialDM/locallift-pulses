"""Builds the "market" object in live/stillwater-k4p7/data.json from facts already in that file
(compete, checked by the daily refresh; rivals map scan; tiles). No other numbers are used.
Run after the daily compete refresh: python3 tools/stillwater_market.py"""
import json,os,datetime
P=os.path.join(os.path.dirname(__file__),'..','live','stillwater-k4p7','data.json')
D=json.load(open(P))
C=D['compete'];U=C['us'];I={x['name']:x for x in C['items']}
def frm(it,lab):
    for v,l in it['from']:
        if l==lab: return v
    return 'None'
def us(row):
    for r in JA['vs']:
        if r[0]==row: return r[2]
    return 'Not posted'
def vs(it,row):
    for r in it.get('vs',[]):
        if r[0]==row: return r[1]
    return 'Not posted'
iso=C['checkedIso'];md=datetime.date.fromisoformat(iso);sd=f'{md.month}/{md.day}'
CV,JA,MO=I['Cielo View'],I['The Jamison'],I['Mosaic at Lake Toho']
us1,us2,usS=frm(U,'1 bed'),frm(U,'2 bed'),frm(U,'studio')
num=lambda s:int(''.join(c for c in s if c.isdigit()) or 0)
riv=[('Cielo View',CV),('The Jamison',JA),('Mosaic at Lake Toho',MO)]
lower=[n for n,it in riv if num(frm(it,'1 bed'))<num(us1) and num(frm(it,'2 bed'))<num(us2)]
dep=vs(JA,'Deposit')
rvrow={r[0]:r for r in D['rivals']['rows']}
me=D['rv'];scan=D['rivals']['date']
ai=[t for t in D['tiles'] if 'AI answers' in t[1]]
src=f'Each community’s website · checked {sd}'
spec=U['special']
cards=[
 {'lab':'WHERE WE STAND OUT','p':['new','New'],'h':'Use these on every tour',
  'b':', '.join(U['showoff'])+'.','src':f'Stillwater Lakes and rival websites · checked {sd}',
  'cmp':{'cols':['Stillwater','Jamison','Mosaic'],'rows':[['Deposit',us('Deposit'),vs(JA,'Deposit'),vs(MO,'Deposit')],['Pet rent',us('Pet rent'),vs(JA,'Pet rent'),vs(MO,'Pet rent')],['Pet fee',us('Pet fee'),vs(JA,'Pet fee'),vs(MO,'Pet fee')]]},
  'chips':U['showoff'][:8],
  'note':f'Studios from {usS} and townhomes too. Cielo View has 1 and 2 bedrooms only and does not post a deposit.'},
 {'lab':'SPECIALS WATCH','p':['m','Measured'],'h':'2 of 3 rivals post a special too',
  'b':f'Stillwater Lakes: {spec}. Cielo View: {CV["special"].lower()}. Mosaic at Lake Toho: {MO["special"].lower()}. The Jamison: no special posted.',
  'src':src,'list':[['Stillwater Lakes',spec+', no end date posted','me'],['Cielo View',CV['special'],''],['Mosaic at Lake Toho',MO['special'],''],['The Jamison','No special posted','']]},
 {'lab':'PRICE CHECK','c':'warn','p':['m','Measured'],'h':f'{len(lower)} rivals list lower starting rents','t':'rivals','src':src,
  'more':'Base rents. The Jamison adds mandatory monthly costs on top, and Mosaic posts an 18 month lease, so ask what total and term they were quoted.'},
 {'lab':'GOOGLE REVIEWS','c':'warn','p':['m','Measured'],'h':f'Cielo View has {rvrow["Cielo View"][2]} reviews to our {me["count"]}',
  'b':f'Our rating is {me["rating"]} from {me["count"]} Google reviews.','src':f'Google map scan · {scan.replace(" map scan","")}',
  'stats':[[me['rating'],'Our Google rating'],[me['count'],'Our reviews'],[str(rvrow['Cielo View'][2]),'Cielo View reviews']],
  'note':'Every review we ask for moves our average more than theirs.'}]
if ai:
  a=ai[0];n,o=a[0].split(' of ')
  cards.append({'lab':'AI ANSWERS','p':['s','Signal'],'h':'AI assistants name Stillwater Lakes','b':f'Named in {a[0]} answers to renter questions.','src':f'AI answer panel · {a[2].replace("Panel of ","")}',
   'stats':[[n,f'of {o} AI answers name you']]})
ex=[
 {'k':'edge','q':'Where do we stand out against rivals?','a':'From the Stillwater Lakes website: '+', '.join(s if s[:2].isupper() else s[0].lower()+s[1:] for s in U['showoff'])+'.'+f'<ul><li>Deposit: {us("Deposit")} vs {vs(JA,"Deposit")} at The Jamison and {vs(MO,"Deposit")} at Mosaic at Lake Toho.</li><li>Pets: {us("Pet rent").replace("/mo"," a month")} and a {us("Pet fee")} pet fee, vs {vs(JA,"Pet rent").replace("/mo"," a month")} and a {vs(JA,"Pet fee")} pet fee at The Jamison.</li><li>Studios from {usS} and townhomes. Cielo View has 1 and 2 bedrooms only.</li></ul>','s':f'Stillwater Lakes and rival websites · checked {sd}'},
 {'k':'ops','q':'Who showed the tour? Pending service requests?','a':'Tour agents and service requests live in your property management system, which is not connected to this app. Tours you log in Tour mode are on your desk list.','s':'LocalLift Live'},
 {'k':'why','q':'Why are tours not signing?','a':f'We cannot see each person’s reason, but here is what they see when they compare you:<ul><li>All 3 rivals list lower starting base rents. 1 beds: Mosaic at Lake Toho {frm(MO,"1 bed")}, The Jamison {frm(JA,"1 bed")}, Cielo View {frm(CV,"1 bed")}, ours {us1}.</li><li>Cielo View also posts two months free, and Mosaic up to 8 weeks free.</li><li>Cielo View has {rvrow["Cielo View"][2]} Google reviews to our {me["count"]}.</li></ul>What wins them back: {spec}, the {us("Deposit")} deposit, studios and townhomes, and a total cost check (The Jamison adds monthly fees, Mosaic posts an 18 month lease).','s':src},
 {'k':'specials','q':'What specials are rivals running?','a':f'Cielo View: {CV["special"].lower()}. Mosaic at Lake Toho: {MO["special"].lower()}. The Jamison: no special posted. Stillwater Lakes: {spec}.','s':src},
 {'k':'rivals','q':'Who are we up against?','a':f'Cielo View (1 beds from {frm(CV,"1 bed")}, {CV["special"].lower()}), The Jamison (from {frm(JA,"1 bed")}, no special posted, monthly fees added) and Mosaic at Lake Toho (from {frm(MO,"1 bed")}, {MO["special"].lower()}). Stillwater Lakes 1 beds start at {us1}.','s':src},
 {'k':'price','q':'Are we priced right?','a':f'1 bed from: Stillwater Lakes {us1}, Cielo View {frm(CV,"1 bed")}, The Jamison {frm(JA,"1 bed")}, Mosaic at Lake Toho {frm(MO,"1 bed")}.<br>2 bed from: Stillwater Lakes {us2}, Cielo View {frm(CV,"2 bed")}, The Jamison {frm(JA,"2 bed")}, Mosaic at Lake Toho {frm(MO,"2 bed")}.<br>Studios from: Stillwater Lakes {usS}, The Jamison {frm(JA,"studio")}, Mosaic at Lake Toho {frm(MO,"studio")}. Cielo View has no studios.<br>These are base rents. The Jamison adds mandatory monthly costs, Mosaic posts an 18 month lease and ours is on a 15 month lease, so confirm the term before quoting a difference.','s':src},
 {'k':'reviews','q':'How are our reviews?','a':f'{me["rating"]} stars from {me["count"]} Google reviews. Cielo View {rvrow["Cielo View"][1]} ({rvrow["Cielo View"][2]}), Mosaic at Lake Toho {rvrow["Mosaic at Lake Toho"][1]} ({rvrow["Mosaic at Lake Toho"][2]}), The Jamison {rvrow["The Jamison"][1]} ({rvrow["The Jamison"][2]}). Every review request counts.','s':f'Google map scan · {scan.replace(" map scan","")}'}]
if ai: ex.append({'k':'ai','q':'Is AI sending renters our way?','a':f'AI assistants named Stillwater Lakes in {ai[0][0]} answers to renter questions.','s':f'AI answer panel · {ai[0][2].replace("Panel of ","")}'})
rows=[['Stillwater Lakes',us1,us2]]+[[n,frm(it,'1 bed'),frm(it,'2 bed')] for n,it in riv]
D['market']={'rvh':['Community','1 bed from','2 bed from'],'rv':rows,'srh':['Source','Visits','Leads'],'sr':[],
 'pts':[f'Our special: {spec}. No end date is posted.',
  f'{len(lower)} rivals list lower starting base rents on 1 and 2 bedrooms. The Jamison adds mandatory monthly costs and Mosaic posts an 18 month lease, so ask what total and term they were quoted.',
  f'Our deposit is {us("Deposit")} vs {vs(JA,"Deposit")} at The Jamison and Mosaic, and our pet rent and pet fee are lower than The Jamison.'],
 'cards':cards,'ex':ex,'line':f'Specials today: Cielo View {CV["special"].lower()}, Mosaic {MO["special"].lower()}.',
 'briefSrc':f'Websites checked {sd} · Google scan {scan.replace(" map scan","")}','checked':C['checked'],'checkedIso':iso}
json.dump(D,open(P,'w'),ensure_ascii=False,indent=1)
print(json.dumps(D['market'],ensure_ascii=False,indent=1)[:4000])
