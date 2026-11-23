from base import *

# 1 Tue Nov 24, light, mock form (Field Notes week 1 short)
T['s-1124-behind-form'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">AI search</div>
<div class="ex abs" style="right:80px;top:74px">Example</div>
<div class="pf abs" style="left:80px;top:150px;width:900px;font-size:88px;line-height:1.04;font-weight:500;color:#0E0E0E">Your best answer may be behind a <span class="it red">form.</span></div>
<div class="abs" style="left:80px;top:520px;width:920px;background:#fff;border:2px solid #0E0E0E;padding:44px 48px;box-shadow:16px 16px 0 #E8E4DC">
  <div class="plex" style="font-size:34px;font-weight:600;color:#0E0E0E">Get our pet policy and parking guide</div>
  <div class="mono" style="font-size:20px;color:#5E5952;margin-top:34px">Name</div>
  <div style="height:64px;border:2px solid #C9C4BA;margin-top:10px"></div>
  <div class="mono" style="font-size:20px;color:#5E5952;margin-top:24px">Email</div>
  <div style="height:64px;border:2px solid #C9C4BA;margin-top:10px"></div>
  <div class="osw" style="margin-top:30px;display:inline-block;background:#0E0E0E;color:#FAFAF8;font-size:30px;font-weight:600;letter-spacing:.04em;padding:14px 34px">Send me the guide</div>
</div>
<div class="news it abs" style="left:80px;top:1078px;width:640px;font-size:38px;line-height:1.22;color:#0E0E0E">A renter can fill it out. An AI tool generally can't.</div>
{foot('ll', False, right=80, bottom=86)}
''')

# 2 Wed Nov 25, dark, full bleed windows photo
T['s-1125-lights-on'] = S(f'''
<div class="photo" style="inset:0;{ph('16816328','50% 45%')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(6,10,14,0) 30%,rgba(6,10,14,.55) 55%,rgba(6,10,14,.93) 78%)"></div>
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FAFAF8;background:rgba(14,14,14,.55);padding:8px 12px">Holiday week</div>
<div class="fra abs" style="left:80px;top:830px;width:900px;font-size:92px;line-height:1.0;font-weight:400;color:#FAFAF8;letter-spacing:-.02em">The lights are on. <span class="it" style="color:#FF8A75">Is the office?</span></div>
<div class="plex abs" style="left:80px;top:1052px;width:640px;font-size:30px;line-height:1.35;color:#E9E5DE">Post holiday hours where renters check first: Google, the website and social.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 3 Thu Nov 26, cream, type only Thanksgiving
T['s-1126-thank-you'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">Thursday, November 26</div>
<div class="fra it abs" style="left:66px;top:150px;font-size:250px;line-height:.9;font-weight:300;color:#0E0E0E;letter-spacing:-.04em">Thank</div>
<div class="fra it abs" style="left:300px;top:370px;font-size:250px;line-height:.9;font-weight:300;color:#D2321E;letter-spacing:-.04em">you.</div>
<div class="abs" style="left:80px;top:720px;width:920px;border-top:3px solid #0E0E0E"></div>
<div class="news abs" style="left:80px;top:756px;width:880px;font-size:40px;line-height:1.35;color:#0E0E0E">To everyone on call today. To the teams who keep keys, doors and hours right all year. And to everyone who reads along and shares these posts.</div>
<div class="plex abs" style="left:80px;top:1040px;font-size:30px;color:#5E5952">Happy Thanksgiving from The SocialDM.</div>
{foot('sdm', False, right=80, bottom=70)}
''', bg='#E8E4DC')

# 4 Fri Nov 27, dark, three column comparison
cols = [('Community A', ['Photos from this year', 'Special shows an end date', 'Holiday hours posted']),
        ('Community B', ['Photos from 2022', 'Special with no end date', 'Hours missing']),
        ('Community C', ['Photos from this year', 'No special listed', 'Shows open Thursday'])]
cards = ''.join(f'''<div style="width:290px;background:#1C1B19;border-top:6px solid {'#D2321E' if i==1 else '#FAFAF8'};padding:26px 22px 30px">
<div class="osw" style="font-size:34px;font-weight:600;color:#FAFAF8;letter-spacing:.01em">{n}</div>
{''.join(f'<div class="plex" style="font-size:25px;line-height:1.3;color:#E3DED6;border-top:1px solid #3A3835;padding:16px 0 14px;margin-top:{16 if j==0 else 0}px">{r}</div>' for j,r in enumerate(rows))}
</div>''' for i,(n,rows) in enumerate(cols))
T['s-1127-side-by-side'] = S(f'''
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FF8A75">Black Friday</div>
<div class="ex abs" style="right:80px;top:74px">Illustrative</div>
<div class="anton abs" style="left:76px;top:140px;width:940px;font-size:118px;line-height:.98;color:#FAFAF8">Renters compare<br>side by side.</div>
<div class="news it abs" style="left:80px;top:400px;width:900px;font-size:38px;line-height:1.25;color:#CFCAC1">Not only this Friday. Every week, on one phone.</div>
<div class="abs" style="left:80px;top:530px;width:920px;display:flex;gap:25px">{cards}</div>
{foot('sdm', True, left=80, bottom=70)}
''', bg='#0E0E0E')

# 5 Sat Nov 28, light, split photo left
T['s-1128-coffee-shop'] = S(f'''
<div class="photo" style="left:0;top:0;width:560px;height:1350px;{ph('15101682','100% 50%')}"></div>
<div class="mono red abs" style="left:616px;top:80px;font-size:22px;line-height:1.5">Small Business<br>Saturday</div>
<div class="pf abs" style="left:616px;top:230px;width:400px;font-size:66px;line-height:1.08;font-weight:500;color:#0E0E0E">The coffee shop down the street is part of the <span class="it red">tour.</span></div>
<div class="abs" style="left:616px;top:800px;width:384px;border-top:2px solid #0E0E0E"></div>
<div class="plex abs" style="left:616px;top:830px;width:384px;font-size:29px;line-height:1.4;color:#3A3631">Renters choose a neighborhood along with a floor plan. Show them the places nearby.</div>
{foot('sdm', False, left=616, bottom=70)}
''')

# 6 Sun Nov 29, red, Swiss type
T['s-1129-december'] = S(f'''
<div class="anton abs" style="left:52px;top:40px;font-size:520px;line-height:.86;color:transparent;-webkit-text-stroke:4px #FAFAF8;letter-spacing:-.01em">Dec</div>
<div class="mono abs" style="left:80px;top:540px;font-size:24px;color:#FAFAF8">Year end leasing</div>
<div class="osw abs" style="left:80px;top:600px;width:920px;font-size:96px;line-height:1.02;font-weight:700;color:#0E0E0E">Fewer renters search in December.</div>
<div class="osw abs" style="left:80px;top:820px;width:920px;font-size:96px;line-height:1.02;font-weight:700;color:#FAFAF8">Many who do have a date to move.</div>
<div class="plex abs" style="left:80px;top:1040px;width:620px;font-size:30px;line-height:1.35;color:#0E0E0E">Make sure what they find this month is current.</div>
<div class="abs" style="left:0;right:0;bottom:0;height:200px;background:#0E0E0E"></div>
{foot('sdm', True, right=80, bottom=48)}
''', bg='#D2321E')

# 7 Mon Nov 30, light, vertical split says vs can use (Field Notes week 2 short)
T['s-1130-close-to'] = S(f'''
<div class="abs" style="left:0;top:0;width:540px;height:1350px;background:#ECE9E3"></div>
<div class="abs" style="left:540px;top:0;width:540px;height:1350px;background:#0E0E0E"></div>
<div class="mono abs" style="left:60px;top:80px;font-size:22px;color:#5E5952">What the site says</div>
<div class="mono abs" style="left:600px;top:80px;font-size:22px;color:#FF8A75">What a renter can use</div>
<div class="pf it abs" style="left:60px;top:300px;width:430px;font-size:76px;line-height:1.08;color:#8A847B">"Close to everything."</div>
<div class="bsd abs" style="left:598px;top:290px;width:440px;font-size:90px;line-height:.92;font-weight:800;color:#FAFAF8">12 minutes to downtown by rail.</div>
<div class="ex abs" style="left:600px;top:860px">Example</div>
<div class="news abs" style="left:60px;top:960px;width:960px;font-size:40px;line-height:1.25;color:#0E0E0E;mix-blend-mode:normal"></div>
<div class="news it abs" style="left:60px;top:1000px;width:420px;font-size:36px;line-height:1.25;color:#0E0E0E">A feeling sells the home.</div>
<div class="news it abs" style="left:600px;top:1000px;width:420px;font-size:36px;line-height:1.25;color:#FAFAF8">A fact is easier for AI to repeat.</div>
{foot('ll', False, left=60, bottom=80)}
''')

# 8 Tue Dec 1, dark, rain photo
T['s-1201-umbrella'] = S(f'''
<div class="photo" style="inset:0;{ph('7536597','40% 50%','auto 100%')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(8,9,11,.82) 0%,rgba(8,9,11,.35) 34%,rgba(8,9,11,.2) 55%,rgba(8,9,11,.85) 82%)"></div>
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FAFAF8">Winter traffic</div>
<div class="news abs" style="left:80px;top:140px;width:900px;font-size:84px;line-height:1.02;font-weight:400;color:#FAFAF8;letter-spacing:-.01em">Winter tours start on a phone, <span class="it">under an umbrella.</span></div>
<div class="plex abs" style="left:80px;top:1090px;width:600px;font-size:30px;line-height:1.35;color:#EDEAE4">Rain, cold or sunshine, the first visit is the search.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 9 Wed Dec 2, light, calendar
days = ''
for d in range(1, 36):
    n = d - 2
    lab = ''
    style = 'color:#0E0E0E'
    if n == 10: lab = 'Invite'; style = 'color:#FAFAF8;background:#D2321E'
    if n == 13: lab = 'Recap'; style = 'color:#FAFAF8;background:#0E0E0E'
    txt = str(n) if 1 <= n <= 31 else ''
    days += f'<div style="height:96px;border-top:1px solid #DAD6CE;padding:8px 10px;{style}"><div class="bsd" style="font-size:34px;font-weight:700">{txt}</div><div class="mono" style="font-size:16px;margin-top:4px">{lab}</div></div>'
T['s-1202-two-posts'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">Resident events</div>
<div class="ex abs" style="right:80px;top:74px">Illustrative</div>
<div class="fra abs" style="left:80px;top:140px;width:920px;font-size:96px;line-height:1.0;font-weight:400;color:#0E0E0E;letter-spacing:-.02em">One resident event, <span class="it red">two posts.</span></div>
<div class="abs" style="left:80px;top:400px;width:920px">
 <div class="mono" style="display:grid;grid-template-columns:repeat(7,1fr);font-size:18px;color:#5E5952;padding-bottom:10px"><div>Sun</div><div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div></div>
 <div style="display:grid;grid-template-columns:repeat(7,1fr);border-bottom:1px solid #DAD6CE">{days}</div>
</div>
<div class="news it abs" style="left:80px;top:1010px;width:900px;font-size:36px;line-height:1.28;color:#0E0E0E">The invite tells renters what happens here. The recap shows that it did.</div>
{foot('sdm', False, right=80, bottom=70)}
''')

# 10 Thu Dec 3, dark, chat mock
T['s-1203-ask-why'] = S(f'''
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FF8A75">AI search for apartments</div>
<div class="ex abs" style="right:80px;top:74px">Example</div>
<div class="plex abs" style="left:80px;top:146px;width:900px;font-size:46px;line-height:1.2;color:#CFCAC1;font-weight:300">Ask an AI for apartments near you.</div>
<div class="osw abs" style="left:78px;top:206px;font-size:122px;line-height:1;font-weight:700;color:#FAFAF8;white-space:nowrap">Then ask it why.</div>
<div class="abs" style="right:80px;top:470px;width:640px;background:#FAFAF8;color:#0E0E0E;padding:26px 30px;border-radius:26px 26px 4px 26px" ><div class="plex" style="font-size:30px;line-height:1.35">Why did you pick those three communities?</div></div>
<div class="abs" style="left:80px;top:650px;width:760px;background:#24231F;color:#EDEAE4;padding:28px 32px;border-radius:26px 26px 26px 4px"><div class="plex" style="font-size:29px;line-height:1.4">The first lists its pet rules and parking on its website. The second has recent reviews about maintenance. The third shows current hours and photos.</div></div>
<div class="news it abs" style="left:80px;top:1010px;width:700px;font-size:36px;line-height:1.25;color:#FAFAF8">The reasons show which details it could find.</div>
{foot('ll', True, right=80, bottom=86)}
''', bg='#0E0E0E')

# 11 Fri Dec 4, light, crane photo band
T['s-1204-lease-up'] = S(f'''
<div class="photo" style="left:0;top:0;width:1080px;height:700px;{ph('4513940','62% 50%')}"></div>
<div class="mono red abs" style="left:80px;top:750px;font-size:24px">Lease up</div>
<div class="bsd abs" style="left:76px;top:790px;font-size:200px;line-height:.86;font-weight:900;color:#0E0E0E">Day one</div>
<div class="fra it abs" style="left:80px;top:972px;width:940px;font-size:52px;line-height:1.06;font-weight:400;color:#0E0E0E">happens online, before the doors open.</div>
<div class="plex abs" style="left:80px;top:1130px;width:600px;font-size:27px;line-height:1.4;color:#3A3631">Profile, photos and answers can be ready long before move in day.</div>
{foot('sdm', False, right=80, bottom=70)}
''')

# 12 Sat Dec 5, dark, patio lights photo led
T['s-1205-dusk'] = S(f'''
<div class="photo" style="inset:0;{ph('17813247','50% 40%')}"></div>
<div class="abs" style="left:0;right:0;bottom:0;height:520px;background:linear-gradient(180deg,rgba(10,8,6,0) 0%,rgba(10,8,6,.88) 45%)"></div>
<div class="mono abs" style="left:80px;top:850px;font-size:24px;color:#FFD9A0">Photo tip</div>
<div class="pf it abs" style="left:80px;top:900px;width:860px;font-size:68px;line-height:1.1;color:#FAFAF8">Shoot the lights at dusk, while the sky still has color.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 13 Sun Dec 6, light, contents page
rows = [('01', 'Reread your reviews like a renter would.'), ('02', 'Find the oldest photo of you online.'),
        ('03', 'Ask an AI what it knows about you.'), ('04', 'Give every special an end date.')]
T['s-1206-year-review'] = S(f'''
<div class="abs" style="left:80px;right:80px;top:80px;display:flex;justify-content:space-between" ><span class="mono" style="font-size:22px">The year in review</span><span class="mono red" style="font-size:22px">December 2026</span></div>
<div class="abs" style="left:80px;right:80px;top:124px;border-top:3px solid #0E0E0E"></div>
<div class="ins abs" style="left:74px;top:150px;font-size:210px;line-height:.95;color:#0E0E0E;letter-spacing:-.02em">Contents</div>
<div class="news it abs" style="left:80px;top:380px;width:900px;font-size:38px;color:#3A3631">Four reads before the year closes.</div>
<div class="abs" style="left:80px;right:80px;top:500px">{''.join(f'<div style="display:flex;gap:34px;align-items:baseline;border-top:1px solid #0E0E0E;padding:30px 0 30px"><span class="bsd" style="font-size:64px;font-weight:800;color:#D2321E;width:80px">{n}</span><span class="news" style="font-size:44px;line-height:1.2;color:#0E0E0E">{t}</span></div>' for n,t in rows)}<div style="border-top:1px solid #0E0E0E"></div></div>
{foot('sdm', False, right=80, bottom=60, h=96)}
''')

# 14 Mon Dec 7, dark, tally card (Field Notes week 3 short)
tal = [('Parking', 7), ('Package delivery', 6), ('Pet rules', 4)]
def marks(n):
    g = []
    while n > 0:
        k = min(5, n); g.append('|' * k if k < 5 else '<s>||||</s>'); n -= k
    return '&nbsp;&nbsp;'.join(g)
T['s-1207-tally'] = S(f'''
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FF8A75">Original knowledge</div>
<div class="fra abs" style="left:80px;top:140px;width:920px;font-size:86px;line-height:1.02;font-weight:400;color:#FAFAF8;letter-spacing:-.02em">What did renters ask most <span class="it" style="color:#FF8A75">this fall?</span></div>
<div class="abs" style="left:150px;top:470px;width:780px;background:#FAFAF8;padding:40px 46px;transform:rotate(-2deg);box-shadow:0 30px 60px rgba(0,0,0,.45)">
 <div style="display:flex;justify-content:space-between"><span class="mono" style="font-size:20px;color:#5E5952">Tour questions, November</span><span class="ex" style="font-size:18px">Example</span></div>
 {''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;border-top:1px solid #DAD6CE;padding:22px 0;margin-top:{20 if i==0 else 0}px"><span class="news" style="font-size:40px;color:#0E0E0E">{q}</span><span class="mono" style="font-size:40px;letter-spacing:.05em;color:#D2321E">{marks(n)}</span></div>' for i,(q,n) in enumerate(tal))}
</div>
<div class="plex abs" style="left:80px;top:1060px;width:620px;font-size:31px;line-height:1.35;color:#E3DED6">Your team hears it every day. Few websites ever say it.</div>
{foot('ll', True, right=80, bottom=86)}
''', bg='#161514')

# 15 Tue Dec 8, light, four dates
dates = ['12.24', '12.25', '12.31', '1.1']
T['s-1208-four-dates'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">Holiday hours</div>
<div class="pf abs" style="left:80px;top:140px;width:920px;font-size:92px;line-height:1.02;font-weight:500;color:#0E0E0E">Four dates renters <span class="it red">will check.</span></div>
<div class="abs" style="left:80px;top:420px;width:920px;display:grid;grid-template-columns:1fr 1fr;gap:0">
{''.join(f'<div style="border-top:3px solid #0E0E0E;padding:20px 0 34px"><div class="bsd" style="font-size:150px;line-height:.9;font-weight:900;color:#0E0E0E">{d}</div><div class="mono red" style="font-size:24px;margin-top:10px">Hours?</div></div>' for d in dates)}
</div>
<div class="plex abs" style="left:80px;top:960px;width:640px;font-size:30px;line-height:1.35;color:#3A3631">Set special hours on Google before the week arrives, then match the website.</div>
{foot('sdm', False, right=80, bottom=70)}
''')

# 16 Wed Dec 9, dark, ask first
T['s-1209-ask-first'] = S(f'''
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FAFAF8">Resident event photos</div>
<div class="anton abs" style="left:68px;top:150px;font-size:400px;line-height:.86;color:#D2321E">Ask</div>
<div class="anton abs" style="left:72px;top:500px;font-size:400px;line-height:.86;color:transparent;-webkit-text-stroke:4px #FAFAF8">first.</div>
<div class="abs" style="left:80px;top:910px;width:920px;border-top:3px solid #FAFAF8"></div>
<div class="plex abs" style="left:80px;top:940px;width:880px;font-size:38px;line-height:1.32;color:#FAFAF8">Get a clear yes before a resident's face goes on the feed. Then the recap can run with confidence.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 17 Thu Dec 10, light, three snapshot cards
snaps = [('October', ['Community B', 'Community A', 'Community D']), ('November', ['Community A', 'Community C', 'Community B']), ('December', ['Community C', 'Community A', 'Community E'])]
T['s-1210-answer-changes'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">AI answers</div>
<div class="ex abs" style="right:80px;top:74px">Illustrative</div>
<div class="fra abs" style="left:80px;top:140px;width:920px;font-size:92px;line-height:1.0;font-weight:500;color:#0E0E0E;letter-spacing:-.02em">The answer <span class="it red">changes.</span></div>
<div class="plex abs" style="left:80px;top:258px;width:900px;font-size:34px;line-height:1.3;color:#3A3631">Same question, asked three months in a row.</div>
<div class="abs" style="left:80px;top:380px;width:920px;display:flex;gap:24px">
{''.join(f'<div style="flex:1;border:2px solid #0E0E0E;background:{"#0E0E0E" if i==2 else "#FFFFFF"};padding:24px 22px"><div class="mono" style="font-size:20px;color:{"#FF8A75" if i==2 else "#D2321E"}">{m}</div>{"".join(f"<div class=\'plex\' style=\'font-size:27px;line-height:1.3;color:{chr(35)+"FAFAF8" if i==2 else chr(35)+"0E0E0E"};border-top:1px solid {chr(35)+"3A3835" if i==2 else chr(35)+"DAD6CE"};padding:16px 0;margin-top:{14 if j==0 else 0}px\'><span class=\'bsd\' style=\'font-weight:800;font-size:30px;margin-right:10px\'>{j+1}</span>{c}</div>" for j,c in enumerate(l))}</div>' for i,(m,l) in enumerate(snaps))}
</div>
<div class="news it abs" style="left:80px;top:860px;width:900px;font-size:44px;line-height:1.2;color:#0E0E0E">Checking once tells you about one day.</div>
{foot('ll', False, right=80, bottom=86)}
''')

# 18 Fri Dec 11, dark, phone photo
T['s-1211-photo-date'] = S(f'''
<div class="photo" style="inset:0;{ph('30332467','42% 50%','auto 100%')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(8,8,8,.86) 0%,rgba(8,8,8,.45) 30%,rgba(8,8,8,0) 50%,rgba(8,8,8,.7) 80%,rgba(8,8,8,.9) 100%)"></div>
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FAFAF8">Listing photos</div>
<div class="osw abs" style="left:78px;top:140px;width:920px;font-size:110px;line-height:1.0;font-weight:700;color:#FAFAF8">When were your photos taken?</div>
<div class="news it abs" style="left:80px;top:1100px;width:620px;font-size:40px;line-height:1.2;color:#FAFAF8">A renter can usually tell.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 19 Sat Dec 12, light, keys photo right
T['s-1212-tonight'] = S(f'''
<div class="photo" style="right:0;top:0;width:620px;height:1350px;{ph('29871187','38% 50%','auto 100%')}"></div>
<div class="mono red abs" style="left:60px;top:80px;font-size:22px">Saturday</div>
<div class="fra abs" style="left:60px;top:140px;width:370px;font-size:70px;line-height:1.04;font-weight:400;color:#0E0E0E;letter-spacing:-.02em">Can a renter book a tour <span class="it red">tonight?</span></div>
<div class="abs" style="left:60px;top:760px;width:340px;border-top:2px solid #0E0E0E"></div>
<div class="plex abs" style="left:60px;top:790px;width:350px;font-size:28px;line-height:1.4;color:#3A3631">Plenty of weekend searching happens after the office closes. The booking link can still work.</div>
{foot('sdm', False, left=60, bottom=70, h=96)}
''')

# 20 Sun Dec 13, dark, 2027 outline
T['s-1213-plan-2027'] = S(f'''
<div class="bsd abs" style="left:50px;top:20px;font-size:470px;line-height:.9;font-weight:900;color:transparent;-webkit-text-stroke:3px #D2321E">2027</div>
<div class="mono abs" style="left:80px;top:540px;font-size:24px;color:#FAFAF8">Planning</div>
<div class="fra abs" style="left:80px;top:600px;width:920px;font-size:90px;line-height:1.02;font-weight:400;color:#FAFAF8;letter-spacing:-.02em">Plan it around how renters <span class="it" style="color:#FF8A75">search now.</span></div>
<div class="abs" style="left:80px;top:930px;width:920px;display:flex;gap:24px">
{''.join(f'<div style="flex:1;border-top:3px solid #FAFAF8;padding-top:18px"><div class="bsd" style="font-size:30px;font-weight:800;color:#FF8A75">0{i+1}</div><div class="plex" style="font-size:32px;line-height:1.25;color:#FAFAF8;margin-top:8px">{t}</div></div>' for i,t in enumerate(['The social feed','Google Maps','AI answers']))}
</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# 21 Mon Dec 14, light, giant quote (Field Notes week 4 short)
T['s-1214-neighbor'] = S(f'''
<div class="pf abs" style="left:40px;top:-80px;font-size:620px;line-height:1;color:#D2321E">&ldquo;</div>
<div class="ex abs" style="right:80px;top:74px">Example review</div>
<div class="pf it abs" style="left:80px;top:360px;width:900px;font-size:76px;line-height:1.12;color:#0E0E0E">Maintenance fixed my sink the same afternoon.</div>
<div class="mono abs" style="left:80px;top:680px;font-size:22px;color:#5E5952">A resident, in a review</div>
<div class="abs" style="left:80px;top:780px;width:920px;border-top:3px solid #0E0E0E"></div>
<div class="osw abs" style="left:80px;top:810px;width:920px;font-size:64px;line-height:1.08;font-weight:600;color:#0E0E0E">A resident's word carries further than your own.</div>
<div class="plex abs" style="left:80px;top:1000px;width:640px;font-size:29px;line-height:1.38;color:#3A3631">AI tools may weigh it the same way a renter does.</div>
{foot('ll', False, right=80, bottom=86)}
''')

# 22 Tue Dec 15, dark, palms lit
T['s-1215-lit-up'] = S(f'''
<div class="photo" style="left:470px;top:0;width:610px;height:1350px;{ph('13894130','50% 30%')}"></div>
<div class="abs" style="left:470px;top:0;width:160px;height:1350px;background:linear-gradient(90deg,rgba(4,8,15,1) 0%,rgba(4,8,15,0) 100%)"></div>
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#FFD9A0">Holiday local</div>
<div class="news abs" style="left:80px;top:150px;width:440px;font-size:76px;line-height:1.04;color:#FAFAF8">The neighborhood is lit up. <span class="it" style="color:#FFD9A0">Is your feed?</span></div>
<div class="plex abs" style="left:80px;top:960px;width:390px;font-size:28px;line-height:1.4;color:#EDEAE4">Lights, markets and events near the community are posts renters stop for.</div>
{foot('sdm', True, left=80, bottom=70)}
''', bg='#04080F')

# 23 Wed Dec 16, light, tag
T['s-1216-end-date'] = S(f'''
<div class="mono red abs" style="left:80px;top:80px;font-size:24px">Year end specials</div>
<div class="pf abs" style="left:80px;top:140px;width:920px;font-size:88px;line-height:1.04;font-weight:500;color:#0E0E0E">A special needs an <span class="it red">end date.</span></div>
<div class="abs" style="left:250px;top:470px;width:600px;height:400px;background:#D2321E;transform:rotate(-6deg);clip-path:polygon(18% 0,100% 0,100% 100%,18% 100%,0 50%)">
 <div class="abs" style="left:52px;top:180px;width:40px;height:40px;border-radius:50%;background:#FAFAF8"></div>
 <div class="mono abs" style="left:170px;top:84px;font-size:28px;color:#FAFAF8">Offer ends</div>
 <div class="bsd abs" style="left:166px;top:128px;font-size:190px;line-height:.9;font-weight:900;color:#FAFAF8">12.31</div>
</div>
<div class="ex abs" style="left:80px;top:930px">Example</div>
<div class="plex abs" style="left:80px;top:1000px;width:660px;font-size:31px;line-height:1.35;color:#3A3631">Same wording and the same date everywhere a renter looks.</div>
{foot('sdm', False, right=80, bottom=70)}
''')

# 24 Thu Dec 17, dark, lobby
T['s-1217-listing-works'] = S(f'''
<div class="photo" style="inset:0;{ph('6758532','50% 50%','auto 100%')}"></div>
<div class="abs" style="inset:0;background:linear-gradient(180deg,rgba(10,10,10,.1) 25%,rgba(10,10,10,.92) 62%)"></div>
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#0E0E0E;background:rgba(250,250,248,.9);padding:8px 12px">Holiday break</div>
<div class="fra abs" style="left:80px;top:770px;width:920px;font-size:84px;line-height:1.02;font-weight:400;color:#FAFAF8;letter-spacing:-.02em">Your listing keeps working <span class="it" style="color:#FF8A75">through the holidays.</span></div>
<div class="plex abs" style="left:80px;top:1100px;width:620px;font-size:29px;line-height:1.38;color:#EDEAE4">Check that what it says is current before the office closes.</div>
{foot('sdm', True, right=80, bottom=70)}
''', bg='#0E0E0E')

# LinkedIn Dec 1 Field Notes, before and after
T['li-1201-before-after'] = S(f'''
<div class="mono abs" style="left:80px;top:80px;font-size:24px;color:#5E5952">Marketing language and clear language</div>
<div class="bsd abs" style="left:76px;top:150px;font-size:150px;line-height:.9;font-weight:300;color:#8A847B">Before</div>
<div class="news it abs" style="left:80px;top:300px;width:900px;font-size:58px;line-height:1.15;color:#5E5952">"A pet friendly community where everyone feels at home."</div>
<div class="abs" style="left:0;top:600px;width:1080px;height:750px;background:#0E0E0E"></div>
<div class="bsd abs" style="left:76px;top:650px;font-size:150px;line-height:.9;font-weight:900;color:#FAFAF8">After</div>
<div class="news abs" style="left:80px;top:800px;width:900px;font-size:62px;line-height:1.15;color:#FAFAF8">"Two dogs are welcome per home, with a 75 pound limit."</div>
<div class="ex abs" style="left:80px;top:1030px">Examples, not a real policy</div>
{foot('ll', True, right=80, bottom=86)}
''')

if __name__ == '__main__': asyncio.run(render(sys.argv[1:] or None))
