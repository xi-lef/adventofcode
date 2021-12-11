from collections import Counter

ls = [l.strip() for l in open(0)]

MOST, LEAST = 0, -1
def f(ls, i):
    e = ''
    for bs in zip(*ls):
        c = Counter(bs).most_common()
        if len(c) > 1 and c[0][1] == c[1][1]:
            e += '1' if i == 0 else '0'
        else:
            e += c[i][0]
    return e

print(int(f(ls, MOST), 2) * int(f(ls, LEAST), 2))

o2 = ls
co2 = ls.copy()
for ls, crit in ((o2, MOST), (co2, LEAST)):
    b = 0
    while len(ls) > 1:
        ls[:] = [x for x in ls if x[b] == f(ls, crit)[b]]
        b += 1

print(int(o2[0], 2) * int(co2[0], 2))
