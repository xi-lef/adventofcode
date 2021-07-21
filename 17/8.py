from collections import defaultdict
import sys

lines = [l.strip().split() for l in sys.stdin]

regs = defaultdict(int)
m = 0
for l in lines:
    x, cmp, v = l[-3:]
    v = int(v)
    if (cmp == '>' and regs[x] > v
            or cmp == '<' and regs[x] < v
            or cmp == '<=' and regs[x] <= v
            or cmp == '>=' and regs[x] >= v
            or cmp == '==' and regs[x] == v
            or cmp == '!=' and regs[x] != v):
        reg, op, change = l[:3]
        regs[reg] += (-1 if op == 'dec' else 1) * int(change)
        m = max(m, regs[reg])
print(max(regs.values()), m)
