import math
import re
from itertools import cycle

lines = [l.strip() for l in open(0).readlines()]
instructions = lines[0]
network = {}
starts = []
for l in lines[2 :]:
    a, b, c = re.findall(r'\w+', l)
    network[a] = (b, c)
    if a[-1] == 'A':
        starts.append(a)

def walk(start, is_finished):
    cur = start
    steps = 0
    for step in cycle(instructions):
        if is_finished(cur):
            return steps
        cur = network[cur][step == 'R']
        steps += 1

print(walk('AAA', lambda n: n == 'ZZZ'))
print(math.lcm(*[walk(s, lambda n: n[-1] == 'Z') for s in starts]))
