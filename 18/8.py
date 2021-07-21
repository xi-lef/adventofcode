from collections import defaultdict
import sys

nums = [int(x) for x in sys.stdin.readline().split()]

def meta(n):
    c, m = n[0:2]
    length = 2

    if c == 0:
        s = sum(n[2:2 + m])
        return length + m, s, s

    metasum = 0
    values = defaultdict(int)
    for i in range(c):
        l, s, v = meta(n[length:])
        length += l
        metasum += s
        values[i + 1] = v

    metadata = n[length:length + m]
    return length + m, metasum + sum(metadata), sum(values[c] for c in metadata)

print(*meta(nums)[1:3])
