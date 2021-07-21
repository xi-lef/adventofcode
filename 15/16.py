import sys
from collections import defaultdict

sues = {}
for l in sys.stdin:
    l = l.strip().split(': ')
    num = int(l[0][4:])
    l = [x for w in l[1:] for x in w.split(', ')]
    sues[num] = defaultdict(lambda: -1, {l[i]: int(l[i + 1]) for i in range(0, len(l), 2)})
gifter = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0,
          'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

for num, info in sues.items():
    if all(n == gifter[i] for i, n in info.items() if n != -1):
        print(num)
        break

for num, info in sues.items():
    if all(n > gifter[i] if i in ('cats', 'trees') else
           n < gifter[i] if i in ('pomeranians', 'goldfish') else
           n == gifter[i] for i, n in info.items() if n != -1):
        print(num)
        break
