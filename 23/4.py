lines = open(0).readlines()

score = 0
cards = {i: 1 for i in range(len(lines))}
for i, line in enumerate(lines):
    have, win = (set(int(x) for x in p.split())
                 for p in line.split(':')[1].split('|'))
    matches = len(have & win)
    if matches:
        score += 2 ** (matches - 1)
    for j in range(matches):
        cards[i + 1 + j] += cards[i]
print(score)
print(sum(cards.values()))
