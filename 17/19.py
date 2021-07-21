import sys

path = set()
letters = {}
for y, l in enumerate(sys.stdin):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c.isalpha():
            letters[p] = c
        if not c.isspace():
            path.add(p)

pos = min(path, key = lambda x: x.imag)
dir = 1j
res = ''
steps = 0
while True:
    steps += 1
    if pos in letters:
        res += letters[pos]

    if pos + dir in path:
        pass
    elif pos + 1j * dir in path:
        dir *= 1j
    elif pos - 1j * dir in path:
        dir *= -1j
    else:
        break
    pos += dir
print(res, steps)
