import sys
from collections import defaultdict, Counter

lines = [l.strip() for l in sys.stdin]
lines.sort()

id = 0
times = defaultdict(list)
for l in lines:
    if '#' in l:
        id = int(l[l.index('#') + 1:-13])
    elif 'asleep' in l:
        sleep = int(l[l.index(':') + 1:-14])
    elif 'wakes' in l:
        wake = int(l[l.index(':') + 1:-10])
        times[id].append((sleep, wake))
#print(times)

total = {}
for id, ranges in times.items():
    total[id] = sum(r[1] - r[0] for r in ranges)
#print(total)

most = sorted(total.items(), key = lambda kv: kv[1])[-1][0]
#print(most)

minutes = defaultdict(Counter)
for id in total:
    for r in times[id]:
        m = list(range(*r))
        minutes[id].update(m)

print(most * minutes[most].most_common(1)[0][0])

max = 0
for id, m in minutes.items():
    minute, times = m.most_common(1)[0]
    if times > max:
        max = times
        max_m = minute
        max_id = id
print(max_id * max_m)
