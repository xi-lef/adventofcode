import sys
knot_hash = __import__('10').knot_hash

input = sys.stdin.readline().strip()

used = set()
for y in range(128):
    row = knot_hash(input + '-' + str(y))
    b = bin(int(row, 16))[2:].zfill(128)
    for x, c in enumerate(b):
        if c == '1':
            used.add(x + y * 1j)

print(len(used))

regions = 0
while used:
    regions += 1
    region = {used.pop()}
    while region:
        cur = region.pop()
        for d in (-1, 1j, 1, -1j):
            n = cur + d
            if n in used:
                used.remove(n)
                region.add(n)

print(regions)
