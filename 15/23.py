import sys
from collections import defaultdict

lines = [l.strip().split() for l in sys.stdin]

def exec(a = 0):
    vals = defaultdict(int, {'a': a})
    pc = 0
    while pc < len(lines):
        i = lines[pc]
        #print(i)
        op = i[0]
        a, *b = i[1:]
        a = a.strip(',')
        if b:
            b, = b
            b = int(b)
        pc += 1

        if op == 'inc':
            vals[a] += 1
        elif op == 'hlf':
            vals[a] //= 2
        elif op == 'tpl':
            vals[a] *= 3

        if op == 'jmp':
            pc += int(a) - 1
        elif op == 'jie':
            if vals[a] % 2 == 0:
                pc += b - 1
        elif op == 'jio':
            if vals[a] == 1:
                pc += b - 1

    return vals['b']

print(exec())
print(exec(1))
