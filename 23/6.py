from functools import reduce
from operator import mul

times, distances = open(0).readlines()
times = [int(x) for x in times.split()[1 :]]
distances = [int(x) for x in distances.split()[1 :]]

num_ways = []
for (time, distance) in zip(times, distances):
    ways = 0
    for hold in range(1, time):
        if (time - hold) * hold > distance:
            ways += 1
    num_ways.append(ways)
print(reduce(mul, num_ways))

time2 = int(''.join(str(x) for x in times))
distance2 = int(''.join(str(x) for x in distances))

start = 0
for hold in range(1, time2):
    traveled = (time2 - hold) * hold
    if traveled > distance2:
        start = hold
        break

end = 0
for hold in range(time2 - 1, start, -1):
    traveled = (time2 - hold) * hold
    if traveled <= distance2:
        end = hold + 1
        break
print(start, end, end - start)

num_ways = 0
first = True
for hold in range(1, time2):
    if (time2 - hold) * hold > distance2:
        if num_ways == 0:
            print('start', hold)
        num_ways += 1
    elif num_ways > 0 and first:
        print('end', hold)
        first = False
print(num_ways)
# TODO
