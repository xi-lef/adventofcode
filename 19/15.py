import curses
from collections import defaultdict
from intcode import *
from time import sleep

NSWE = (N, S, W, E) = (1, 2, 3, 4)
dir = {N: -1j, S: 1j, W: -1, E: 1}

def pmap(map, pos, stdscr):
    ys = [k.imag for k in map]
    xs = [k.real for k in map]
    minx = int(min(xs)) - 1
    miny = int(min(ys)) - 1
    w = int(max(xs) - minx) + 1
    h = int(max(ys) - miny) + 1
    out = [[' '] * (w + 1) for _ in range(h + 1)]
    for x, v in map.items():
        out[int(x.imag) - miny][int(x.real) - minx] = v
    out[int(pos.imag) - miny][int(pos.real) - minx] = 'D'
    out = '\n'.join([''.join(l) for l in out])
    stdscr.clear(); stdscr.addstr(out); stdscr.refresh()

def play(prog):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    input = []
    r = run(prog, input)
    pos = 0
    map = {0: '.'}
    try:
        while True:
            pmap(map, pos, stdscr)
            c = stdscr.getkey()
            if c == 'w': i = N
            elif c == 'a': i = W
            elif c == 's': i = S
            elif c == 'd': i = E
            else: break
            input.append(i)

            a = next(r)
            if a == 0:
                map[pos + dir[i]] = '#'
            else:
                pos += dir[i]
                if a == 1:
                    map[pos] = '.'
                else:
                    map[pos] = 'X'
                for d in NSWE:
                    input.append(d)
                    if next(r) == 0:
                        map[pos + dir[d]] = '#'
                    else:
                        if a == 1:
                            map[pos + dir[d]] = '.'
                        else:
                            map[pos + dir[d]] = 'X'
                        input.append(d + 1 if d % 2 == 1 else d - 1)
                        next(r)
    finally:
        curses.endwin()

#stdscr = curses.initscr(); curses.noecho(); curses.cbreak()
def explore(r, input, map, shortest, pos = 0, steps = 0):
    if shortest[pos] <= steps:
        return 0
    shortest[pos] = steps

    #pmap(map, pos, stdscr); sleep(0.04)
    oxy = 0
    for d in NSWE:
        input.append(d)
        a = next(r)
        if a == 0:
            map[pos + dir[d]] = '#'
        else:
            pos += dir[d]
            if a == 1:
                map[pos] = '.'
            else:
                map[pos] = 'X'
                oxy = pos
            o = explore(r, input, map, shortest, pos, steps + 1)
            if o:
                oxy = o
            input.append(d + 1 if d % 2 == 1 else d - 1)
            next(r)
            pos -= dir[d]
    return oxy

prog = get_program()
#play(prog)

input = []
shortest = defaultdict(lambda: 1e10)
map = {0: '.'}
try:
    oxy = explore(run(prog, input), input, map, shortest)
    #pmap(map, 0, stdscr)
finally:
    #sleep(3); curses.nocbreak(); curses.echo(); curses.endwin()
    pass
print(shortest[oxy])

def walk(map, cur, visited):
    steps = len(visited)

    if shortest[cur] <= steps:
        return 1e10
    shortest[cur] = steps

    for dir in (1, 1j, -1, -1j):
        new = cur + dir
        if map[new] != '#' and new not in visited:
            walk(map, new, visited | set([new]))

shortest.clear()
walk(map, oxy, set())
print(max(shortest.values()))
