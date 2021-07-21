import sys

banks = [int(x) for x in sys.stdin.readline().split()]

n = len(banks)
steps = 0
seen = {tuple(banks): 0}
while True:
    m = max(banks)
    b = banks.index(m)
    banks[b] = 0
    for i in range(m):
        banks[(b + i + 1) % n] += 1
        m -= 1

    steps += 1
    if tuple(banks) in seen:
        break
    seen[tuple(banks)] = steps
print(steps, steps - seen[tuple(banks)])
