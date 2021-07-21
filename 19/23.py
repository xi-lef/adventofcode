from intcode import *

prog = get_program()

n = 50
inputs = [[i] for i in range(n)]
comps = [run(prog, inputs[i]) for i in range(n)]
queue = [list() for _ in range(n)]
nat = None
last_y = -1
idle = False

while True:
    if nat and idle and all(not q for q in queue):
        if nat[1] == last_y:
            print(last_y)
            exit()
        last_y = nat[1]
        inputs[0].extend(nat)
    idle = True

    for i in range(n):
        q = queue[i]
        inputs[i].extend(q)
        q.clear()

        c = comps[i]
        dest = next(c)
        if dest == -1:
            continue
        x = next(c)
        y = next(c)
        idle = False

        if dest == 255:
            if not nat:
                print(y)
            nat = (x, y)
        else:
            queue[dest].extend([x, y])
