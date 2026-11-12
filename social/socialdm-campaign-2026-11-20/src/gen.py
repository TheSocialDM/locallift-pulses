from base import *

# Fri Nov 20: reviews, split with portrait photo right
T['g-1120-every-reply'] = G(f'''
<div class="photo" style="right:0;top:0;width:500px;height:900px;{ph('balcony','22% 40%')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:64px;font-size:24px">Reviews</div>
<div class="fra" style="position:absolute;left:64px;top:118px;width:590px;font-size:76px;line-height:1.02;font-weight:400;color:#0E0E0E;letter-spacing:-.02em">Every reply is read by the <span class="it red">next</span> renter.</div>
<div style="position:absolute;left:64px;top:470px;width:590px">
 <div style="border-top:2px solid #0E0E0E;padding:16px 0 18px" class="news"><span class="mono" style="font-size:20px;color:#6B665E">01</span>&nbsp;&nbsp;<span style="font-size:32px">Five stars, no words? Still reply.</span></div>
 <div style="border-top:1px solid #DAD6CE;padding:16px 0 18px" class="news"><span class="mono" style="font-size:20px;color:#6B665E">02</span>&nbsp;&nbsp;<span style="font-size:32px">A complaint? Answer it, calmly.</span></div>
 <div style="border-top:1px solid #DAD6CE;border-bottom:1px solid #DAD6CE;padding:16px 0 18px" class="news"><span class="mono" style="font-size:20px;color:#6B665E">03</span>&nbsp;&nbsp;<span style="font-size:32px">Never confirm who lives there.</span></div>
</div>
{foot('sdm', False, right='', left=64, rightpx=560, bottom=40, scale=0.95)}
''', bg='#FAFAF8')

# Sat Nov 21: approved Swiss concept "Seen is not chosen", adapted to the Google format
T['g-1121-seen-chosen'] = G(f'''
<div style="position:absolute;left:0;top:0;width:330px;height:900px;background:#D2321E"></div>
<div class="mono" style="position:absolute;left:36px;top:56px;font-size:19px;line-height:1.6;color:#FAFAF8">AI search<br>Local search<br>Social</div>
<div class="anton" style="position:absolute;left:250px;top:40px;font-size:250px;line-height:.9;color:#0E0E0E">Seen</div>
<div class="osw" style="position:absolute;left:350px;top:282px;font-size:42px;color:#D2321E;font-weight:700">is not the same as</div>
<div class="anton" style="position:absolute;left:250px;top:350px;font-size:250px;line-height:.9;color:transparent;-webkit-text-stroke:3px #0E0E0E">Cho</div>
<div class="anton" style="position:absolute;left:250px;top:572px;font-size:250px;line-height:.9;color:#0E0E0E">sen.</div>
<div style="position:absolute;right:64px;top:560px;width:380px;border-top:4px solid #0E0E0E"></div>
<div class="sans" style="position:absolute;right:64px;top:582px;width:380px;font-size:33px;line-height:1.3;color:#0E0E0E">Showing up gets you looked at. Clear, consistent details get you picked.</div>
<div style="position:absolute;right:64px;bottom:44px"><img src="{LG}socialdm-color.png" style="height:96px;display:block"></div>
''', bg='#FAFAF8')

# Sun Nov 22: holiday social, cinematic table photo
T['g-1122-holiday-useful'] = G(f'''
<div class="photo" style="inset:0;{ph('coffee','100% 50%','135% auto')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,9,8,.93) 0%,rgba(10,9,8,.84) 52%,rgba(10,9,8,.15) 88%)"></div>
<div class="mono" style="position:absolute;left:64px;top:64px;font-size:24px;color:#FF8A75">Holiday social</div>
<div class="bod" style="position:absolute;left:64px;top:120px;width:700px;font-size:96px;line-height:1.0;color:#FAFAF8">Make the holiday post <span class="it">useful.</span></div>
<div class="news it" style="position:absolute;left:64px;top:470px;width:640px;font-size:34px;line-height:1.25;color:#EDEDED">A resident event. A market nearby.<br>The office hours that change this week.</div>
{foot('sdm', True, right='', left=64, rightpx=700, bottom=40, scale=0.95)}
''', bg='#0E0E0E')

