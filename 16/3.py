import sys

lines = [int(x) for l in sys.stdin for x in l.split()]

p1 = range(0, len(lines), 3)
# 0, 1, 2, 9, 10, 11, 18, 19, 20, ...
p2 = [i + 6 * (i // 3) for i in range(len(lines) // 3)]

for p, s in (p1, slice(0, 3)), (p2, slice(0, 9, 3)):
    valid = []
    for i in p:
        l = lines[i:][s]
        if sum(l) - max(l) > max(l):
            valid.append(l)
    print(len(valid))
