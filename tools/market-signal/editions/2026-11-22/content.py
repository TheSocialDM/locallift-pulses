# Market Signal No. 05 content (built Sun Nov 22 2026). Run: python3 content.py -> posts.json, captions.md
import json,re,datetime
ML="https://themultifamilydesk.com/pillar/"
LEDGER="https://themultifamilydesk.com/pillar/ledger/"
NRC="https://www.census.gov/construction/nrc/pdf/newresconst_202610.pdf"
YPHX="https://www.yardimatrix.com/blog/phoenix-multifamily-market-report/"
YNAT="https://www.yardimatrix.com/blog/national-multifamily-market-report-september-2026/"
SRC_NRC=f"U.S. Census Bureau and HUD, New Residential Construction, October 2026 (Nov 18, 2026) {NRC}"
SRC_YPHX=f"Yardi Matrix, Phoenix Multifamily Market Report, September 2026 (Oct 5, 2026) {YPHX}"
P=[]
def add(date,topic,mel,melfc,pil,pilfc,image=None):
    wd=datetime.date.fromisoformat(date).weekday()
    P.append(dict(date=date,time='09:11' if wd>=5 else '08:11',topic=topic,melanie=mel.strip(),melanie_fc=melfc,pillar=pil.strip(),pillar_fc=pilfc,image=image))

