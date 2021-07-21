import sys
from itertools import count


GOBLIN = 0
ELF = 1
class Unit:
    def __init__(self, pos, side):
        self.pos = pos
        self.side = side
        self.atk = 3
        self.hp = 200

    def distance(self, unit):
        return self.pos

    def can_attack(self, units):
        for unit in units:
            if unit == self:
                continue


units = []
walls = set()

for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l.strip()):
        pos = x + y * 1j
        if c == '#':
            walls.add(pos)
        elif c in ('E', 'G'):
            units.append(Unit(pos, ELF if c == 'E' else GOBLIN))

for round in count():
    units.sort(key = lambda u: [u.pos.imag, u.pos.real])
    if len(set(u.side for u in units)) == 1:
        break

    for unit in units:
        pass

print(round * sum(u.hp for u in units))
