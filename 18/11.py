import sys
from functools import cache

serial = int(sys.stdin.readline())
n = 300

@cache
def power(x, y):
    rack = x + 10
    return ((rack * y + serial) * rack) // 100 % 10 - 5

@cache
def total_power(x, y, s):
    if s == 0:
        return 0
    elif s == 1:
        return power(x, y)
    total = (total_power(x, y, s - 1) + total_power(x + 1, y + 1, s - 1)
             + power(x + s - 1, y) + power(x, y + s - 1)
             - total_power(x + 1, y + 1, s - 2))
    return total

mx = my = ms = mt = mx3 = my3 = mt3 = 0
for s in range(1, n + 1):
    print(s, '\r', end = '')
    for x in range(1, n - s + 2):
        for y in range(1, n - s + 2):
            total = total_power(x, y, s)
            if s == 3 and total > mt3:
                mx3 = x
                my3 = y
                mt3 = total
            if total > mt:
                mx = x
                my = y
                ms = s
                mt = total

print(f'{mx3},{my3}', f'{mx},{my},{ms}')
