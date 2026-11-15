import json
ML="https://themultifamilydesk.com/pillar/"
LEDGER="https://themultifamilydesk.com/pillar/ledger/"
BLS_PHX="https://www.bls.gov/regions/west/news-release/consumerpriceindex_phoenix.htm"
BLS_SEA="https://www.bls.gov/regions/west/news-release/consumerpriceindex_seattle.htm"
CENSUS="https://www.census.gov/housing/hvs/files/qtr326/Q326press.pdf"
RP="https://www.realpage.com/analytics/us-apartment-supply-3rd-quarter-2026/"
YCOMP="https://www.yardimatrix.com/blog/multifamily-housing-completion-estimate-for-2026/"
AL="https://www.apartmentlist.com/research/national-rent-data"
cap=open('../captions.md').read()
def grab(day):
    b=cap.split('## '+day)[1].split('\n',1)[1].split('\n## ')[0]
    c,f=b.split('FIRST COMMENT: ');return c.strip(),f.strip()
m1,mf1=grab('2026-11-17'); p1,pf1=grab('2026-11-19')
m1=m1.replace("That index follows what renters in the area pay, existing leases included, not the price on a listing. So it is a different signal","That index tracks what renters in the area are paying, including those on existing leases, rather than the price on a listing. It is a different signal")
assert 'rather than the price on a listing' in m1
P=[]
def add(date,time,topic,mel,melfc,pil,pilfc,image=None):
    P.append(dict(date=date,time=time,topic=topic,melanie=mel.strip(),melanie_fc=melfc,pillar=pil.strip(),pillar_fc=pilfc,image=image))

add("2026-11-15","11:41","Phoenix area rents paid (BLS CPI), Market Signal No. 04",m1,mf1,p1,pf1,"market-signal-2026-11-15-no04-rents-paid-phoenix.png")

