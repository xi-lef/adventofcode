from functools import cache

orig = tuple(map(int, (l.split()[-1] for l in open(0))))

players = list(orig)
scores = [0, 0]
for die in range(1, 10000, 3):
    i = die % 2 == 0
    players[i] += 3 * die + 3
    players[i] = (players[i] - 1) % 10 + 1
    scores[i] += players[i]

    if any(s >= 1000 for s in scores):
        print(min(scores) * (die + 2))
        break

@cache
def play(players, scores, turn):
    wins = [0, 0]
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                roll = a + b + c
                p = list(players)
                p[turn] = (p[turn] + roll - 1) % 10 + 1
                s = list(scores)
                s[turn] += p[turn]
                if s[turn] >= 21:
                    wins[turn] += 1
                    continue

                w = play(tuple(p), tuple(s), not turn)
                wins[0] += w[0]
                wins[1] += w[1]
    return wins

print(max(play(orig, (0, 0), 0)))
