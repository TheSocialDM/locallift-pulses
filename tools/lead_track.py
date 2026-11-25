"""LocalLift lead tracking standard (Nov 24 2026), idempotent. One GA4 scheme for every LocalLift Live property.
  Agent pages (team/<prop>/leasing/ and card/): loads guide/lltrack.js, which fires
      lead_action {property, staff, action, src, place}
  Staff app (live/<app>/v3/): adds <script id="llappact">, which fires
      app_action {property, staff, action, detail}
  Old events (tab_*, card_*, tour_start, heard_from, review_link_open, call_tap, tour_click, apply_click ...) are untouched.
  No prospect names, phones or emails go to analytics. No per tap Make pings.
Usage:
  python3 tools/lead_track.py                 every agent page, card and staff app listed in live/apps.json
  python3 tools/lead_track.py agent <file> <prop>
  python3 tools/lead_track.py app <live/<app>/v3/index.html>
The build_*_leasing.py scripts call agent_file() on what they write, and tools/app_ui_fix_nov24.py calls app()."""
import re,os,sys,json
R=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
LTV='1'
def slug(prop):
    return {'stillwater lakes':'stillwater'}.get(prop.lower(),prop.lower())

def agent(s,prop):
    """Add (or refresh) the lltrack.js tag on an agent page or card page."""
    s=re.sub(r'\n?<script src="[./]*guide/lltrack\.js[^"]*"[^>]*></script>','',s)
    m=re.search(r'<script src="((?:\.\./)+)guide/guide\.js',s)
    pre=m.group(1) if m else '../../../'
    tag=f'<script src="{pre}guide/lltrack.js?v={LTV}" data-llprop="{slug(prop)}" defer></script>'
    i=s.rfind('</body>');assert i>0
    return s[:i]+tag+'\n'+s[i:]

def agent_file(path,prop):
    s=open(path).read();n=agent(s,prop)
    if n!=s: open(path,'w').write(n)
    return n!=s

APP_JS=r'''<script id="llappact">
/* LocalLift lead tracking standard: one app_action event per staff lead tap (property, staff, action, detail).
   No resident or prospect details are sent. Events use transport beacon so they survive the jump to Messages or Mail. */
(function(){if(window.__llAA)return;window.__llAA=1;var P='__PROP__',ME='__PRE__-me',mom='';
if(/\/demo\//.test(location.pathname))return;
var who=function(){var n='';try{n=localStorage.getItem(ME)||''}catch(e){}n=n.replace(/[^A-Za-z .'-]/g,'').trim().split(' ')[0].slice(0,20);return n||'unknown'};
var A=function(a,d){try{if(typeof gtag==='function')gtag('event','app_action',{property:P,staff:who(),action:a,detail:d||'',transport_type:'beacon'})}catch(x){}};
window.llAppAction=A;
var ID={bTour:['tour_start','button'],bTour2:['tour_start','today'],mcTour:['tour_start','dock'],tFin:['tour_finish',''],mcBtn:['card_open','dock'],
 dSend:['send_day','email'],dCopy:['send_day','copy'],dShare:['send_day','share'],bCap:['snap_open','']};
document.addEventListener('click',function(e){try{var t=e.target;if(!t||!t.closest)return;
 var m=t.closest('[data-mc]');if(m){var k=m.getAttribute('data-mc');
  if(k==='sent'){var kk=m.getAttribute('data-k')||'';if(kk==='text'||kk==='email'||kk==='share')A(kk,'my_card');return}
  if(k==='page'){A('my_page','my_card');return}
  if(k==='open'&&!t.closest('#box')){A('card_open','card');return}
  return}
 var r=t.closest('button[data-m]');if(r){mom=r.getAttribute('data-m')||'any';A('review_ask',mom);return}
 var a=t.closest('a[href]');if(a){var hh=(a.getAttribute('href')||'').toLowerCase();
  if(/^tel:/.test(hh)){A('call','link');return}if(/^sms:/.test(hh)){A('text','link');return}}
 var b=t.closest('[id]');if(!b)return;var id=b.id;
 if(id==='qr'){A('review_qr',mom||'any');return}
 if(id==='snapSend'||id==='snapVid'){if(!b.disabled)A('snap_upload',id==='snapVid'?'video':'photo');return}
 if(ID[id])A(ID[id][0],ID[id][1]);
}catch(x){}},true);
})();
</script>'''

def app(s):
    """Add (or refresh) the app_action block in a staff app (v3) page."""
    pre=re.search(r"const K='([a-z]+)-team'",s).group(1)
    prop=re.search(r"\{app:'live_([a-z]+)'\}",s).group(1)
    js=APP_JS.replace('__PROP__',prop).replace('__PRE__',pre)
    s=re.sub(r'<script id="llappact">.*?</script>',lambda m:js,s,count=1,flags=re.S) if 'id="llappact"' in s else s.replace('</head>',js+'</head>',1)
    return s

def all_pages():
    A=json.load(open(os.path.join(R,'live/apps.json')))['apps']
    for a in A:
        p=slug(a['property'])
        for f in [f'team/{p}/leasing/index.html',f'team/{p}/leasing/card/index.html']:
            fp=os.path.join(R,f)
            if os.path.exists(fp): print(f,'changed' if agent_file(fp,a['property']) else 'unchanged')
        fp=os.path.join(R,a['folder'],'v3/index.html')
        s=open(fp).read();n=app(s)
        if n!=s: open(fp,'w').write(n)
        print(a['folder']+'/v3','changed' if n!=s else 'unchanged')

if __name__=='__main__':
    if len(sys.argv)==1: all_pages()
    elif sys.argv[1]=='agent': print(agent_file(sys.argv[2],sys.argv[3]))
    elif sys.argv[1]=='app':
        s=open(sys.argv[2]).read();n=app(s);open(sys.argv[2],'w').write(n);print('changed' if n!=s else 'unchanged')
