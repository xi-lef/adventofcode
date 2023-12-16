import curses
import re
from more_itertools import grouper
from time import sleep

rocks = set()

for l in open(0):
    px, py, *nums = (int(x) for x in re.findall(r'\d+', l))
    for (x, y) in grouper(nums, 2):
        minx, maxx, miny, maxy = *sorted((px, x)), *sorted((py, y))
        for cx in range(minx, maxx + 1):
            for cy in range(miny, maxy + 1):
                rocks.add(cx + 1j * cy)
        px, py = x, y

abyss = max(c.imag for c in rocks)

def draw(rocks, stdscr):
    minx = int(min(c.real for c in rocks)) - 1
    stdscr.clear()
    for r in rocks:
        stdscr.addch(int(r.imag), int(r.real) - minx, '#')
    stdscr.refresh()
    sleep(3)

def sim(rocks, floor = None):
    map = rocks.copy()
    if floor:
        for x in range(-10000, 10000):
            map.add(x + 1j * floor)

    count = 0
    startx = 500
    while True:
        pos = startx
        while True:
            if not floor and pos.imag > abyss:
                return count
            if pos + 1j not in map:
                pos += 1j
                continue
            if pos - 1 + 1j not in map:
                pos += -1 + 1j
                continue
            if pos + 1 + 1j not in map:
                pos += 1 + 1j
                continue

            map.add(pos)
            count += 1
            if pos == startx:
                return count
            break

count = sim(rocks)
print(count)

count = sim(rocks, abyss + 2)
print(count)
