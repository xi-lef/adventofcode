import sys

sys.stdin.readline()
sys.stdin.readline()
nodes = {}
max_x = 0
for l in sys.stdin:
    n, s, u, a, _ = l.split()
    _, x, y = n.split('-')

    x, y = map(lambda x: int(x[1:]), [x, y])
    max_x = max(max_x, x)
    s, u, a = map(lambda x: int(x[:-1]), [s, u, a])

    n = (x, y)
    if u == 0:
        free = n
    nodes[n] = (u, a)

pairs = 0
for an, (au, aa) in nodes.items():
    for bn, (bu, ba) in nodes.items():
        if an == bn:
            continue
        if au > 0 and au <= ba:
            pairs += 1
print(pairs)

# 37,  0: goal
# 34, 26: free
#  8, 24: rightmost opening
# (26 + 2) + (29 - 1 + 24) + 37 * 5 - 4 = 261 :D
max_u = max(u for u, _ in nodes.values())
wall_y = next(y for (_, y), (u, _) in nodes.items() if u == max_u)
wall_x = next(x for x in range(max_x) if nodes[x, wall_y][0] > max_u // 2)
open_x = wall_x - 1
steps = (free[0] - open_x        # move free node to the first open spot next to the wall
         + free[1]               # move free node to y = 0
         + max_x - 1 - open_x    # move free node to max_x - 1
         + (max_x - 1) * 5 + 1)  # move goal to free node; move free node left of goal (5 steps)
                                 # until goal is at x = 0 (max_x - 1 times, 1 for last goal to free)
print(steps)
