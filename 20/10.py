import functools
import sys

lines = [0]
for l in sys.stdin:
    lines.append(int(l.rstrip('\n')))
lines.sort()
lines.append(lines[-1] + 3)

d = [0, 0, 0]
for i in range(len(lines) - 1):
    d[lines[i + 1] - lines[i] - 1] += 1

print('first part:', d[0] * d[2])

#p = [0] * len(lines)
#for i in range(len(lines)):
#    for j in range(i + 1, min(len(lines), i + 4)):
#        if lines[j] > lines[i] + 3:
#            break
#        p[i] += 1

#print(p[:-1])
#print(f'possibilities: {functools.reduce(lambda a, b: a * b, p[:-1])}')

dp = [0] * len(lines)
dp[-1] = 0
dp[-2] = dp[-3] = 1
for i in range(len(lines) - 3, -1, -1):
    dp[i] = sum([dp[j] for j in range(i + 1, len(lines)) if lines[j] <= lines[i] + 3])
print(dp)
print('possibilities:', dp[0])
