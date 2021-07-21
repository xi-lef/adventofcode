from collections import Counter
import sys

lines = [l.strip() for l in sys.stdin]

n = len(lines[0])
counters = [Counter() for _ in range(n)]
for l in lines:
    for i, c in enumerate(l):
        counters[i].update(c)

print(''.join([c.most_common(1)[0][0] for c in counters]))
print(''.join([c.most_common()[-1][0] for c in counters]))
