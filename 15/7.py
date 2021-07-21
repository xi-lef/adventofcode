from functools import cache
import sys

wires = {}
for l in sys.stdin:
    p = l.strip().split(' ')
    wires[p[-1]] = p[:p.index('->')]
#print(wires)

@cache # TODO why???
def resolve(w):
    if w not in wires:
        return int(w)
    val = wires[w]

    if len(val) == 1:
        return resolve(val[0])
    elif len(val) == 2:
        return ~resolve(val[1])

    a, op, b = val[0:3]
    a = resolve(a)
    b = resolve(b)
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'LSHIFT':
        return a << b
    elif op == 'RSHIFT':
        return a >> b

a = resolve('a')
print(a)

wires['b'] = [str(a)]
resolve.cache_clear()
print(resolve('a'))
