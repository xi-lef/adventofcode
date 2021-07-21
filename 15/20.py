import sys

wanted = int(sys.stdin.readline())

m = wanted // 30
presents1 = [0 for _ in range(m)]
presents2 = [0 for _ in range(m)]
for e in range(1, m):
    for h in range(e, m, e):
        presents1[h] += e
    for h in range(e, min(m, e * 50), e):
        presents2[h] += e

print(next(i for i, p in enumerate(presents1) if p * 10 >= wanted))
print(next(i for i, p in enumerate(presents2) if p * 11 >= wanted))
