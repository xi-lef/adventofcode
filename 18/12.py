import sys

initial = sys.stdin.readline().strip().split(': ')[1]
sys.stdin.readline()
rules = {l: r for l in sys.stdin for l, r in [l.strip().split(' => ')]}

def count(pots, offset):
    c = 0
    for i, x in enumerate(pots):
        if x == '#':
            c += i - offset
    return c

def sim(gens):
    getleft = lambda p: max(0, 4 - p.index('#'))
    getright = lambda p: (4 - (len(p) - 1 - p.rindex('#')))
    offset = getleft(initial)
    pots = '.' * offset + initial + '.' * getright(initial)

    diffs = [0]
    prev = 0
    for g in range(gens):
        new = '..' + ''.join([rules[pots[i - 2:i + 3]] for i in range(2, len(pots) - 2)]) + '..'
        l = getleft(new)
        offset += l
        pots = '.' * l + new + '.' * getright(new)

        c = count(pots, offset)
        diff = c - prev
        print(g, c, diff)
        if diff == diffs[-1] == diffs[-2]:
            return count(pots, offset) + (gens - g - 1) * diff

        diffs.append(diff)
        prev = c

    return count(pots, offset)

for gens in (20, 50000000000):
    print(sim(gens))
