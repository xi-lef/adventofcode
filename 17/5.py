import sys

offsets = [int(x) for x in sys.stdin]

cur = steps = 0
while cur in range(len(offsets)):
    old = offsets[cur]
    #offsets[cur] += 1
    offsets[cur] += -1 if old > 2 else 1
    cur += old
    steps += 1
print(steps)
