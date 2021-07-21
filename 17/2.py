import sys

lines = []
for l in sys.stdin:
    lines.append([int(x) for x in l.split()])

c1 = c2 = 0
for l in lines:
    c1 += max(l) - min(l)
    for a in l:
        for b in l:
            if a != b and a % b == 0:
                c2 += a // b
                print(c2)
print(c1, c2)
