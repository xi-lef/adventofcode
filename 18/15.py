import sys
from copy import deepcopy
from itertools import count


def pr():
    full = [['#' for _ in range(int(max(x.real for x in open)) + 2)]
            for _ in range(int(max(x.imag for x in open)) + 2)]
    for g, c in ((open, '.'), ((e.pos for e in elves), 'E'), ((g.pos for g in goblins), 'G')):
        for p in g:
            full[int(p.imag)][int(p.real)] = c
    print('\n'.join(''.join(l) for l in full))


ELVES, GOBLINS = range(2)
dirs = (-1j, -1, 1, 1j)


class Unit:
    def __init__(self, pos, side):
        self.pos = pos
        self.side = side
        self.atk = 3
        self.hp = 200

    @property
    def allies(self):
        return elves if self.side == ELVES else goblins

    @property
    def enemies(self):
        return goblins if self.side == ELVES else elves

    def can_attack(self):
        return any(self.pos + d in {e.pos for e in self.enemies} for d in dirs)

    def try_attack(self):
        epos = {e.pos: e for e in self.enemies}
        cands = []
        for d in dirs:
            n = self.pos + d
            if n in epos.keys():
                cands.append(n)
        if not cands:
            return None

        target = epos[min(cands, key = lambda x: (epos[x].hp, x.imag, x.real))]
        target.hp -= self.atk
        return target.hp <= 0

    def move(self):
        enemies_pos = {e.pos for e in self.enemies}
        units_pos = enemies_pos | {e.pos for e in self.allies}

        limit = 1e9
        cands = []
        visited = set()
        stack = [(self.pos, 0, None)]
        while stack:
            cur, steps, move = stack.pop(0)
            if steps > limit:
                break
            if cur in visited:
                continue
            visited.add(cur)

            for d in dirs:
                n = cur + d

                if n in enemies_pos:
                    cands.append((cur, move))
                    limit = steps
                elif n in open and n not in units_pos:
                    stack.append((n, steps + 1, move if move else d))
        #print('cands', cands)

        if not cands:
            return

        _, move = min(cands, key = lambda x: (x[0].imag, x[0].real, dirs.index(x[1])))
        self.pos += move
        return move


def fight(elves, goblins, num_elves = None):
    for round in count():
        #print('round', round); pr()

        if num_elves and len(elves) < num_elves:
            return None

        units = elves + goblins
        units.sort(key = lambda u: (u.pos.imag, u.pos.real))
        for unit in units:
            if unit.hp <= 0:
                continue
            if not unit.enemies:
                return round * sum(u.hp for u in elves + goblins)

            if not unit.can_attack():
                unit.move()
            ret = unit.try_attack()
            if ret:
                for g in (elves, goblins):
                    g[:] = (u for u in g if u.hp > 0)


open = set()
elves = []
goblins = []
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l.strip()):
        pos = x + y * 1j
        if c != '#':
            open.add(pos)
        if c == 'E':
            elves.append(Unit(pos, ELVES))
        elif c == 'G':
            goblins.append(Unit(pos, GOBLINS))

num_elves = len(elves)
_elves = deepcopy(elves)
_goblins = deepcopy(goblins)

print(fight(elves, goblins))

for boost in count(1):
    elves = deepcopy(_elves)
    goblins = deepcopy(_goblins)
    for e in elves:
        e.atk += boost

    ret = fight(elves, goblins, num_elves)
    if ret:
        print(ret)
        break
