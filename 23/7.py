from collections import Counter
from functools import cmp_to_key

lines = [l.split() for l in open(0)]
hands = {l[0]: int(l[1]) for l in lines}
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def compare(a, b, part2 = False):
    a_cnt = Counter(a)
    b_cnt = Counter(b)
    if part2:
        for cnt in (a_cnt, b_cnt):
            cnt['1'] = 0 # any invalid card, in case of 'JJJJJ'
            most = cnt.most_common()
            i = 1 if most[0][0] == 'J' else 0
            cnt[most[i][0]] += cnt['J']
            del cnt['J']

    for x, y in zip(a_cnt.most_common(), b_cnt.most_common()):
        diff = x[1] - y[1]
        if diff:
            return diff

    i = 0
    while a[i] == b[i]:
        i += 1
    # b - a, not a - b because of index()!
    return order.index(b[i]) - order.index(a[i])

def compare2(a, b):
    return compare(a, b, True)

cards = list(hands.keys())
cards.sort(key = cmp_to_key(compare))
p = lambda: print(sum(hands[c] * i for i, c in enumerate(cards, start = 1)))
p()

order.remove('J')
order.append('J')
cards.sort(key = cmp_to_key(compare2))
p()
