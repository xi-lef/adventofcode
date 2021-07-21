import sys
from functools import reduce
from itertools import combinations
from operator import mul

packages = {int(l) for l in sys.stdin.read().split()}
all = sum(packages)

def possible(packs, groups):
    all = sum(packs)
    for i in range(1, len(packs)):
        for comb in combinations(packs, i):
            if sum(comb) * groups == all:
                if groups == 2:
                    return True
                return possible(packs ^ set(comb), groups - 1)
    return False

for groups in (3, 4):
    found = []
    for i in range(2, len(packages)):
        for comb in combinations(packages, i):
            s = sum(comb)
            if groups * s != all:
                continue
            if possible(packages ^ set(comb), groups - 1):
                found.append(comb)
        if found:
            break
    print(min(reduce(mul, c) for c in found))
