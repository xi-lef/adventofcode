from intcode import *
import matplotlib.pyplot as plt

program = get_program()

BLACK = 0
WHITE = 1

def draw(start):
    hull = {}
    dir = pos = 0
    change = {0: 1j, 1: 1, 2: -1j, 3: -1}
    input = [start]
    r = run(program, iter(input))

    for color in r:
        turn = next(r)
        hull[pos] = color
        dir = (dir + 2 * turn - 1) % 4
        pos += change[dir]
        input.append(hull.get(pos, BLACK))
    return hull
print(len(draw(BLACK)))

id = draw(WHITE)
X = [x.real for x, c in id.items() if c == WHITE]
Y = [x.imag for x, c in id.items() if c == WHITE]
plt.scatter(X, Y)
plt.show()
