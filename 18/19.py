import sys
from collections import defaultdict

ip = int(sys.stdin.readline().split()[-1])
prog = [l.split() for l in sys.stdin]
for i in prog:
    op, *args = i
    i[:] = (op, *map(int, args))

def exec(r0 = 0):
    regs = defaultdict(int, {0: r0})

    while 0 <= regs[ip] < len(prog):
        op, a, b, c = prog[regs[ip]]
        #print(op, a, b, c, regs)
        if op.startswith('gt') or op.startswith('eq'):
            ra, rb = op[2 :]
            op = op[: 2]
        else:
            rb = op[-1]
            ra = 'r' if not op.startswith('set') else rb
            op = op[: -1]

        if ra == 'r':
            a = regs[a]
        if rb == 'r':
            b = regs[b]

        regs[c] = {'add': a + b,
                   'mul': a * b,
                   'ban': a & b,
                   'bor': a | b,
                   'set': a,
                   'gt': a > b,
                   'eq': a == b}[op]

        #print(a, b, c, ra, rb, regs, '\n')
        regs[ip] += 1

    return regs[0]

print(exec())
print(exec(1))
