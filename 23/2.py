from collections import defaultdict
from functools import reduce
from operator import mul

lines = [l.strip() for l in open(0)]
bag = {'red': 12, 'green': 13, 'blue': 14}

min_bags = []
score = 0
for l in lines:
    game, r = l.split(':')
    game_num = int(game.split()[1])

    min_bag = defaultdict(int)
    possible = True
    for round in r.split(';'):
        for cubes in round.split(','):
            n, color = cubes.split()
            n = int(n)

            min_bag[color] = max(min_bag[color], n)
            if n > bag[color]:
                possible = False

    min_bags.append(min_bag)
    if possible:
        score += game_num
print(score)
print(sum(reduce(mul, d.values()) for d in min_bags))
