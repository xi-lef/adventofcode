import sys

p1 = p2 = 0
for l in sys.stdin:
    pol, pw = l.strip().split(': ')
    nums, c = pol.split()
    a, b = map(int, nums.split('-'))

    if pw.count(c) in range(a, b + 1):
        p1 += 1
    if (pw[a - 1] == c) ^ (pw[b - 1] == c):
        p2 += 1

print(p1, p2)
