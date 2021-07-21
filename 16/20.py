import sys
from itertools import count

blacklist = [tuple(map(int, l.split('-'))) for l in sys.stdin]
blacklist.sort()

#for i in count():
#    if not any(a <= i <= b for a, b in blacklist):
#        print(i)
#        break

i = 0
first = True
valid = 2 ** 32
for a, b in blacklist:
    if i < a and first:
        print(i)
        first = False

    diff = b - max(a, i) + 1
    valid -= max(0, diff)
    i = max(i, b + 1)
print(valid)
