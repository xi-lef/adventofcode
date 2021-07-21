import sys

nums = map(int, sys.stdin.readline().split('-'))

c = d = 0
for i in range(next(nums), next(nums) + 1):
    if (s := str(i)) != ''.join(sorted(s)):
        continue
    c += any(s.count(c) > 1 for c in s)
    d += any(s.count(c) == 2 for c in s)
print(c, d)
