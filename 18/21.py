import sys
from collections import defaultdict

ip = int(sys.stdin.readline().split()[-1])
prog = [l.split() for l in sys.stdin]
for i in prog:
    op, *args = i
    i[:] = (op, *map(int, args))

def exec():
    regs = defaultdict(int)

    last = 0
    r3 = set()
    while 0 <= regs[ip] < len(prog):
        op, a, b, c = prog[regs[ip]]
        #print(op, a, b, c, regs)

        if op == 'eqrr':
            r = regs[max(a, b)]
            if not r3:
                print(r)
            if r in r3:
                print(last)
                break
            r3.add(r)
            last = r

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

        regs[ip] += 1

exec()
