import itertools
from intcode import *

program = get_program()

m = 0
for p in itertools.permutations(range(5)):
    o = [0]
    for i in range(len(p)):
        o = list(run(program, iter([p[i]] + o)))
    m = max(m, o[0])
print(m)

m = 0
for p in itertools.permutations(range(5, 10)):
    def amp_a(): yield from run(program, itertools.chain([p[0], 0], amp_e()))
    def amp_b(): yield from run(program, itertools.chain([p[1]], amp_a()))
    def amp_c(): yield from run(program, itertools.chain([p[2]], amp_b()))
    def amp_d(): yield from run(program, itertools.chain([p[3]], amp_c()))
    def amp_e(): yield from run(program, itertools.chain([p[4]], amp_d()))

    m = max(m, list(amp_e())[-1])
print(m)
