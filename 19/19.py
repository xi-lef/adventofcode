from intcode import *
from itertools import count

prog = get_program()

def in_beam(x, y):
    return next(run(prog, [x, y]))

print(sum(in_beam(x, y) for x in range(50) for y in range(50)))

x = y = 0
while not in_beam(x + 99, y):
    y += 1
    while not in_beam(x, y + 99):
        x += 1
print(x * 10000 + y)
