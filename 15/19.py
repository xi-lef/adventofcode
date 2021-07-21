import sys
from collections import defaultdict
from os.path import commonprefix
from random import shuffle

rules = defaultdict(set)
revrules = {}
for l in sys.stdin:
    l = l.strip()
    if not l:
        break
    l, r = l.split(' => ')
    rules[l].add(r)
    assert r not in revrules
    revrules[r] = l
med = sys.stdin.readline().strip()

def replace_nth(s, n, l, r):
    pos = s.find(l)
    for _ in range(n):
        pos = s.find(l, pos + 1)
    return s[: pos] + r + s[pos + len(l) :]

all = set()
for l, rs in rules.items():
    for r in rs:
        for i in range(med.count(l)):
            #all.add(med.replace(l, r, i + 1).replace(r, l, i))
            all.add(replace_nth(med, i, l, r))
print(len(all))

def expand(mol, match = med, steps = 0):
    #print(mol, match, steps)
    if mol == match:
        return steps

    ret = 1e9
    if len(mol) > len(match):
        return ret

    ls = [l for l in rules if mol.startswith(l)]
    if not ls:
        return ret
    l = ls[0]

    rs = list(rules[l])
    rs.sort(key = lambda r: len(commonprefix([r, match])), reverse = True)
    for r in rules[l]:
        #ret = min(ret, expand(mol.replace(l, r, 1)[pre :], match[pre :], steps + 1))
        for i in range(mol.count(l)):
            ret = min(ret, expand(replace_nth(mol, i, l, r), match, steps + 1))
    return ret
#print(expand('e'))

rights = list(revrules.keys())
rights.sort(key = lambda r: len(r), reverse = True)

tried = set()
def reduce(mol, steps = 0):
    #print(steps, mol)
    if mol == 'e':
        print(steps)
        return steps
    ret = 1e9
    if mol in tried:
        #print('no')
        return ret
    tried.add(mol)

    #r = next(r for r in rights if mol.startswith(r))
    #r = next(r for i in range(len(mol)) for r in rights if mol.startswith(r, i))
    #return reduce(mol.replace(r, revrules[r], 1), steps + 1)
    #for i in range(len(mol)):
    #for i in range(mol.count(r)):
    for r in rights:
            #if mol.startswith(r, i):
        if r in mol:
            #print(mol, r)
            ret = min(ret, reduce(mol.replace(r, revrules[r], 1), steps + 1))
    return ret
#print(reduce(med))

lrules = list(revrules.items())
while True:
    steps = 0
    cur = med
    while True:
        bla = cur
        for r, l in lrules:
            if r in bla:
                bla = bla.replace(r, l, 1)
                steps += 1
        if bla == cur:
            break
        cur = bla
    if cur == 'e':
        break
    shuffle(lrules)
print(steps)

# TODO cyk