add("2026-11-26","Market Signal No. 05: apartment starts jumped, permits slipped",
"""Apartment starts jumped in October.
I would not read too much into one month, and the earlier signal points the other way.

The Census Bureau and HUD put starts in buildings with five or more units at a 433,000 annual rate in October, up 22% from a year earlier. Permits for those buildings, which usually come first, came in at 475,000, down 5.2% from September and 0.4% from a year earlier. Census also notes the starts change is within its margin of error, so it is not statistically significant.

Why it matters in Arizona: homes started now often reach lease up in roughly two years, depending on the project. Yardi Matrix counted 24,400 apartments under construction in Phoenix in its September report, so new starts, if they hold up, may arrive in a market still absorbing what is being built today.

For an Arizona operator, the practical question is which projects breaking ground near our communities now could be leasing against us in 2028.

Happy Thanksgiving. I hope you get some time away from the numbers today.

Which projects near your communities are on your radar for 2028?

#Multifamily #ArizonaRealEstate #HousingStarts""",
f"Sources: {SRC_NRC} . {SRC_YPHX} . More of my market analysis: {ML}",
"""Apartment starts rose in October. Permits for the same kind of buildings slipped.
For a property team, the useful part is what it may mean two years out.

The Census Bureau and HUD estimate starts in buildings with five or more units at a 433,000 annual rate in October, up 22.0% from a year earlier, while permits for those buildings fell 5.2% from September and 0.4% from a year earlier. Census notes the starts change is within its margin of error, so one month may say little on its own.

New construction that starts now often reaches lease up in roughly two years, though timing varies. Questions worth adding to a long range plan:
1. Which floor plans and price points would a new community nearby compete with most directly?
2. What would the renewal approach be if two lease ups opened nearby at once?
3. Which services or amenities would still set the community apart?
4. How would the marketing budget shift during a nearby lease up?

How far ahead does your team plan for new competition?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: {SRC_NRC} . More from Melanie Graham Prock: {ML}",
image="market-signal-2026-11-22-no05-apartment-starts.png")

add("2026-11-27","December renewals deserve their own plan",
"""Renewal letters that arrive in the middle of the holidays get read differently.
I think December deserves its own renewal plan.

Between travel, guests and year end bills, a resident may open a renewal offer at the worst possible moment. A number on a page, with no context, can feel bigger than it is.

What I would rather see in December: a short conversation before the letter, a clear explanation of what is included, and enough time to decide without a holiday deadline hanging over it. The offer itself does not have to change for it to land better.

How does your team handle renewals that land over the holidays?

#Multifamily #PropertyManagement #ResidentRetention""",
f"More of my market analysis: {ML}",
"""Many renewal notices for early year lease ends go out in December.
A few points to settle before those notices go out:

1. Timing: does the notice give a resident time to decide after the holidays?
2. Conversation: does someone on the team reach out before the letter arrives?
3. Clarity: does the offer explain what is included and what changed?
4. Follow up: who answers questions while the office keeps holiday hours?

Small adjustments like these can shape how an offer is received without changing the offer itself.

Which part of the renewal process does your team review before year end?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

add("2026-11-28","Holiday weekend on call coverage",
"""Holiday weekends test the parts of a community nobody sees in a brochure.
The on call schedule is one of them.

A water heater does not care that it is the Saturday after Thanksgiving. When something breaks this weekend, the resident's experience will come down to how fast someone answers, how clearly they explain the next step and whether the follow up actually happens.

I have a lot of respect for the technicians and managers who carry the phone on weekends like this one. Their work rarely shows up in a report, but it may show up later in a renewal decision or a review.

How does your team thank the people who cover the holidays?

#Multifamily #PropertyManagement #MaintenanceTeams""",
f"More of my market analysis: {ML}",
"""Somebody on the team is carrying the on call phone this weekend.
A few habits make that weekend easier for them and for residents:

1. A handoff note before the weekend: open work orders, vendor contacts and homes in make ready.
2. A clear escalation path: who to call when the on call technician needs help.
3. A Monday debrief: what came in, what waited and what could be prevented next time.
4. Recognition: a thank you that names the people who covered.

A smooth holiday weekend usually starts with preparation the week before.

Which of these habits is hardest to keep up over a long weekend?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

add("2026-11-29","West housing starts fell while national apartment starts rose",
"""October's national construction headline may not describe the West.
Regional starts moved the other way.

The Census Bureau's October figures show total housing starts in the West 11.6% below a year earlier, even as single family starts in the region rose 7.0%. On those estimates, that implies fewer starts in buildings with two or more homes, though Census says both regional changes fall within its margin of error.

For Arizona, I take two things from that. First, a national headline may not describe our region. Second, if fewer apartments are breaking ground in the West now, the supply picture a couple of years out could look different here than the national number suggests.

One month is not a trend, and regional data are not Phoenix data. I would want to see a few more months before changing any plan.

Do you read regional construction data differently from national numbers?

#Multifamily #ArizonaRealEstate #Development""",
f"Source: {SRC_NRC} . More of my market analysis: {ML}",
"""Housing starts in the West were 11.6% below a year earlier in October, while single family starts in the region rose 7.0%.
Nationally, starts in buildings with five or more units rose.

Census notes both regional changes are within its margin of error. A split like this is a reminder that supply is best read close to home. Useful local sources include:
1. City permit records and planning agendas for the submarket.
2. Approved projects that have not yet broken ground.
3. Expected opening dates for communities within a few miles.

Local filings tend to be the more reliable read on what will open nearby.

Where does your team get its view of the local construction pipeline?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: {SRC_NRC} . More from Melanie Graham Prock: {ML}")

add("2026-11-30","Ledger: a checkpoint that waits for the source",
"""The market research I share follows one rule I like: every call gets checked later, on a date set in advance.
This week, one of those checks could not be graded yet.

The call was about Phoenix renewal rent growth, which Yardi Matrix reported at negative 2.4% in September. The checkpoint was Yardi's October report. Coverage of that report has appeared, but the Phoenix renewal figure could not be read on Yardi's own pages this week, so the check stays open until it can be.

It would be easy to grade a call from a secondhand summary. I would rather wait for the source.

How does your team decide which numbers are solid enough to act on?

#Multifamily #PropertyManagement #RealEstateResearch""",
f"Source for the September figure: Yardi Matrix, National Multifamily Report, September 2026 (Oct 19, 2026) {YNAT} . The ledger, with every call and checkpoint: {LEDGER}",
"""Before a market figure goes into a plan, three quick checks can save a lot of second guessing later:

1. Source: can the figure be found on the publisher's own page, not only in a summary?
2. Scope: does it name the period and the geography, such as metro, city or region?
3. Shape: is it one month, or a trend across several readings?

Figures that pass all three tend to be easier to defend in a budget meeting.

Which source does your team treat as the final word on your market?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {LEDGER}")

add("2026-12-01","Completions down while starts rose",
"""Census estimates fewer apartments were finished nationally in October than a year ago.
That is the other half of October's construction story.

The Census Bureau and HUD estimate completions in buildings with five or more units at a 362,000 annual rate in October, 9.0% below a year earlier, though that change is within the margin of error. Completions were up 9.0% from September, and starts for the same buildings ran higher.

So the pipeline may be thinning at the delivery end while it refills at the start. If that holds, the next year or so could bring some breathing room for communities that have been competing with lease ups, before newer projects arrive.

I would plan for that as a possibility and keep watching the numbers. In Arizona, the timing will depend on what is already under construction nearby.

What would your team do differently with fewer lease ups opening nearby?

#Multifamily #ArizonaRealEstate #Leasing""",
f"Source: {SRC_NRC} . More of my market analysis: {ML}",
"""Completions in buildings with five or more units ran 9.0% below a year earlier in October, at a 362,000 annual rate.
Starts for the same buildings ran higher.

The Census Bureau and HUD note the completions change falls within the margin of error. Even so, a possible lull in nearby deliveries raises practical questions for a property team:
1. If fewer lease ups open nearby next year, how quickly could concessions come down?
2. Which residents are most likely to be drawn to the next new opening?
3. What would the team invest in during a slower delivery year?

How is your team planning for the next year of deliveries nearby?

#Multifamily #PropertyManagement #PillarCommunities""",
f"Source: {SRC_NRC} . More from Melanie Graham Prock: {ML}")

