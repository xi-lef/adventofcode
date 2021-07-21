from collections import Counter
import sys

lines = [l.strip() for l in sys.stdin]

c2 = c3 = 0
for l in lines:
    v = Counter(l).values()
    c2 += 2 in v
    c3 += 3 in v
print(c2 * c3)

for a in lines:
    for b in lines:
        if a == b:
            continue
        diff = 0
        for i, t in enumerate(zip(a, b)):
            if t[0] != t[1]:
                diff += 1
                pos = i

        if diff == 1:
            print(a[:pos] + a[pos + 1:])
            exit()
