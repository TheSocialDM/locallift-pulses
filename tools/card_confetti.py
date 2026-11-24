import re,sys
p='live/montage-r8x2/v3/index.html';s=open(p).read()
# fresh window: first 21 days after the first time this phone used the card
fresh="const mcFresh=()=>{try{let d=+localStorage.getItem('ll-mc-day0');if(!d){d=Date.now();localStorage.setItem('ll-mc-day0',String(d))}return Date.now()-d<21*864e5}catch(x){return false}};\n"
a="const mcCard=()=>{"
assert s.count(a)==1
s=s.replace(a,fresh+a,1)
# confetti when the card opens
old="const mcCard=()=>{mcLog('Card opened');"
s=s.replace(old,"const mcCard=()=>{mcLog('Card opened');if(mcFresh())setTimeout(()=>mcConfetti(90),300);",1)
# confetti when they flip to see what prospects see
old2="const mcToggle=()=>{const f=document.getElementById('mcF');if(!f)return;const intro=f.dataset.a==='mia';const onA=f.dataset.side==='a';"
assert s.count(old2)==1
s=s.replace(old2,old2+"if(onA&&!intro&&mcFresh())setTimeout(()=>mcConfetti(70),420);",1)
# intro also starts the clock
s=s.replace("mcLog('Intro seen');","mcLog('Intro seen');mcFresh();",1)
s=re.sub(r"const APPV='[^']*'","const APPV='2026-11-24d'",s)
open(p,'w').write(s);open('live/montage-r8x2/v3/version.txt','w').write('2026-11-24d\n')
print('ok')
