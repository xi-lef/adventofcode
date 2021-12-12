from collections import Counter

orig = Counter(int(x) for x in open(0).read().split(','))

for days in (80, 256):
    fish = orig.copy()
    for _ in range(days):
        nfish = Counter()
        for k, v in fish.items():
            nfish[6 if k == 0 else k - 1] += v
        nfish[8] = fish[0]
        fish = nfish
    print(sum(fish.values()))
