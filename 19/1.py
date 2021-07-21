import sys

c = c2 = 0
for l in sys.stdin:
    f = lambda x: int(x) // 3 - 2
    c += f(l)

    while (l := f(l)) > 0:
        c2 += l
print(c, c2)