add("2026-12-02","Year end review: what residents asked for",
"""Year end reviews tend to focus on occupancy and rent.
I would add one question that rarely makes the agenda: what did our residents tell us this year, and what did we change because of it?

Surveys, reviews, maintenance requests and move out reasons all carry that kind of signal. Collecting it is the easy part. Closing the loop, and telling residents what changed, takes more effort.

When it does happen, I think residents notice, in renewal conversations and in what they say about the community online.

What is one change your team made this year because residents asked for it?

#Multifamily #PropertyManagement #ResidentExperience""",
f"More of my market analysis: {ML}",
"""A year end review question that is easy to skip: what did residents ask for this year, and what changed?
Four places to look:

1. Review themes, both positive and negative.
2. Maintenance requests that keep repeating.
3. Move out reasons.
4. Survey comments.

Then one more step: tell residents what changed because of their feedback.

Which source of resident feedback does your team find most useful?

#Multifamily #PropertyManagement #PillarCommunities""",
f"More from Melanie Graham Prock: {ML}")

LOCALLIFT=dict(date="2026-11-30",account="LocalLift / The SocialDM company page (post after 12 PM)",text="""More apartments are starting construction than a year ago.
We think many of them will end up competing for the same neighborhood searches your community appears in today.

Census Bureau data show starts in buildings with five or more units at 364,500 from January through October, compared with 336,600 a year earlier, before seasonal adjustment. Census notes that change is within its margin of error.

Many renters start with a place rather than a name: apartments near a hospital, a campus or the freeway they commute on. As new communities open nearby, those searches may get more crowded. Communities that clearly describe their location, nearby employers and commute times could be easier for Google and AI assistants to match to the question.

For marketing teams, the next two years may be a useful window to spell out the neighborhood a community serves everywhere renters look.

Which neighborhood search would you most want your community to show up for?

#Multifamily #ApartmentMarketing #LocalSEO""",fc=f"Source: {SRC_NRC}")

MICHAEL=dict(date="2026-12-01",time="07:41",account="Michael Shad personal LinkedIn (Metricool for approval, Tue Dec 1 7:41 AM Phoenix)",image="market-signal-2026-11-22-no05-michael-new-buildings.png",text="""A new apartment building often gets noticed online just for being new.
The established one down the street has to earn it.

The Census Bureau and HUD put October starts in buildings with five or more units at a 433,000 annual rate, up 22% from a year earlier. One month can be noisy, and Census says the change is within its margin of error.

My read as a marketer: if those starts hold up, a renter in a couple of years may be comparing an established community with a brand new one, side by side, in Google and in AI answers.

This is the gap between being seen and being chosen. The new building may get seen because it is new. The established one can still get chosen if what a renter finds is current and specific.

Before those buildings open, I would run three checks:
1. Ask an AI assistant to compare your community with the newest one nearby. What does it say about each?
2. Read your last 20 reviews. Does your website lead with what residents praise most?
3. Find the newest photo on your Google profile. Would a renter guess it was taken this year?

What would a renter see first if they compared your community with the newest one in town?

#Multifamily #ApartmentMarketing #AISearch""",fc=f"Source: {SRC_NRC}")

if __name__=='__main__':
    json.dump(dict(daily=P,locallift=LOCALLIFT,michael=MICHAEL),open('posts.json','w'),indent=1)
    md='# Market Signal No. 05 captions (built Nov 22 2026)\n\n'
    for p in P:
        md+=f"## {p['date']} {p['time']} | Melanie (Metricool brand 5426985){' + image '+p['image'] if p['image'] else ''} | {p['topic']}\n{p['melanie']}\nFIRST COMMENT: {p['melanie_fc']}\n\n### Pillar Communities page, same day (Michael posts by hand after Melanie's post)\n{p['pillar']}\nFIRST COMMENT: {p['pillar_fc']}\n\n"
    md+=f"## {LOCALLIFT['date']} | {LOCALLIFT['account']}\n{LOCALLIFT['text']}\nFIRST COMMENT: {LOCALLIFT['fc']}\n\n"
    md+=f"## {MICHAEL['date']} | {MICHAEL['account']} | {MICHAEL['image']}\n{MICHAEL['text']}\nFIRST COMMENT: {MICHAEL['fc']}\n"
    open('captions.md','w').write(md)
    bad=re.findall('[–—]| - ',md); print(len(P),'dash hits',bad)
