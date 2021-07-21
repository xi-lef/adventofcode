import sys
from collections import defaultdict

lines = [l.strip().split() for l in sys.stdin]

def resolve(regs, a):
    if a[0] == '-':
        a = a[1:]
        v = -1
    else:
        v = 1
    if a.isdecimal():
        v *= int(a)
    else:
        v *= regs[a]
    return v

def exec(a = 0):
    count = pc = 0
    regs = defaultdict(int, {'a': a})
    while pc < len(lines):
        op, a, b = lines[pc]
        b = resolve(regs, b)
        pc += 1

        if op == 'set':
            regs[a] = b
        elif op == 'sub':
            regs[a] -= b
        elif op == 'mul':
            count += 1
            regs[a] *= b
        elif op == 'jnz':
            if resolve(regs, a):
                pc += b - 1
    return count, regs['h']

print(exec()[0])
#print(exec(1)[1])
