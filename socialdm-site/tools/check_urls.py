"""Fail the build if any known old URL (tools/known-urls.txt) has no page and no redirect in dist/."""
import os, sys
def check(out, known):
    rules = [l.split()[0] for l in open(os.path.join(out, '_redirects')) if l.strip() and not l.startswith('#')]
    missing = []
    for p in (l.strip() for l in open(known)):
        if not p or p.startswith('#'):
            continue
        q = p.rstrip('/') or '/'
        ok = (q == '/' or os.path.exists(out + q + '.html') or os.path.exists(out + q + '/index.html')
              or any(q == r or (r.endswith('*') and q.startswith(r[:-1])) for r in rules))
        if not ok:
            missing.append(p)
    return missing
if __name__ == '__main__':
    m = check(sys.argv[1], sys.argv[2]); print('\n'.join(m) or 'all known URLs resolve'); sys.exit(1 if m else 0)
