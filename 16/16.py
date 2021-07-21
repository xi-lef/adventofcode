import sys
from more_itertools import grouper

init = sys.stdin.readline().strip()
zero = ord('0')
one = ord('1')

for disk in (272, 35651584):
    a = init
    while len(a) < disk:
        a += '0' + a[::-1].translate({zero: one, one: zero})
    a = a[:disk]

    while len(a) % 2 == 0:
        a = ''.join('1' if g[0] == g[1] else '0' for g in grouper(a, 2))
    print(a)
