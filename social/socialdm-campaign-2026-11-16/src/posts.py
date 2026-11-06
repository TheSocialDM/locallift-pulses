import json,re
LI='https://www.thesocialdm.com/'
P=[]
def proof(d,li,fb,tags,lc,fc,src):
    P.append(dict(slot=f'{d}-li',date=f'2026-11-{d}T13:00:00',net='linkedin',text=li+'\n\n'+tags,first=lc,src=src))
    P.append(dict(slot=f'{d}-fb',date=f'2026-11-{d}T13:00:00',net='facebook',text=fb+'\n\n'+tags,first=fc,src=src))

proof('06',
"""591 website clicks from one Google listing in four weeks.
That is up 29% from the four weeks before.

This is an apartment community we work with in the Southwest, over the 28 days to October 30. The same weeks last year came in at 521, so the time of year probably does not explain all of it.

Why watch that one button? Someone tapping through to the website has usually moved past the map and wants the details: floor plans, fees, how to book a tour. It is a sign of interest, and a click does not sign a lease on its own, so I would not report it like one.

It is still useful, because a property team can act on it. If clicks climb and tours stay flat, the question moves from the listing to the website.

I also can't pin the rise on one thing. Specials and search demand move this number too.

Google Business Profile optimization is one part of how we work with apartment communities.

If your website clicks jumped 29% next month, where would you look first?""",
"""One Google listing we work with sent 591 clicks to its website in four weeks, up from 459 the four weeks before.

That is one apartment community in the Southwest, over the 28 days to October 30. The same weeks last year it was 521.

We read a number like that this way. A click tells you someone wanted to know more. It doesn't tell you they toured or that they signed. So the useful next step is checking what happens after the tap. Do the floor plans load fast on a phone? Is the tour button easy to find?

Specials and search demand move this number too, so we don't credit any one thing for the jump.

What is the first thing you check on an apartment website?""",
'#Multifamily #GoogleBusinessProfile #ApartmentMarketing',
'How we approach Google Business Profile work for communities: https://www.thesocialdm.com/multifamily-marketing-agency',
'More on the work behind Google listings for apartment communities: https://www.thesocialdm.com/multifamily-marketing-agency',
'Elevation on Central, website clicks Oct 3 to 30 2026: 591; Sep 5 to Oct 2 2026: 459; Oct 3 to 30 2025: 521')

proof('09',
"""620 calls, website clicks and direction requests from one Google listing in 28 days.
Those rose 23%. Views of the listing rose 14%.

That gap is the part I keep looking at. This is an apartment community we work with in Arizona, in the 28 days to October 30 against the 28 days before. Actions went from 505 to 620 while views went from 1,579 to 1,806. The same weeks last year had 511 actions.

So more of the people who saw the listing did something about it: about 34 actions per 100 views, up from 32. Small move, and four weeks is not a trend. A view is also a search rather than a person, so I hold this loosely.

I still like the direction, because views alone can flatter you. Some reports stop at "views are up." The better question is whether the listing is giving people a reason to tap.

That can come down to a current first photo, hours that match, details that answer the question they searched. Specials and season may play a part here too.

When views rise, what else does your report show you about that month?""",
"""Views are nice. What people do next is better.

One apartment listing we work with in Arizona had 620 calls, website clicks and direction requests in the 28 days to October 30. The 28 days before, it had 505. Views grew too, from 1,579 to 1,806, but more slowly than the actions did.

In plain terms, more of the people who saw the listing tapped something: about 34 actions for every 100 views, up from about 32. It is a small move over four weeks and we wouldn't call it a trend. Specials and the season may be part of it.

We like this little math problem anyway, because it asks a better question than "how many saw it?"

When you look up an apartment on Google, what do you tap first?""",
'#Multifamily #PropertyManagement #LocalSEO',
'One renter, several places to find you, and how they fit together: https://www.thesocialdm.com/blog/search-engine-marketing-multifamily',
'How the pieces of apartment search fit together: https://www.thesocialdm.com/blog/search-engine-marketing-multifamily',
'The View at Cascade, Oct 3 to 30 2026: calls 60, web 306, directions 254 = 620, impressions 1,806; Sep 5 to Oct 2 2026: 43, 245, 217 = 505, impressions 1,579; Oct 3 to 30 2025: 56, 279, 176 = 511')

proof('12',
"""Calls from one Google listing: 33 last October, 31 this October.
Direction requests over the same weeks: 203, then 506.

A manager tracking only the phone would see a flat year. The other numbers moved a lot. It belongs to an apartment community we work with in the Southwest, and calls, website clicks and direction requests together went from 470 to 892 for the 28 days to October 30 against the same weeks in 2025.

Part of that is likely a community one year further along, and I won't claim otherwise.

The lesson I take from it is about what we count. Google's call number only counts taps on the call button, so it misses anyone who dials by hand. A renter who wants to see a place may just ask for directions and show up. Website clicks went from 234 to 355 too, and most of that movement would not show up in a phone log.

Any one of these is an incomplete signal. Read together, and checked against tours, they say more.

Google profile work is part of how we help communities get found, and this is how we like to read it.

Of calls, website clicks and direction requests, which does your report lean on most?""",
"""Calls from one Google listing barely moved, and direction requests more than doubled.

One apartment listing we work with in the Southwest got 31 calls from its Google listing in the 28 days to October 30. Same weeks last year: 33. If you only count calls, that looks like a flat year.

Direction requests over those same weeks went from 203 to 506, and website clicks went from 234 to 355.

Some of that is likely a community that is one year further along. Still, plenty of people seem happy to skip the phone call altogether and just look up how to get there.

So when someone asks whether the listing is working, one number rarely answers it.

Do you call an apartment community before you visit, or just go?""",
'#Multifamily #GoogleMaps #LeasingStrategy',
'What calls, clicks and direction requests each count on a Google listing: https://www.thesocialdm.com/blog/multifamily-marketing-metrics',
'Why one number rarely tells the whole story on a Google listing: https://www.thesocialdm.com/blog/multifamily-marketing-metrics',
'Coya, Oct 3 to 30 2026: calls 31, web 355, directions 506 = 892; Oct 3 to 30 2025: 33, 234, 203 = 470')

