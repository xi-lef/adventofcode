from itertools import cycle
import sys

l = [int(x.strip()) for x in sys.stdin.readlines()]

print(sum(l))

v = 0
x = set()
for c in cycle(l):
    v += c
    if v in x:
        print(v)
        break
    x.add(v)
