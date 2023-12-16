from collections import defaultdict
from itertools import count

N, S, W, E = considers = [-1j, 1j, -1, 1]
elves = set()
for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        if c == '#':
            elves.add(x + 1j * y)

def pr(elves):
    min_x = int(min(e.real for e in elves))
    max_x = int(max(e.real for e in elves))
    min_y = int(min(e.imag for e in elves))
    max_y = int(max(e.imag for e in elves))
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print('#' if x + 1j * y in elves else '.', end = '')
        print()
    print()

for round in count():
    #print(round, considers)
    #pr(elves)

    if round == 10:
        xs = sorted(e.real for e in elves)
        ys = sorted(e.imag for e in elves)
        w = xs[-1] - xs[0] + 1
        h = ys[-1] - ys[0] + 1
        print(int(w * h) - len(elves))

    done = True
    proposals = defaultdict(set)
    new_elves = set()
    for elf in elves:
        dirs = [all(elf + consider + (1 if consider.imag else 1j) * d
                    not in elves for d in (-1, 0, 1))
                for consider in considers]
        if all(dirs) or not any(dirs):
            new_elves.add(elf)
        else:
            done = False
            proposals[elf + considers[dirs.index(True)]].add(elf)

    if done:
        print(round + 1)
        break

    for proposal, origs in proposals.items():
        if len(origs) == 1:
            new_elves.add(proposal)
        else:
            for o in origs:
                new_elves.add(o)

    elves = new_elves
    considers.append(considers[0])
    del considers[0]
