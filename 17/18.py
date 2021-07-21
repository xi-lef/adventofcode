import sys
import threading
from collections import defaultdict
from time import sleep

lines = [l.strip().split() for l in sys.stdin]

def resolve(regs, x):
    try:
        return int(x)
    except:
        return regs[x]

c = 0
def exec(lines, part1 = True, pid = 0, other = None):
    regs = defaultdict(int, {'p': pid})
    pc = snd = lc = 0
    global c

    while pc < len(lines):
        i = lines[pc]
        op, x, *y = i
        if y:
            y = resolve(regs, y[0])

        if op == 'snd':
            x = resolve(regs, x)
            if part1:
                snd = x
            else:
                lc += 1
                if pid == 1:
                    c = max(c, lc)
                yield x
        elif op == 'rcv':
            if part1:
                if resolve(regs, x) != 0:
                    yield snd
            else:
                regs[x] = next(other)
        elif op == 'set':
            regs[x] = y
        elif op == 'add':
            regs[x] += y
        elif op == 'mul':
            regs[x] *= y
        elif op == 'mod':
            regs[x] %= y

        if op == 'jgz' and resolve(regs, x) > 0:
            pc += y
        else:
            pc += 1

print(next(exec(lines)))

def p0(): yield from exec(lines, False, 0, p1())
def p1(): yield from exec(lines, False, 1, p0())

t = threading.Thread(target = lambda: list(p0()))
t.daemon = True
t.start()
sleep(3)
print(c)
