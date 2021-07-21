import math
import sys
from collections import defaultdict

lines = [l.strip() for l in sys.stdin]

prods = {}
for l in lines:
    a, b = l.split(' => ')
    n, c = b.split()
    prods[c] = (int(n), [(int(n), c) for x in a.split(', ') for n, c in [x.split()]])
#print(prods)

def get_ore(fuel = 1):
    need = defaultdict(int, {'FUEL': fuel})
    while any(k != 'ORE' for k, v in need.items() if v > 0):
        #print('\nneed', need.items())

        chem, needed = next((c, n) for c, n in need.items() if n > 0 and c != 'ORE')
        num, req = prods[chem]
        factor = math.ceil(needed / num)
        need[chem] -= factor * num

        #print(needed, chem, 'needed.', num, 'producable from', req, factor, 'times')
        for n, c in req:
            need[c] += factor * n

    return need['ORE']

per_fuel = get_ore()
print(per_fuel)

cargo = 1000000000000
fuel = math.ceil(cargo / per_fuel)
while (ore := get_ore(fuel + 1)) < cargo:
    #print(ore)
    fuel += max(1, (cargo - ore) // per_fuel)
print(fuel)
