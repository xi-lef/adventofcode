import sys
from collections import defaultdict

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

def exec(lines, a = 0):
    vals = defaultdict(int, {'a': a})
    pc = 0
    while pc < len(lines):
        instr = lines[pc]
        #print(pc, instr)
        op = instr[0]
        a, *b = instr[1:]
        if b:
            b = b[0]
        pc += 1

        if op == 'cpy':
            vals[b] = resolve(a, vals)
        elif op == 'jnz':
            if resolve(a, vals):
                pc += resolve(b, vals) - 1
        elif op == 'inc':
            vals[a] += 1
        elif op == 'dec':
            vals[a] -= 1
        elif op == 'tgl':
            a = resolve(a, vals) - 1
            if pc + a not in range(len(lines)):
                continue
            o = lines[pc + a]
            if o[0] == 'tgl':
                o[0] = 'wait' if a == -1 else 'inc'
            else:
                o[0] = {'inc': 'dec', 'dec': 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}[o[0]]
        elif op == 'wait':
            instr[0] = 'inc'

    return vals['a']

print(exec([x[:] for x in lines], 7))
print(exec([x[:] for x in lines], 12)) # runtime (pypy3): 3m40s
