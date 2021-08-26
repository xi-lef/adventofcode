import re
import sys
import z3

bots = {}
for l in sys.stdin:
    x, y, z, r = map(int, re.findall(r'-?\d+', l))
    bots[x, y, z] = r

def dist(a, b):
    return sum(map(lambda v: abs(v[0] - v[1]), zip(a, b)))

pos, rad = max(bots.items(), key = lambda b: b[1])
print(sum(1 for other in bots if dist(pos, other) <= rad))

def zabs(x):
    return z3.If(x < 0, -x, x)

o = z3.Optimize()
X, Y, Z = z3.Ints('x y z')
for (x, y, z), r in bots.items():
    o.add_soft(zabs(X - x) + zabs(Y - y) + zabs(Z - z) <= r)
o.check()
print(o.model().eval(X + Y + Z))
