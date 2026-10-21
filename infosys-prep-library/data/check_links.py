#!/usr/bin/env python3
"""Resolve every external URL in the library with a browser user agent (some hosts 403 automation).
    python3 data/check_links.py [--only-new]   -> prints status per URL; writes data/links-checked.json
"""
import concurrent.futures as cf, json, pathlib, re, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
urls = {}
for f in ROOT.rglob('*.md'):
    if 'data' in f.relative_to(ROOT).parts or f.name in ('04-qa-report.md', '02-online-research-log.md'): continue
    for u in re.findall(r'https?://[^\s)`>\]"”]+', f.read_text()):
        u = u.rstrip('.,;*')
        urls.setdefault(u, set()).add(str(f.relative_to(ROOT)))

def check(u):
    r = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '-L', '-m', '25', '-A', UA, '-H', 'Accept-Language: en', u], capture_output=True, text=True)
    st = r.stdout.strip() or 'ERR'
    if st == '000':        # curl could not complete TLS. Retry without verification only to tell a bad host from an incomplete certificate chain
        r2 = subprocess.run(['curl', '-s', '-k', '-o', '/dev/null', '-w', '%{http_code}', '-L', '-m', '25', '-A', UA, u], capture_output=True, text=True)
        if r2.stdout.strip().startswith(('2', '3')):
            return u, r2.stdout.strip() + ' (incomplete certificate chain)'
    return u, st

with cf.ThreadPoolExecutor(8) as ex:
    res = dict(ex.map(check, sorted(urls)))
json.dump({u: {'status': s, 'files': sorted(urls[u])} for u, s in res.items()}, open(ROOT / 'data' / 'links-checked.json', 'w'), indent=1)
ok = [u for u, s in res.items() if s.startswith(('2', '3'))]
print(f"{len(urls)} URLs: {len(ok)} resolve")
for u, s in sorted(res.items()):
    if not s.startswith(('2', '3')):
        print(s, u, '<-', ', '.join(sorted(urls[u]))[:90])
