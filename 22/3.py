from string import ascii_letters
from more_itertools import grouper

lines = [l.strip() for l in open(0)]

#print(sum(ascii_letters.index(set(l[: len(l) // 2]).intersection(set(l[len (l) // 2 :])).pop()) + 1 for l in lines))
s = 0
for l in lines:
    half = len(l) // 2
    a, b = set(l[: half]), set(l[half :])
    item = a.intersection(b).pop()
    s += ascii_letters.index(item) + 1
print(s)

s2 = 0
for g in grouper(lines, 3):
    g = [set(r) for r in g]
    item = g[0].intersection(g[1]).intersection(g[2]).pop()
    s2 += ascii_letters.index(item) + 1
print(s2)
