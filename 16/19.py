import sys
from collections import deque

num = int(sys.stdin.readline())

#circle = {i: (i + 1) % num for i in range(num)}
#while len(circle) > 1:
#    for e in list(circle.keys())[:: 2]:
#        n = circle[e]
#        circle[e] = circle[n]
#        del circle[n]
#print(next(iter(circle.keys())) + 1)

#circle = {i: (i + 1) % num for i in range(num)}
#cur = 0
#while circle[cur] != cur:
#    circle[cur], cur = circle[circle[cur]], circle[cur]
#print(cur + 1)

b = bin(num)[2 :]
print(int(b[1 :] + b[0], 2))

circle = {i for i in range(1, num + 1)}
elves = deque(range(1, num + 1))
elves.rotate(-(num // 2))
while len(circle) > 1:
    for e in list(circle):
        if e not in circle:
            continue

        n = elves.popleft()
        circle.remove(n)

        if len(circle) % 2 == 0:
            elves.rotate(-1)
print(next(iter(circle)))
