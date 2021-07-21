from collections import Counter
import string
import sys

valid = []
count = 0
for l in sys.stdin:
    l = l.strip()
    name = l[:-10]
    id = int(l[-10:-7])
    chk = l[-6:-1]

    c = Counter(name.replace('-', ''))
    bla = sorted([(-n, c) for c, n in c.most_common()])
    if ''.join(c for _, c in bla).startswith(chk):
        count += id
        valid.append((name, id, chk))
print(count)

for name, id, _ in valid:
    orig = ''
    for c in name:
        if c == '-':
            orig += ' '
            continue
        lc = string.ascii_lowercase
        orig += lc[(lc.index(c) + id) % len(lc)]
    if 'northpole' in orig:
        print(orig, id)
