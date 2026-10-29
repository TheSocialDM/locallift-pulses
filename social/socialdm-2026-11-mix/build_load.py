#!/usr/bin/env python3
"""Turn plan.json + inventory.json into ready Metricool calls (load.json).
usage: build_load.py <commit>"""
import json, sys, copy, pathlib
COMMIT = sys.argv[1]
ROOT = pathlib.Path(__file__).resolve().parent
plan = json.load(open(ROOT/'plan.json'))
inv = {p['id']: p for p in json.load(open('/tmp/claude-0/-home-claude/8b559400-d684-57af-841a-a5642ccf2402/scratchpad/inventory.json'))}
BASE = f'https://raw.githubusercontent.com/TheSocialDM/locallift-pulses/{COMMIT}/'
PRE = {'S:': plan['S'], 'N:': plan['N']}
def url(m):
    for k, v in PRE.items():
        if m.startswith(k): return BASE + v + m[len(k):]
    raise ValueError(m)

NETMAP = {'instagram': 'instagram', 'facebook': 'facebook', 'linkedin': 'linkedin', 'gmb_post': 'gmb', 'gmb_photo': 'gmb'}
out = []
for x in plan['posts']:
    net = NETMAP[x['net']]
    media = [url(m) for m in x.get('media', [])]
    if x['action'] == 'create':
        info = {'autoPublish': True, 'draft': False, 'descendants': [], 'hasNotReadNotes': False, 'shortener': False,
                'smartLinkData': {'ids': []}, 'providers': [{'network': net}],
                'publicationDate': {'dateTime': f"{x['date']}T{x['time']}:00", 'timezone': 'America/Phoenix'},
                'text': '' if x['net'] == 'gmb_photo' else x['text'],
                'firstCommentText': x.get('first_comment', ''),
                'media': media, 'mediaAltText': [x.get('alt')] * len(media)}
        if net == 'instagram': info['instagramData'] = {'type': 'POST', 'autoPublish': True, 'showReelOnFeed': True, 'isAiGenerated': False}
        if net == 'facebook': info['facebookData'] = {'type': 'POST'}
        if net == 'linkedin': info['linkedinData'] = {'type': 'post', 'previewIncluded': False}
        if net == 'gmb': info['gmbData'] = {'type': 'publication' if x['net'] == 'gmb_post' else 'photo'}
        out.append({'tool': 'createScheduledPostForReview', 'date': f"{x['date']}T{x['time']}:00-07:00", 'label': f"{x['date']} {x['time']} {x['net']}", 'info': info})
        continue
    src = inv[x['id']]
    info = copy.deepcopy(src['raw'])
    for k in ('id', 'uuid', 'creationDate', 'providers', 'creatorUserMail', 'creatorUserId', 'postApprovalData', 'uuid'):
        pass
    keep = {}
    for k in ('autoPublish', 'draft', 'descendants', 'hasNotReadNotes', 'shortener', 'smartLinkData', 'publicationDate', 'text',
              'firstCommentText', 'media', 'mediaAltText', 'saveExternalMediaFiles', 'instagramData', 'facebookData',
              'linkedinData', 'gmbData', 'videoCoverMilliseconds'):
        if k in info: keep[k] = info[k]
    keep['providers'] = [{'network': p['network']} for p in info['providers']]
    keep.setdefault('descendants', []); keep.setdefault('smartLinkData', {'ids': []})
    if media:
        keep['media'] = media
        alts = x.get('alt_list') or [x.get('alt')] * len(media)
        old = src.get('mediaAltText') or []
        keep['mediaAltText'] = [a if a else (old[i] if i < len(old) else None) for i, a in enumerate(alts)]
    if x['action'] in ('edit', 'edit_move') and 'text' in x: keep['text'] = x['text']
    if x['action'] in ('edit', 'edit_move') and 'first_comment' in x: keep['firstCommentText'] = x['first_comment']
    if x.get('text_replace'):
        a, b = x['text_replace']; assert a in keep['text']; keep['text'] = keep['text'].replace(a, b)
    if x['action'] == 'edit_move':
        keep['publicationDate'] = {'dateTime': f"{x['new_date']}T{x['new_time']}:00", 'timezone': 'America/Phoenix'}
    if net == 'facebook': keep.pop('instagramData', None)
    if net == 'linkedin': keep.pop('instagramData', None)
    if net == 'gmb': keep.pop('instagramData', None)
    keep.pop('twitterData', None)
    out.append({'tool': 'sendScheduledPostForReview', 'id': str(src['id']), 'uuid': src['uuid'],
                'label': f"{x['date']} {x['time']} {x['net']} {x['action']}", 'info': keep})
json.dump(out, open(ROOT/'load.json', 'w'), indent=1, ensure_ascii=False)
print(len(out), 'calls;', sum(1 for o in out if o['tool'] == 'createScheduledPostForReview'), 'new')
