import math
import sys
from collections import defaultdict

target = int(sys.stdin.readline())

sqrt = math.floor(math.sqrt(target))
sqrt -= sqrt % 2 == 0
steps = sqrt + 1
change = -1
start = sqrt ** 2 + 1
for i in range(1, target - start + 2):
    steps += change

    if i % (math.floor(sqrt / 2) + 1) == 0:
        change *= -1
print(steps)

grid = defaultdict(int, {0: 1})
cur = r = 1
dir = 1j
next = False
while True:
    val = 0
    for dx in (-1, 0, 1):
        for dy in (-1j, 0, 1j):
            val += grid[cur + dx + dy]
    grid[cur] = val
    if val > target:
        print(val)
        break

    cur += dir
    if cur.real == r and cur.imag == -r:
        r += 1
        next = True
    elif next or abs(cur.real) == abs(cur.imag) == r:
        dir *= 1j
        next = False
