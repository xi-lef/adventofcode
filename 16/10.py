import sys
from collections import defaultdict

lines = [l.split() for l in sys.stdin]
init = [l for l in lines if len(l) == 6]
moves = [l for l in lines if len(l) > 6]

bots = defaultdict(list)
for i in init:
    bots[int(i[-1])].append(int(i[1]))
outputs = defaultdict(list)

i = 0
while i < len(moves):
    m = moves[i]
    src = int(m[1])
    if len(bots[src]) < 2:
        i += 1
        continue
    del moves[i]
    i = 0

    dst_lo = int(m[6])
    bot_lo = m[5] == 'bot'
    dst_hi = int(m[-1])
    bot_hi = m[-2] == 'bot'

    #print(bots)
    #print(m)
    l, h = sorted(bots[src])
    if l == 17 and h == 61:
        print(src)
    bots[src].clear()

    target_lo = bots if bot_lo else outputs
    target_hi = bots if bot_hi else outputs
    target_lo[dst_lo].append(l)
    target_hi[dst_hi].append(h)

print(outputs[0][0] * outputs[1][0] * outputs[2][0])
