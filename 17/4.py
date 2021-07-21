from collections import Counter
from itertools import permutations
import sys

lines = [l.strip() for l in sys.stdin]

c1 = c2 = 0
for l in lines:
    words = l.split()
    counter = Counter(words)
    c1 += max(counter.values()) == 1

    perms = [''.join(p) for w in words for p in set(permutations(w)) if ''.join(p) != w]
    #print(perms)
    counter.update(perms)
    #print(counter)
    c2 += max(counter.values()) == 1
print(c1, c2)