add("2026-11-16","08:11","Seattle rents paid rose while Phoenix fell",
"""Phoenix and Seattle rents paid moved in opposite directions this fall.
I think that is a good argument for giving each market its own playbook.

In the Bureau of Labor Statistics' latest local price data, the Phoenix area rent index fell 1.4% from August to October. The Seattle area index rose 1.0% over the same stretch.

Both are single readings, not seasonally adjusted, and BLS says local indexes swing more than national ones. I would not build a strategy on them alone.

But they are a good reminder for anyone who works in both places. A renewal approach, a concession habit or a marketing calendar that fits Phoenix this fall may not fit Seattle, and the reverse is true too.

When your teams in different markets compare notes, which number do you line up first?

#Multifamily #PropertyManagement #SeattleRealEstate""",
f"Sources: U.S. Bureau of Labor Statistics, Consumer Price Index, Seattle area and Phoenix area, October 2026 (Nov 10, 2026) {BLS_SEA} and {BLS_PHX} . More of my market analysis: {ML}",
"""The Phoenix area rent index fell 1.4% from August to October. The Seattle area index rose 1.0%.
For operators in both metros, that split is worth a closer look.

Those figures come from the Bureau of Labor Statistics' local consumer price data released November 10. Each is one reading, not seasonally adjusted, and BLS notes that local indexes are more volatile than national ones.

For any operator with communities in more than one metro, a split like this is a useful prompt to check:
1. Are renewal guidelines set market by market, or company wide?
2. Do concession decisions use each community's own comparison set?
3. Is the marketing calendar built around each market's leasing season?

A metro figure can point to where to look. Each community's own numbers decide what to do.

How does your team adjust its approach from one market to the next?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Sources: U.S. Bureau of Labor Statistics, Consumer Price Index, Seattle area and Phoenix area, October 2026 (Nov 10, 2026) {BLS_SEA} and {BLS_PHX} . More from Melanie Graham Prock: {ML}")

add("2026-11-17","08:11","Census rental vacancy rose in Q3, West up year over year",
"""Fewer new apartments are being finished.
Vacancy still went up.

The Census Bureau's third quarter numbers put the U.S. rental vacancy rate at 7.6%, up from 7.3% in the second quarter and 7.1% a year earlier. In the West, it was 6.7%, compared with 6.0% a year before.

Completions have been slowing, so that may seem surprising. My read is that a slower pipeline does not empty out the buildings already leasing up. Supply that delivered over the last year or two may still be working its way through.

So in Arizona I would be careful with the idea that relief is right around the corner. It may come, but the timing could be slower than the headlines suggest.

How has your own occupancy moved since the summer?

#Multifamily #ArizonaRealEstate #PropertyManagement""",
f"Sources: U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Third Quarter 2026 (Oct 28, 2026) {CENSUS} . RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . More of my market analysis: {ML}",
"""Rental vacancy in the West was 6.7% in the third quarter, up from 6.0% a year before.
Nationally, the Census Bureau put it at 7.6%.

The national rate was 7.3% in the second quarter and 7.1% a year earlier. The rise comes while new apartment completions have been slowing nationally, which is a reminder that a smaller pipeline and lower vacancy do not always arrive at the same time.

To read this at the community level, start with four comparisons:
1. How does current occupancy compare with the same month last year?
2. Are recent move outs concentrated in one floor plan?
3. How many communities nearby are still in lease up?
4. Has the time it takes to lease a vacant home changed?

A community's own trend over the past year is likely to say more about next steps than the national rate does.

How often does your team compare occupancy with the same month last year?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Sources: U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Third Quarter 2026 (Oct 28, 2026) {CENSUS} . RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . More from Melanie Graham Prock: {ML}")

add("2026-11-18","08:11","Signal Ledger: grading our own call",
"""A few weeks ago, the market research I share on my site made a call about apartment supply.
The first checkpoint did not go its way.

In late October, RealPage reported that U.S. completions through the third quarter were about 27% lower than a year earlier. The question was whether that slowdown would start to show up as lower vacancy. The next Census release said no, not yet: national rental vacancy rose to 7.6% in the third quarter.

That checkpoint is now logged as not confirmed, in a ledger where every call gets graded against what the data later shows.

I like that approach. Coming back to report what happened is more useful to me than the forecast itself, especially when the answer is "not yet."

How does your team look back at the calls it made earlier in the year?

#Multifamily #PropertyManagement #RealEstateResearch""",
f"Sources: RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Third Quarter 2026 (Oct 28, 2026) {CENSUS} . More of my market analysis: {ML}",
"""Forecasts are easy to publish. Checking them later is the part that builds trust.
A short note on grading market calls.

In October, RealPage reported that U.S. apartment completions through the third quarter were about 27% lower than a year earlier. One natural expectation was that vacancy would start to ease. The Census Bureau's third quarter release showed national rental vacancy rising to 7.6% instead.

For a property team, the same habit applies to internal calls:
1. Write down the expectation and the date it should show up.
2. Name the number that will confirm or reject it.
3. Revisit it on that date, whatever the answer is.
4. Record what changed in the plan because of it.

Calls that get checked tend to get better over time.

What is one market assumption your team will revisit in the new year?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Sources: RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . U.S. Census Bureau, Quarterly Residential Vacancies and Homeownership, Third Quarter 2026 (Oct 28, 2026) {CENSUS} . More from Melanie Graham Prock: {ML}")

add("2026-11-19","08:11","Yardi raised its 2026 completions estimate",
"""Supply relief may take a little longer than expected.
Yardi Matrix's newest estimate is one more reason to plan for that.

On November 11, Yardi Matrix said it now expects 2026 multifamily completions to come in 4.8% higher than it previously forecast. It still expects 2027 new supply to land below 2026 levels, then rise again in 2028.

For anyone writing 2027 budgets in Arizona right now, I think that matters. If more units finish this year than expected, more of them may still be leasing up into next year, competing for the same renters.

I would rather budget for a slower recovery and be pleasantly surprised than the other way around.

What supply assumption is built into your 2027 plan?

#Multifamily #ArizonaRealEstate #PropertyManagement""",
f"Source: Yardi Matrix, Multifamily Housing Completion Estimate for 2026 (Nov 11, 2026) {YCOMP} . More of my market analysis: {ML}",
"""Yardi Matrix now expects 2026 multifamily completions to come in 4.8% higher than it previously forecast.
It still expects 2027 supply to be lower than 2026.

That update, published November 11, lands in the middle of budget season, when lease up assumptions for next year are being set.

Points worth building into a 2027 plan:
1. Which communities nearby opened this year or will open early next year?
2. How long did recent lease ups nearby take to stabilize?
3. What concession level does the budget assume, and for how long?
4. What would change the plan if supply clears faster or slower than expected?

How those questions are answered locally may matter more than any change to the national estimate.

How long does your plan assume nearby lease ups will keep offering concessions?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: Yardi Matrix, Multifamily Housing Completion Estimate for 2026 (Nov 11, 2026) {YCOMP} . More from Melanie Graham Prock: {ML}")

add("2026-11-20","08:11","Apartment List vacancy index at 7.0%, below February peak",
"""National apartment vacancy is easing.
Slowly.

Apartment List's national vacancy index was 7.0% in October, below its 7.3% peak in February. Apartment List says the rate is slowly creeping down but is still above its 2017 to 2019 average of 6.4%.

A slow decline can be easy to skip past, but I think it tells you something. The market may be past the worst of the oversupply, and it is not yet tight. In that middle ground, I think execution counts for more, especially turning vacant homes quickly and keeping the residents a community already has.

When the market is only easing slowly, the basics carry more weight.

Where is your team putting its extra effort before year end?

#Multifamily #PropertyManagement #Leasing""",
f"Source: Apartment List National Rent Report, November 2026 (Oct 28, 2026) {AL} . More of my market analysis: {ML}",
"""National vacancy kept easing in October, to 7.0% on Apartment List's index.
That is below February's 7.3% peak, and Apartment List says the rate is slowly creeping down.

A slowly easing national reading may leave more of the outcome to execution at the community level. Four measures to pull in a market that is easing only gradually:
1. Make ready: how many days does a vacant home sit before it is ready to show?
2. Lead response: how quickly does a new inquiry get a personal reply?
3. Tour to lease: what share of tours turn into applications?
4. Renewals: how early does the renewal conversation start?

Each of these can usually be measured from a community's own data within a week.

Which of these has moved the most for your team this year?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: Apartment List National Rent Report, November 2026 (Oct 28, 2026) {AL} . More from Melanie Graham Prock: {ML}")

add("2026-11-21","09:11","Budget season: which number do you trust",
"""Budget season is a good time to ask a blunt question.
Which numbers in the plan could you actually defend?

Rent growth, occupancy, concessions, renewals, turnover cost: each one rests on an assumption. Some come from a community's own history and some from market reports. A few, if we are honest as an industry, come from hope.

My view is that each one deserves a label: own data, market source or judgment call. Judgment calls are fine, as long as everyone in the room knows which ones they are.

I think that also makes the mid year review a lot more useful.

How do you mark the judgment calls in your own budget?

#Multifamily #PropertyManagement #Budgeting""",
f"More of my market analysis: {ML}",
"""Every budget rests on assumptions. Labeling them makes the plan easier to defend.
A simple exercise for budget season.

For each major line in the budget, note where the number came from:
1. The community's own history.
2. A named market source, with its date.
3. A judgment call, with the reason behind it.

Judgment calls are part of every plan. Labeling them helps a team know which numbers to watch most closely once the year begins, and which ones to revisit first if results drift.

Which line in a budget do you find hardest to forecast?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

add("2026-11-22","09:11","RealPage: completions down 27% through Q3, Phoenix still among top delivery metros",
"""Nationally, the construction wave is fading.
In Phoenix, the deliveries have kept coming.

RealPage counted about 231,000 U.S. apartment completions through the third quarter, 27% fewer than in the same period of 2025. It was also the smallest third quarter for deliveries since 2019.

But Phoenix was among the five metros RealPage named for the most new deliveries in the quarter, each above 3,000 units, alongside Dallas, Houston, Austin and Atlanta.

So when a headline says supply is drying up, my first question is where. A national slowdown and a busy local pipeline can both be true at the same time, and the second one is what shows up on a property's comp report.

How many new communities opened within a few miles of yours this year?

#Multifamily #ArizonaRealEstate #PropertyManagement""",
f"Source: RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . More of my market analysis: {ML}",
"""Phoenix was still among the busiest delivery metros in the third quarter.
That held even as U.S. completions fell about 27% from a year earlier, according to RealPage.

RealPage counted about 231,000 completions through the third quarter, and it was the smallest third quarter for deliveries since 2019. Phoenix, Dallas, Houston, Austin and Atlanta each delivered more than 3,000 units in the quarter.

When national and local supply move differently, a few local checks help:
1. Which communities nearby delivered homes this year?
2. Which are still offering lease up concessions?
3. How do their floor plans and prices overlap with yours?
4. When are they likely to stabilize?

A renter comparing homes this winter may be looking at those nearby lease ups, whatever the national total says.

How does your team track new communities as they open nearby?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: RealPage Analytics, U.S. Apartment Supply Update, 3rd Quarter 2026 (Oct 22, 2026) {RP} . More from Melanie Graham Prock: {ML}")

add("2026-11-23","08:11","Thanksgiving week: residents first",
"""Thanksgiving week puts the focus on the residents already at home.
The small things tend to get noticed most.

The office may close for the holiday, packages can pile up and guests come and go. What residents may remember most is whether they knew what to expect.

If I had to pick one thing to settle before the holiday, it would be making sure every resident knows how to reach maintenance after hours. Posted hours and a plan for packages come close behind.

It is not glamorous, but it can show up later in renewal conversations and reviews.

What is one holiday week detail your team never skips?

#Multifamily #PropertyManagement #ResidentExperience""",
f"More of my market analysis: {ML}",
"""Thanksgiving is this week, and many leasing offices will close for part of it.
Five details to settle before the holiday:

1. Office hours: posted on the community app, the door and the Google profile.
2. Maintenance emergencies: one clear after hours number, shared with every resident.
3. Packages: a plan for the extra volume while the office is closed.
4. Guests and parking: one reminder of the posted guest parking rules, sent to all residents.
5. A note of thanks: a short message to residents from the team.

These details rarely show up in a report, but residents tend to remember how a holiday week went.

What would you add to this list?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

add("2026-11-24","08:11","Holiday weekend renters: the online first impression",
"""Some renters may use the long weekend to look at apartments.
They may meet your community online before anyone at the office can answer.

That is worth a quick look before Thursday. Do the photos online still look like the community today? If someone sends a message on Friday, do they know when to expect a reply? Can they book a tour for Monday without having to call?

None of this takes long. But a renter browsing on the Friday after Thanksgiving is making a first impression of the community from whatever they can find, and the team is not there to explain the difference.

What does a renter find if they look you up on Thanksgiving Day?

#Multifamily #Leasing #ApartmentMarketing""",
f"More of my market analysis: {ML}",
"""When the leasing office closes for Thanksgiving, the online listing does the talking.
Three things to check before Thursday:

1. Holiday hours: does the Google profile show special hours for Thursday and Friday?
2. Voicemail: does the office greeting give the holiday hours and the emergency maintenance number?
3. Tours: can a renter request a tour for the following week online, without calling?

A renter browsing on a holiday has only what is online to go on. Making sure it is current is a small task with a long reach.

What is the last thing your team updates before the office closes for a holiday?

#Multifamily #Leasing #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

add("2026-11-25","08:11","What we are watching in December",
"""Before the holiday, a quick look at what I will be watching next.
Three releases that could change how this fall reads.

First, whether Phoenix renewal rent growth stays below zero in Yardi Matrix's coming reports, after September's negative 2.4%. Second, Apartment List's next vacancy reading, after 7.0% in October, down from a 7.3% peak in February. Third, the Bureau of Labor Statistics' Phoenix and Seattle price data on January 13, after Phoenix rents paid fell 1.4% from August to October and Seattle's rose 1.0%.

None of them will settle the question alone. Together they could help show whether this fall's softness in Arizona was a blip or a direction.

Happy Thanksgiving to everyone in this industry who keeps residents' homes running through the holiday.

What number are you watching most closely heading into December?

#Multifamily #ArizonaRealEstate #PropertyManagement""",
f"Sources: Yardi Matrix, National Multifamily Market Report, September 2026 (Oct 19, 2026) https://www.yardimatrix.com/blog/national-multifamily-market-report-september-2026/ . Apartment List National Rent Report {AL} . U.S. Bureau of Labor Statistics, Phoenix area and Seattle area CPI {BLS_PHX} and {BLS_SEA} . More of my market analysis: {ML}",
"""December and January bring fresh readings on rents and vacancy.
Here is where each one stands going in:

1. Yardi Matrix's coming reports: does Phoenix renewal rent growth stay below zero after negative 2.4% in September?
2. Apartment List's next national vacancy reading: does it keep easing from 7.0% in October?
3. The Bureau of Labor Statistics' Phoenix and Seattle price data, scheduled for January 13: does the rent index keep moving after Phoenix fell 1.4% and Seattle rose 1.0% from August to October?

Each is a single reading, and on its own any one of them may say little about a particular community.

Wishing every onsite team a restful Thanksgiving.

If one of these readings surprised you, which part of your plan would you revisit first?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Sources: Yardi Matrix, National Multifamily Market Report, September 2026 (Oct 19, 2026) https://www.yardimatrix.com/blog/national-multifamily-market-report-september-2026/ . Apartment List National Rent Report {AL} . U.S. Bureau of Labor Statistics, Phoenix area and Seattle area CPI {BLS_PHX} and {BLS_SEA} . More from Melanie Graham Prock: {ML}")

order={'2026-11-15':'2026-11-15','2026-11-22':'2026-11-16','2026-11-17':'2026-11-17','2026-11-21':'2026-11-18','2026-11-18':'2026-11-19','2026-11-16':'2026-11-20','2026-11-19':'2026-11-21','2026-11-20':'2026-11-22','2026-11-23':'2026-11-23','2026-11-24':'2026-11-24','2026-11-25':'2026-11-25'}
import datetime
for p in P:
    p['date']=order[p['date']]
    wd=datetime.date.fromisoformat(p['date']).weekday()
    if p['date']!='2026-11-15': p['time']='09:11' if wd>=5 else '08:11'
P.sort(key=lambda p:p['date'])
json.dump(P,open('posts.json','w'),indent=1)
md=''
for p in P:
    md+=f"## {p['date']} {p['time']} | {p['topic']}\n### Melanie (Metricool){' + image '+p['image'] if p['image'] else ''}\n{p['melanie']}\nFIRST COMMENT: {p['melanie_fc']}\n\n### Pillar Communities page (Michael posts by hand)\n{p['pillar']}\nFIRST COMMENT: {p['pillar_fc']}\n\n"
open('posts.md','w').write(md)
import re
print(len(P), re.findall('[–—]',md))