# Mon Nov 23: 2027 planning, editorial split
rows = [('Cost per lease, by source'), ('Tours booked'), ('Searches without your name')]
T['g-1123-budget-lines'] = G(f'''
<div class="photo" style="left:0;top:0;width:470px;height:900px;{ph('notebook','28% 4%','auto 150%')}"></div>
<div class="mono red" style="position:absolute;left:530px;top:64px;font-size:24px">2027 planning</div>
<div class="bsd" style="position:absolute;left:528px;top:110px;font-size:84px;line-height:.95;font-weight:900;text-transform:uppercase;color:#0E0E0E">Before the<br>2027 budget,</div>
<div class="fra it" style="position:absolute;left:530px;top:290px;width:600px;font-size:60px;line-height:1.05;color:#0E0E0E">ask what each line produced.</div>
<div style="position:absolute;left:530px;right:64px;top:470px">{''.join(f'<div style="border-top:{"2px solid #0E0E0E" if i==0 else "1px solid #DAD6CE"};padding:15px 0 16px;display:flex;gap:18px;align-items:baseline"><span class="mono" style="font-size:20px;color:#D2321E">0{i+1}</span><span class="news" style="font-size:31px">{r}</span></div>' for i,r in enumerate(rows))}<div style="border-top:1px solid #DAD6CE"></div></div>
{foot('sdm', False, right='', left=530, rightpx=64, bottom=40, scale=0.95)}
''', bg='#FAFAF8')

# Tue Nov 24: Google profile and AI, cinematic architecture
T['g-1124-profile-first'] = G(f'''
<div class="photo" style="inset:0;{ph('towers','50% 40%')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,10,14,.94) 0%,rgba(8,10,14,.86) 55%,rgba(8,10,14,.2) 92%)"></div>
<div class="mono" style="position:absolute;left:64px;top:64px;font-size:24px;color:#FAFAF8">AI search</div>
<div class="news" style="position:absolute;left:64px;top:122px;width:720px;font-size:50px;line-height:1.1;color:#CFCAC1">Before it reads your website,</div>
<div class="bod" style="position:absolute;left:64px;top:190px;width:600px;font-size:96px;line-height:1.0;color:#FAFAF8">AI often reads your <span class="it" style="color:#FF8A75">Google profile.</span></div>
<div class="news it" style="position:absolute;left:64px;top:590px;width:620px;font-size:34px;line-height:1.25;color:#FAFAF8">Hours, categories, photos and reviews travel further than they used to.</div>
{foot('ll', True, right='', left=64, rightpx=64, bottom=56)}
''', bg='#0E0E0E')

# Wed Nov 25: move in day, photo band over white
T['g-1125-move-in'] = G(f'''
<div class="photo" style="left:0;top:0;width:1200px;height:430px;{ph('moving','50% 12%')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:462px;font-size:24px">Residents</div>
<div class="anton" style="position:absolute;left:60px;top:500px;width:760px;font-size:100px;line-height:.95;color:#0E0E0E">Move in day<br>is marketing.</div>
<div class="news it" style="position:absolute;left:64px;top:708px;width:640px;font-size:34px;line-height:1.2;color:#3A3631">The first week shapes how a resident talks about home.</div>
<div style="position:absolute;right:64px;bottom:40px"><img src="{LG}socialdm-color.png" style="height:100px;display:block"></div>
''', bg='#FAFAF8')

# Thu Nov 26: Thanksgiving, warm editorial
T['g-1126-thanksgiving'] = G(f'''
<div class="photo" style="left:0;top:0;width:440px;height:900px;{ph('harvest','50% 40%')}"></div>
<div class="mono red" style="position:absolute;left:510px;top:64px;font-size:24px">Thanksgiving, Nov. 26</div>
<div class="fra" style="position:absolute;left:508px;top:130px;width:630px;font-size:74px;line-height:1.04;font-weight:400;color:#0E0E0E;letter-spacing:-.02em">Grateful for the teams who make a building feel like <span class="it red">home.</span></div>
<div class="news it" style="position:absolute;left:510px;top:520px;width:640px;font-size:32px;line-height:1.3;color:#3A3631">Leasing teams, maintenance crews and residents.<br>Happy Thanksgiving from all of us.</div>
{foot('sdm', False, right='', left=510, rightpx=64, bottom=40, scale=0.95)}
''', bg='#E8E4DC')

if __name__ == '__main__': asyncio.run(render(sys.argv[1:] or None))
