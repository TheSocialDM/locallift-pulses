"""Make logo, icon, hero and shot files for a Pillar app from media/pillar-dec photos.
Usage: python3 tools/pillar_assets.py cuvee|elevation-santan"""
import sys,os,json
from PIL import Image,ImageDraw,ImageFont
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
K=sys.argv[1]
M='/usr/share/fonts/truetype/google-fonts/ofl/montserrat/Montserrat[wght].ttf'
C={'cuvee':dict(folder='cuvee-c6v2',word='CUVEE',mono='C',col=(123,35,64),dark=(70,18,31),src='media/pillar-dec/cuvee/cuvee-glendale-az-',
     hero='pool-spa-sunset',shots={'outside':'building-exterior','pool':'pool-spa-sunset','pooldusk':'pool-dusk','rooftop':'rooftop-fire-pit-sunset','gym':'fitness-center-free-weights','yoga':'yoga-spin-room','living':'living-room-leather-sofa','kitchen':'kitchen-counter-pendant','balcony':'balcony-chairs','office':'leasing-office-palms'}),
   'elevation-santan':dict(folder='elevation-santan-e3t8',word='ELEVATION SANTAN',mono='E',col=(43,95,135),dark=(19,47,69),src='media/pillar-dec/elevation-santan/elevation-san-tan-gilbert-az-',
     hero='entry-sign',shots={'outside':'entry-sign','lounge':'clubhouse-lounge','lobby':'lobby-lounge','gym':'fitness-center','kitchen':'gray-kitchen','pendant':'kitchen-pendant-lights','living':'living-room-white-sofa','petspa':'dog-wash','nook':'bedroom-desk-nook'})}[K]
D=os.path.join(R,'live',C['folder']);os.makedirs(D+'/shots',exist_ok=True)
def font(sz,w=700):
    f=ImageFont.truetype(M,sz)
    try:f.set_variation_by_axes([w])
    except Exception:pass
    return f
def wordmark(color,path):
    im=Image.new('RGBA',(720,140),(0,0,0,0));d=ImageDraw.Draw(im)
    sz=78 if len(C["word"])<8 else 44;f=font(sz,600)
    # letter spaced
    sp=sz*0.18;chars=C['word'];w=sum(d.textlength(ch,font=f) for ch in chars)+sp*(len(chars)-1)
    x=(720-w)/2
    for ch in chars:
        d.text((x,70),ch,font=f,fill=color,anchor='lm');x+=d.textlength(ch,font=f)+sp
    im.save(path)
wordmark((255,255,255,255),D+'/logo-white.png');wordmark(C['dark']+(255,),D+'/logo-umber.png')
for s in (180,192,512):
    im=Image.new('RGB',(s,s),C['col']);d=ImageDraw.Draw(im)
    d.text((s/2,s*0.47),C['mono'],font=font(int(s*0.58),600),fill=(255,255,255),anchor='mm')
    d.rectangle([s*0.34,s*0.80,s*0.66,s*0.82],fill=(255,255,255))
    im.save(D+f'/icon-{s}.png')
def crop(src,dst,w,h):
    im=Image.open(src).convert('RGB');r=max(w/im.width,h/im.height);im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
    x=(im.width-w)//2;y=(im.height-h)//2;im.crop((x,y,x+w,y+h)).save(dst,quality=84)
crop(R+'/'+C['src']+C['hero']+'.jpg',D+'/hero.jpg',1400,933) if Image.open(R+'/'+C['src']+C['hero']+'.jpg').width>=1100 else Image.open(R+'/'+C['src']+C['hero']+'.jpg').convert('RGB').save(D+'/hero.jpg',quality=86)
for k,v in C['shots'].items():
    im=Image.open(R+'/'+C['src']+v+'.jpg').convert('RGB');im.thumbnail((1000,1000));im.save(D+f'/shots/{k}.jpg',quality=82)
print('assets',K,sorted(os.listdir(D)))
