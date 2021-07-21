import sys

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\n'))

floor = '.'
empty = 'L'
occu = '#'
h = len(lines)
w = len(lines[0])

def adj_occu(x, y):
    ret = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                continue
            a = x + i
            b = y + j
            if a in range(w) and b in range(h):
                ret += lines[b][a] == occu
    return ret

def adj_occu2(x, y):
    ret = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == j == 0:
                continue
            a = x + i
            b = y + j
            while a in range(w) and b in range(h):
                if lines[b][a] != floor:
                    ret += lines[b][a] == occu
                    break
                a += i
                b += j
    return ret

i = 0
while True:
    i += 1
    new = [''] * h
    for y in range(h):
        for x in range(w):
            seat = lines[y][x]
            num = adj_occu2(x, y) # adj_occu
            if seat == empty and num == 0:
                n = occu
            elif seat == occu and num >= 5: # 4
                n = empty
            else:
                n = seat
            new[y] += n
    if new == lines:
        break
    lines = new

print(f'after {i} iterations, {"".join(lines).count(occu)} seats are occupied')
