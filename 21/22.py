import re
from more_itertools import grouper

steps = []
for l in open(0):
    act, coords = l.split()
    xl, xh, yl, yh, zl, zh = map(int, re.findall(r'-?\d+', coords))
    assert xl <= xh and yl <= yh and zl <= zh
    steps.append((act == 'on', [xl, xh, yl, yh, zl, zh]))

def mc(al, ah, bl, bh):
    return al <= bh and ah >= bl

def process(steps):
    on = []
    for o, c in steps:
        xl, xh, yl, yh, zl, zh = c
        rm = []
        for oc in on:
            oxl, oxh, oyl, oyh, ozl, ozh = oc
            #if ((oxl <= xl <= oxh or oxl <= xh <= oxh)
            #        and (oyl <= yl <= oyh or oyl <= yh <= oyh)
            #        and (ozl <= zl <= ozh or ozl <= zh <= ozh)
            #    or (xl <= oxl <= xh or xl <= oxh <= xh)
            #        and (yl <= oyl <= yh or yl <= oyh <= yh)
            #        and (zl <= ozl <= zh or zl <= ozh <= zh) ):
            if (mc(xl, xh, oxl, oxh) and mc(yl, yh, oyl, oyh) and mc(zl, zh, ozl, ozh)):
                rm.append(oc)
                new = [[oxl, oxh, oyl, oyh, ozl, zl - 1],  # below
                       [oxl, oxh, oyl, oyh, zh + 1, ozh],  # above
                       [oxl, xl - 1, oyl, oyh, max(zl, ozl), min(zh, ozh)],  # left
                       [xh + 1, oxh, oyl, oyh, max(zl, ozl), min(zh, ozh)],  # right
                       [max(xl, oxl), min(xh, oxh), oyl, yl - 1, max(zl, ozl), min(zh, ozh)],  # front
                       [max(xl, oxl), min(xh, oxh), yh + 1, oyh, max(zl, ozl), min(zh, ozh)]]  # back
                on.extend(n for n in new if all(a <= b for a, b in grouper(n, 2)))
        for r in rm:
            on.remove(r)
        if o:
            on.append(c)
    return on

def count(ranges):
    total = 0
    for xl, xh, yl, yh, zl, zh in ranges:
        total += (xh - xl + 1) * (yh - yl + 1) * (zh - zl + 1)
    return total

print(count(process(steps[: 20])))
print(count(process(steps)))
