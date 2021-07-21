import sys

p = [[], []]
i = 0
sys.stdin.readline()
for l in sys.stdin:
    l = l.rstrip('\n')
    if not l:
        i = 1
        sys.stdin.readline()
        continue
    p[i].append(int(l))


def play(p1, p2, part2 = True):
    prev = set()
    #print('bla', p1, p2)
    while True:
        if not p1:
            return p2, 2
        if not p2:
            return p1, 1

        k = tuple(tuple(x) for x in (p1, p2))
        if k in prev:
            return p1, 1
        prev.add(k)

        c1 = p1.pop(0)
        c2 = p2.pop(0)

        if part2 and len(p1) >= c1 and len(p2) >= c2:
            _, win = play(p1[:c1], p2[:c2])
            #print('rec', win, c1, c2, p1, p2)
            if win == 1:
                p1.extend((c1, c2))
            else:
                p2.extend((c2, c1))
        elif c1 > c2:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))

count = 0
for i, c in enumerate(play(p[0][:], p[1][:], False)[0][::-1]):
    count += (i + 1) * c
print(count)
count = 0
for i, c in enumerate(play(p[0], p[1])[0][::-1]):
    count += (i + 1) * c
print(count)
