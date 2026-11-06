from base import *

# Mon Nov 16: market read, data style table on black
rows=[('Nearby A','No change','Quiet week',False),('Nearby B','Special added on one floor plan','May point to one slow floor plan',False),('Nearby C','Offer raised, second week in a row','May be behind on leasing goals',True),('Nearby D','Offer shrank','Demand may be catching up',False)]
trs=''.join(f"""<div style="display:grid;grid-template-columns:146px 520px 1fr;column-gap:12px;align-items:baseline;border-top:1.5px solid {'#D2321E' if hot else 'rgba(255,255,255,.28)'};padding:19px 0 20px">
<div class="mono" style="font-size:24px;letter-spacing:.04em;color:{'#FF8A75' if hot else '#CFCAC1'}">{a}</div>
<div class="news" style="font-size:34px;line-height:1.1;color:#FAFAF8;font-weight:{500 if hot else 400}">{b}</div><div class="arch" style="font-size:28px;line-height:1.15;color:#CFCAC1;font-weight:500">{c}</div></div>""" for a,b,c,hot in rows)
T['g-1116-specials-talk']=G(f"""
<div class="mono" style="position:absolute;left:64px;top:56px;font-size:24px;color:#FF8A75">Market read</div>
<div style="position:absolute;right:64px;top:50px"><span class="ex">Illustrative</span></div>
<div class="bsd" style="position:absolute;left:62px;top:104px;font-size:136px;line-height:.92;font-weight:900;color:#FAFAF8;text-transform:uppercase">Every special<br>says something.</div>
<div style="position:absolute;left:64px;right:64px;top:374px">{trs}<div style="border-top:1.5px solid rgba(255,255,255,.28)"></div></div>
<div class="mono" style="position:absolute;right:64px;bottom:64px;font-size:22px;color:#FAFAF8">What changed this week</div>
{foot('sdm',True,right='',left=64,rightpx=700,bottom=34,scale=1.0)}
""",bg='#0E0E0E')

# Tue Nov 17: holiday hours poster on red, dark band holds the logo
T['g-1117-holiday-hours']=G(f'''
<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:#0E0E0E"></div>
<div class="mono" style="position:absolute;left:64px;top:60px;font-size:24px;color:#FAFAF8">Holiday hours</div>
<div class="bod" style="position:absolute;right:64px;top:132px;font-size:490px;line-height:1;font-weight:600;color:#0E0E0E;letter-spacing:-.04em">26</div>
<div class="mono" style="position:absolute;right:66px;top:60px;font-size:24px;color:#0E0E0E">Thursday, Nov. 26</div>
<div class="anton" style="position:absolute;left:58px;top:170px;font-size:118px;line-height:1;color:#FAFAF8;width:600px">Closed Thursday?</div>
<div class="fra" style="position:absolute;left:64px;top:436px;font-size:56px;line-height:1.08;color:#FAFAF8;width:470px;font-weight:400">Tell Google before a renter finds out.</div>
{foot('ll',True,right='',left=64,rightpx=64,bottom=44)}
<div class="news" style="position:absolute;right:64px;bottom:50px;font-size:32px;color:#FAFAF8">Set special hours ahead of the holiday.</div>
''',bg='#D2321E')

# Wed Nov 18: wide photo over a run of five words
words=['Location','Price','Concessions','Amenities','Lifestyle']
T['g-1118-decide']=G(f'''
<div class="photo" style="left:0;top:0;width:1200px;height:470px;{ph('4680238','50% 44%','100% auto')}"></div>
<div class="mono red" style="position:absolute;left:64px;top:500px;font-size:24px">Social that helps</div>
<div class="fra" style="position:absolute;left:64px;top:542px;font-size:64px;line-height:1.05;font-weight:400;color:#0E0E0E;letter-spacing:-.015em">Is your feed helping her decide?</div>
<div class="arch" style="position:absolute;left:64px;right:64px;top:636px;font-size:42px;line-height:1.1;font-weight:700;color:#0E0E0E;text-transform:uppercase;display:flex;justify-content:space-between">{''.join(f'<span>{w}</span>' for w in words)}</div>
<div style="position:absolute;left:64px;right:64px;top:700px;border-top:2px solid #0E0E0E"></div>
{foot('sdm',False,right='',left=64,rightpx=700,bottom=26,scale=1.05)}
<div class="news it" style="position:absolute;right:64px;bottom:46px;font-size:32px;color:#3A3631">Five things renters tend to weigh.</div>
''',bg='#FAFAF8')

# Thu Nov 19: cinematic facade, struck word poster
T['g-1119-last-january']=G(f'''
<div class="photo" style="inset:0;{ph('17411447','50% 38%','100% auto')}"></div>
<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(8,12,10,.92) 0%,rgba(8,12,10,.86) 62%,rgba(8,12,10,.3) 92%)"></div>
<div class="mono" style="position:absolute;left:64px;top:64px;font-size:24px;color:#FAFAF8">Winter leasing</div>
<div class="news" style="position:absolute;left:64px;top:128px;font-size:54px;line-height:1.1;color:#FAFAF8;width:760px">Judge this January against</div>
<div class="bod" style="position:absolute;left:64px;top:196px;font-size:138px;line-height:1.08;color:#CFCAC1;font-weight:500">August<span style="position:absolute;left:0;right:-6px;top:56%;height:9px;background:#D2321E;display:block"></span></div>
<div class="bod" style="position:absolute;left:64px;top:362px;font-size:138px;line-height:1.08;color:#FAFAF8;font-weight:500;white-space:nowrap">Last January</div>
<div class="news it" style="position:absolute;left:64px;top:560px;font-size:38px;line-height:1.2;color:#FAFAF8;width:640px">Slower months read differently when you compare them to your own last winter.</div>
{foot('ll',True,right='',left=64,rightpx=64,bottom=56)}
''',bg='#0E0E0E')

if __name__=='__main__': asyncio.run(render(sys.argv[1:] or None))
