poss = [int(x) for x in open(0).read().split(',')]

mfuel1 = mfuel2 = 1e9
for i in range(min(poss), max(poss) + 1):
    mfuel1 = min(mfuel1, sum(abs(p - i) for p in poss))
    mfuel2 = min(mfuel2, sum((abs(p - i) ** 2 + abs(p - i)) // 2 for p in poss))
print(mfuel1)
print(mfuel2)
