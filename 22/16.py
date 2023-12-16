import re
from collections import defaultdict

rates = {}
tunnels = {}
for l in open(0):
    #valve = l.split()[1]
    #rate = int(l.split('=')[1].split(';')[0])
    valve_a, *conns = re.findall(r'[A-Z][A-Z]', l)
    rates[valve_a] = int(*re.findall(r'\d+', l))
    tunnels[valve_a] = conns

num_valves = len([r for _, r in rates.items() if r != 0])
most = 0
visited = defaultdict(lambda: (0, 0))
stack = [(('AA', None), 30, 0, frozenset())]
#stack = [(('AA', 'AA'), 26, 0, frozenset())]
while stack:
    bla = valves, left, released, opened = stack.pop()
    #print(bla)
    if left <= 1 or len(opened) == num_valves:
        most = max(most, released)
        continue

    key = frozenset(valves), opened
    pleft, preleased = visited[key]
    if pleft >= left and preleased >= released:
        continue
    visited[key] = left, released

    first = True
    for valve in [v for v in valves if v is not None]:
        for open in (True, False):
            if open:
                rate = rates[valve]
                if rate == 0 or valve in opened:
                    continue
                if first:
                    left -= 1
                    if left == 0:
                        continue
                first = False
                released += left * rate
                opened = opened.union([valve])
                if len(opened) == num_valves:
                    most = max(most, released)
                    continue

        valve_a, *valve_b = valves
        for tunnel_a in tunnels[valve_a]:
            for tunnel_b in tunnels[valve_b[0]] if valve_b[0] != None else [None]:
                stack.append(((tunnel_a, tunnel_b), left - 1, released, opened))

print(most)
