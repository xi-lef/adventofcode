from functools import cmp_to_key
from itertools import zip_longest

GOOD, IDK, BAD = -1, 0, 1

def check(a, b):
    #print(f'checking {a} vs {b}')
    if a is None:
        return GOOD if b is not None else IDK
    elif b is None:
        return BAD

    aint = isinstance(a, int)
    bint = isinstance(b, int)
    if aint + bint == 1:
        if aint: a = [a]
        if bint: b = [b]

    if aint + bint == 2:
        d = a - b
        if d == 0: return IDK
        if d < 0: return GOOD
        if d > 0: return BAD

    for x, y in zip_longest(a, b, fillvalue = None):
        c = check(x, y)
        if c != IDK:
            return c

    return IDK

sum = 0
pairs = [eval(p.replace('\n', ',')) for p in open(0).read().split('\n\n')]
for i, pair in enumerate(pairs, 1):
    #print('pair', i)
    a, b = pair
    if c := check(a, b) == GOOD:
        sum += i
    #print({BAD: 'BAD', GOOD: 'GOOD', IDK: 'IDK'}[c])
print(sum)

div1, div2 = [[2]], [[6]]
pairs = [x for p in pairs for x in p]
pairs.extend((div1, div2))
pairs.sort(key = cmp_to_key(check))
print((pairs.index(div1) + 1) * (pairs.index(div2) + 1))
