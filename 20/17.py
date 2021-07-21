import copy
import sys

lines = []
for l in sys.stdin:
    l = l.rstrip('\n')
    lines.append(l)

active = '#'
inactive = '.'
cycles = 6
n = len(lines)
bla = n + cycles * 2
space = [[[inactive for _ in range(bla)] for _ in range(bla)] for _ in range(bla)]
space4 = [[[[inactive for _ in range(bla)] for _ in range(bla)] for _ in range(bla)] for _ in
         range(bla)]
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        space[0][i][j] = c
        space4[0][0][i][j] = c

def adj_active(x, y, z):
    c = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                if i == j == k == 0:
                    continue
                if space[(z + i) % bla][(y + j) % bla][(x + k) % bla] == active:
                    c += 1
    return c
def adj_active4(x, y, z, w):
    c = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            for k in (-1, 0, 1):
                for l in (-1, 0, 1):
                    if i == j == k == l == 0:
                        continue
                    if space4[(w + l) % bla][(z + i) % bla][(y + j) % bla][(x + k) % bla] == active:
                        c += 1
    return c

#print(space)
#print('\n\n'.join('\n'.join(''.join(t) for t in s) for s in space))
#print('\n\n\n')

for i in range(cycles):
    new = copy.deepcopy(space)
    new4 = copy.deepcopy(space4)
    for x in range(bla):
        for y in range(bla):
            for z in range(bla):
                num = adj_active(x, y, z)
                s = space[z][y][x]
                if s == active and not 2 <= num <= 3:
                    new[z][y][x] = inactive
                elif s == inactive and num == 3:
                    new[z][y][x] = active

                for w in range(bla):
                    num = adj_active4(x, y, z, w)
                    s = space4[w][z][y][x]
                    if s == active and not 2 <= num <= 3:
                        new4[w][z][y][x] = inactive
                    elif s == inactive and num == 3:
                        new4[w][z][y][x] = active
    space = new
    space4 = new4

#print(space)
#print('\n\n'.join('\n'.join(''.join(t) for t in s) for s in space))
print(''.join(''.join(''.join(t) for t in s) for s in space).count(active))
print(''.join(''.join(''.join(''.join(t) for t in s) for s in r) for r in space4).count(active))
