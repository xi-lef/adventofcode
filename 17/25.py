import sys
from collections import defaultdict

state = sys.stdin.readline().strip()[-2]
steps = int(sys.stdin.readline().split()[-2])

rules = {}
lines = sys.stdin.readlines()
for i in range(0, len(lines), 10):
    l = list(map(lambda l: l.strip().strip('.:').split()[-1], lines[i + 1 : i + 10]))
    rules[l[0]] = {int(l[1]): (int(l[2]), *l[3 : 5]), int(l[5]): (int(l[6]), *l[7 : 9])}

tape = defaultdict(int)
cur = 0
for _ in range(steps):
    w, d, ns = rules[state][tape[cur]]
    tape[cur] = w
    cur += 1 if d == 'right' else -1
    state = ns
print(sum(tape.values()))
