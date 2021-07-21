import curses
from intcode import *
from time import sleep

stdscr = curses.initscr()
def pscreen(s):
    w, h = 41, 22
    out = [[''] * (w + 1) for _ in range(h + 1)]
    for (x, y), v in s.items():
        if v == 0: d = ' '
        elif v == 1: d = '#'
        elif v == 2: d = 'B'
        elif v == 3: d = '‾'
        else: d = 'O'
        out[y][x] = d
    out = '\n'.join([''.join(l) for l in out])
    stdscr.clear()
    stdscr.addstr(out)
    stdscr.refresh()

program = get_program()

screen = {}
r = run(program[:])
for x in r:
    y = next(r)
    id = next(r)
    screen[x, y] = id
print(len([k for k, v in screen.items() if v == 2]))
#pscreen(screen)

program[0] = 2
input = [0]
screen = {}
paddle = ball = score = -1
r = run(program, input)
for x in r:
    y = next(r)
    id = next(r)

    if x == -1 and y == 0:
        score = id
    else:
        screen[x, y] = id

    if id == 3:
        paddle = x
    elif id == 4:
        ball = x
        if score != -1: # game started
            input.append((max(-1, min(1, ball - paddle))))
        #pscreen(screen); sleep(0.01)

#sleep(2)
curses.endwin()
print(score)
