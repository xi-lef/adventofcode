import sys
from collections import defaultdict
from itertools import chain
from more_itertools import grouper
from operator import add, mul, and_, or_, gt, eq
setitem = lambda a, _: a

samples = []
for sample in grouper(sys.stdin, 4):
    before, instr, after, last = map(lambda s: s.strip(), sample)
    if not before.startswith('Before'):
        break

    before, after = map(eval, (before[8:], after[8:]))
    instr = tuple(map(int, instr.split()))
    samples.append((instr, before, after))

prog = [tuple(map(int, l.strip().split())) for l in chain([last, after], sys.stdin)]

def exec(instr, regs, op, areg, breg):
    a, b = instr[1:3]
    if areg: a = regs[a]
    if breg: b = regs[b]
    return op(a, b)

def get_instrs(sample):
    instr, pre, post = sample
    poss = set()

    def test(op, areg, breg):
        if exec(instr, pre, op, areg, breg) == post[instr[3]]:
            poss.add((op, areg, breg))

    for op in (add, mul, and_, or_):
        test(op, True, False)
        test(op, True, True)

    test(setitem, False, False)
    test(setitem, True, False)

    for op in (gt, eq):
        test(op, False, True)
        test(op, True, False)
        test(op, True, True)

    return poss

instr_map = {}
count = 0
for s in samples:
    poss = get_instrs(s)
    if len(poss) >= 3:
        count += 1

    op = s[0][0]
    # overwriting is fine, every sample is the same basically
    instr_map[op] = poss
print(count)

while any(len(poss) > 1 for poss in instr_map.values()):
    for i, op in instr_map.items():
        if len(op) == 1:
            for j in instr_map:
                if j != i:
                    instr_map[j] -= op

assert all(len(poss) == 1 for poss in instr_map.values()), sorted(instr_map.items())
instr_map = {i: next(iter(op)) for i, op in instr_map.items()}

regs = defaultdict(int)
for instr in prog:
    regs[instr[3]] = exec(instr, regs, *instr_map[instr[0]])
print(regs[0])
