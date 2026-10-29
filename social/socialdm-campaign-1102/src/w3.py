from base import *

# Swiss editorial direction: typography as the artwork. Two original concepts.

# X1 SDM, type only. "Seen is not chosen."
T['x-swiss-seen-chosen'] = S(f"""
<div style="position:absolute;left:0;top:0;width:330px;height:1350px;background:#D2321E"></div>
<div class="mono" style="position:absolute;left:44px;top:80px;font-size:22px;color:#FAFAF8;line-height:1.5">AI search<br>Local search<br>Social</div>
<div class="anton" style="position:absolute;left:250px;top:120px;font-size:330px;line-height:.8;color:#0E0E0E;letter-spacing:-.01em">SEEN</div>
<div class="arch" style="position:absolute;left:372px;top:410px;font-size:44px;font-weight:700;color:#D2321E;letter-spacing:.02em;text-transform:uppercase">is not the same as</div>
<div class="anton" style="position:absolute;left:96px;top:480px;font-size:400px;line-height:.8;color:transparent;-webkit-text-stroke:4px #0E0E0E;letter-spacing:-.015em">CHO</div>
<div class="anton" style="position:absolute;left:96px;top:800px;font-size:400px;line-height:.8;color:#0E0E0E;letter-spacing:-.015em">SEN.</div>
<div style="position:absolute;left:372px;top:1150px;width:420px;font-size:27px;line-height:1.35;color:#0E0E0E">Showing up gets you looked at. Clear, consistent details get you picked.</div>
<div style="position:absolute;left:820px;top:1150px;width:180px;height:6px;background:#0E0E0E"></div>
<div style="position:absolute;right:80px;bottom:80px"><img src="{LG}socialdm-color.png" style="height:100px;display:block"></div>
<div class="mono" style="position:absolute;left:44px;bottom:80px;font-size:22px;color:#FAFAF8;writing-mode:vertical-rl;transform:rotate(180deg)">The SocialDM · No. 01</div>
""")

# X2 LocalLift, type plus cinematic photo. "Local. Then loud."
T['x-swiss-local-loud'] = S(f"""
<div class="photo" style="left:540px;top:0;width:540px;height:880px;{ph('12906296','50% 40%')};filter:grayscale(1) contrast(1.1)"></div>
<div style="position:absolute;left:540px;top:0;width:540px;height:880px;background:#D2321E;mix-blend-mode:multiply"></div><div style="position:absolute;left:540px;top:520px;width:540px;height:360px;background:linear-gradient(180deg,rgba(14,14,14,0),rgba(14,14,14,.6))"></div>
<div style="position:absolute;left:0;top:880px;width:1080px;height:470px;background:#0E0E0E"></div>
<div class="mono red" style="position:absolute;left:80px;top:80px;font-size:24px">Local search</div>
<div class="bsd" style="position:absolute;left:60px;top:170px;font-size:212px;line-height:.82;font-weight:900;color:#0E0E0E;text-transform:uppercase;letter-spacing:-.01em">Local</div>
<div class="bsd" style="position:absolute;left:66px;top:390px;font-size:120px;line-height:.9;font-weight:300;color:#0E0E0E;text-transform:uppercase">beats<br>generic.</div>
<div class="mono" style="position:absolute;left:1000px;top:520px;font-size:22px;color:#FAFAF8;writing-mode:vertical-rl">Search · Maps · AI</div>
<div style="position:absolute;left:80px;top:700px;width:150px;height:150px;background:#D2321E"></div>
<div class="fra" style="position:absolute;left:80px;right:80px;top:940px;font-size:62px;line-height:1.04;font-weight:300;color:#FAFAF8;letter-spacing:-.02em">Renters search the neighborhood, not just the brand.</div>
{foot('ll', True, right='THESOCIALDM.COM/LOCALLIFT')}
""")

if __name__ == '__main__':
    asyncio.run(render(sys.argv[1:] or None))
