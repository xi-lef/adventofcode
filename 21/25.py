from itertools import count

right = set()
down = set()
for y, l in enumerate(open(0)):
    for x, c in enumerate(l.strip()):
        if c == '>': right.add((x, y))
        elif c == 'v': down.add((x, y))
h = max(y for _, y in right | down) + 1
w = max(x for x, _ in right | down) + 1

for steps in count(1):
    both = right | down
    nright = {((x + (((x + 1) % w, y) not in both)) % w, y) for x, y in right}
    both = nright | down
    ndown = {(x, (y + ((x, (y + 1) % h) not in both)) % h) for x, y in down}

    if nright == right and ndown == down:
        print(steps)
        break
    right = nright
    down = ndown
