import sys,json
sys.path.insert(0,'.'); import content as c
SHA='91634ef8e1d5f23a4770741ba1fc59e6fd68a686'
m=json.load(open('files.json'))
U=lambda n:f'https://raw.githubusercontent.com/TheSocialDM/locallift-pulses/{SHA}/media/socialdm-dec/{n}'
TZ='America/Phoenix'
posts=[]
def add(key,date,time,net,text,media=None,alt=None,fc=None,gtype=None):
    info={"text":text,"providers":[{"network":net}],"autoPublish":True,"draft":False,"shortener":False,
          "publicationDate":{"dateTime":f"{date}T{time}:00","timezone":TZ}}
    if media: info["media"]=[media]; info["mediaAltText"]=[alt] if alt else [None]
    if fc: info["firstCommentText"]=fc
    if net=='instagram': info["instagramData"]={"type":"POST","autoPublish":True}
    if net=='facebook': info["facebookData"]={"type":"POST"}
    if net=='linkedin': info["linkedinData"]={"type":"POST","previewIncluded":False}
    if net=='gmb': info["gmbData"]={"type":gtype}
    posts.append(dict(key=key,date=f"{date}T{time}:00-07:00",net=net,info=info,photo=media,alt=alt,first=text.split('\n')[0] if text else '(photo item)'))
for p in c.SOCIAL:
    u=U(m[p['img']])
    add(f"ig-{p['date']}",p['date'],'11:15','instagram',p['ig'],u,p['alt'])
    add(f"fb-{p['date']}",p['date'],'11:15','facebook',p['fb'],u,p['alt'],p['fbc'])
for p in c.LI:
    med=U(m[p['img']]) if p.get('img') else None
    add(f"li-{p['date']}",p['date'],p['time'],'linkedin',p['text'],med,p.get('alt'),p['fc'])
for g in c.G:
    add(f"gp-{g['date']}",g['date'],'07:00','gmb',g['text'],U(m[g['date']+'pub']),g['alt'],gtype='publication')
    add(f"gi-{g['date']}",g['date'],'07:05','gmb','',U(m[g['date']+'item']),g['ialt'],gtype='photo')
posts.sort(key=lambda x:(x['date'],x['net']))
json.dump(posts,open('drafts.json','w'),indent=1)
print(len(posts))