G=[
dict(slot='16-g',date='2026-11-16T07:00:00',img='g-1116-specials-talk.png',
alt='Black graphic labeled Market read with an Illustrative tag and the headline "Every special says something." A four row table: Nearby A, no change, quiet week; Nearby B, special added on one floor plan, may point to one slow floor plan; Nearby C, offer raised, second week in a row, may be behind on leasing goals; Nearby D, offer shrank, demand may be catching up. A caption at the bottom right reads What changed this week. The SocialDM logo.',
text="""When a community nearby adds a special, the first reaction is usually to ask what it will cost you to respond. We think the more useful question is what that special is saying. A competitor raising its offer two weeks in a row is often running behind on its leasing goals. A special on one floor plan can point to one hard to lease home type, which is a different problem from a slow market. And when offers shrink across several properties at once, demand may be catching up.

The table on this graphic is illustrative, not client data. It shows how we like to read a market: what changed since last week, on which floor plans, and what it may mean. Change from week to week tends to say more than a market average, because a monthly comp report shows where the market was rather than where it may be heading. Read this way, each week can end in one clear action, or a note that nothing needs to change.

Our article on concessions walks through these signals in more detail, along with how to define a real competitive set.

https://www.thesocialdm.com/blog/concessions-are-a-signal-not-just-a-cost-why-lease-ups-need-a-weekly-market-read"""),
dict(slot='17-g',date='2026-11-17T07:00:00',img='g-1117-holiday-hours.png',
alt='Red poster labeled Holiday hours and Thursday, Nov. 26, with a very large black numeral 26. White headline "Closed Thursday?" above the line "Tell Google before a renter finds out." A black band at the bottom holds the LocalLift logo and the line "Set special hours ahead of the holiday."',
text="""Thanksgiving falls on Thursday, November 26 this year, and a long weekend can give some renters time to look around. Picture someone checking your Google profile that morning, seeing regular hours, and driving over to a locked office. It is a small mismatch, and it may be the first impression they get of how closely the community pays attention.

Google lets a business set special hours for specific dates ahead of time, so a profile can show closed on the holiday or shorter hours the day after, while the regular schedule stays as it is. It is easy to miss during a busy week. The website and the tour steps are worth a look at the same time, so a renter gets the same answer in each place.

Holiday hours are one of the small items in our article on the slower winter leasing season, along with current photos, answered reviews and plain answers on fees, pets and parking.

https://www.thesocialdm.com/blog/winter-leasing-apartment-marketing"""),
dict(slot='18-g',date='2026-11-18T07:00:00',img='g-1118-decide.png',
alt='Photo of a woman with a laptop on a gray sofa beside a husky dog in a bright white living room. Below it, the label Social that helps, the headline "Is your feed helping her decide?" and five words in a row: Location, Price, Concessions, Amenities, Lifestyle. The line "Five things renters tend to weigh." The SocialDM logo.',
text="""Someone on the sofa with a laptop and a dog at her side may look like she is browsing. If she is comparing apartments, she is more likely working through a decision. Is the location right? Does the price work? Is there a concession worth weighing? Do the amenities fit? What would a normal Tuesday feel like here? Those five questions make a useful test for any community's social feed.

A post can look lovely and still answer none of them. A short video of the walk to the nearest coffee shop says something about location and daily life. A clear explanation of what a concession means helps with price. A look at the fitness center at the hour people actually use it says more than a wide shot with nobody in it.

At The SocialDM we call this decision based social media: content shaped by how renters weigh a community, across Instagram, Facebook, TikTok and YouTube. Our multifamily marketing page explains how that approach sits alongside apartment SEO and Google Business Profile work.

https://www.thesocialdm.com/multifamily-marketing-agency"""),
dict(slot='19-g',date='2026-11-19T07:00:00',img='g-1119-last-january.png',
alt='Dark brick apartment facade with balconies at dusk under the label Winter leasing. White text reads "Judge this January against" above the word August struck through in red, then Last January in large serif type, and the line "Slower months read differently when you compare them to your own last winter." LocalLift logo.',
text="""Sometime after the holidays, someone will open a leasing report, see fewer tours than August, and start asking what went wrong. Often nothing did. Apartment demand tends to be seasonal, with most of it falling roughly between April and September, though the pattern varies a lot by market. A Phoenix winter and a Chicago winter are very different leasing seasons, which is why a community's own history is usually the better guide.

That is why we suggest measuring a winter month against last winter rather than against summer. Tours and leases by source, cost per lease by channel, renewals and visibility on searches that do not include your name all read more honestly that way. Fewer leases can still mean a plan is working, as long as your share of relevant searches is holding. Winter also tends to bring renters who have a reason to move soon, so accurate prices, availability and tour steps can matter more than broad awareness.

Our article on the slower winter season goes through what to track, and what to fix while things are calmer.

https://www.thesocialdm.com/blog/winter-leasing-apartment-marketing"""),
]
for g in G:
    g['net']='gmb'; g['first']=''
json.dump(dict(proof=P,google=G),open('posts.json','w'),indent=1,ensure_ascii=False)
for p in P+G:
    body=p['text']; w=len(body.split()); print(p['slot'],w,len(body),'dash' if re.search(r'[–—]|\w-\w',body.split('https')[0]) else '', len(re.findall(r'#\w+',body)))
