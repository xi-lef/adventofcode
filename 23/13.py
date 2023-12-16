patterns = [p.split() for p in open(0).read().split('\n\n')]

def calc_diff(a, b):
    return sum(x != y for x, y in zip(a, b))

def turn(lines):
    return list(zip(*lines))

def is_reflecting(pattern, smudges):
    for i in range(len(pattern) - 1):
        diff = 0
        for j in range(min(i + 1, len(pattern) - i - 1)):
            diff += calc_diff(pattern[i - j], pattern[i + j + 1])
            if diff > 1:
                break
        else:
            if diff == smudges:
                return i + 1
    return 0

for smudges in (0, 1):
    score = 0
    for p in patterns:
        score += is_reflecting(turn(p), smudges)
        score += 100 * is_reflecting(p, smudges)
    print(score)
