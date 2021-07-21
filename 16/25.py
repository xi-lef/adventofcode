import sys
from collections import defaultdict
from itertools import count, cycle, islice

lines = [l.strip().split() for l in sys.stdin]

def resolve(a, vals):
    if a[0] == '-':
        a = a[1:]
        v = -1
    else:
        v = 1
    if a.isdecimal():
        v *= int(a)
    else:
        v *= vals[a]
    return v

def exec(a):
    vals = defaultdict(int, {'a': a})
    pc = 0
    while pc < len(lines):
        instr = lines[pc]
        op = instr[0]
        a, *b = instr[1:]
        if b:
            b = b[0]
        pc += 1

        if op == 'cpy':
            vals[b] = resolve(a, vals)
        elif op == 'jnz':
            if resolve(a, vals) != 0:
                pc += int(b) - 1
        elif op == 'inc':
            vals[a] += 1
        elif op == 'dec':
            vals[a] -= 1
        elif op == 'out':
            yield resolve(a, vals)

target = list(islice(cycle([0, 1]), 20))
for a in count(1):
    if list(islice(exec(a), 20)) == target:
        print(a)
        break
