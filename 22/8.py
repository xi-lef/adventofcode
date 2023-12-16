grid = {}

for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        grid[x + 1j * y] = int(c)

maxx = max(x.real for x in grid)
maxy = max(x.imag for x in grid)

visible = set()
maxscore = 0
for pos in grid:
    score = 1
    for d in (1, -1, 1j, -1j):
        dist = 1
        p = pos + d
        while p in grid:
            if grid[p] >= grid[pos]:
                break
            p += d
            dist += 1
        else:
            dist -= 1
            visible.add(pos)
        score *= dist
    maxscore = max(maxscore, score)

#for y in range(int(maxy) + 1):
#    for x in range(int(maxx) + 1):
#        print('t' if x + 1j * y in visible else ' ', end = '')
#    print()
print(len(visible))
print(maxscore)
