import sys

lines = [l.strip() for l in sys.stdin]

dir = {'U': -1j, 'D': 1j, 'R': 1, 'L': -1}
pos1 = 1 + 1j
valid1 = [a + b * 1j for b in range(3) for a in range(3)]
pos2 = 0 + 2j
valid2 = [
    2,
    *(a + 1j for a in range(1, 4)),
    *(a + 2j for a in range(5)),
    *(a + 3j for a in range(1, 4)),
    2 + 4j
]

for pos, valid in ((pos1, valid1), (pos2, valid2)):
    code = []
    for l in lines:
        for c in l:
            v = dir[c]
            if pos + v in valid:
                pos += v
        code.append(pos)
    print(''.join([hex(valid.index(d) + 1)[-1].upper() for d in code]))
