import sys

l = sys.stdin.readline().strip('\n')
n = len(l)

c1 = c2 = 0
for i in range(n):
    if l[i] == l[(i + 1) % n]:
        c1 += int(l[i])
    if l[i] == l[(i + n // 2) % n]:
        c2 += int(l[i])
print(c1, c2)
