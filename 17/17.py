import sys

steps = int(sys.stdin.readline())

buffer = [0]
cur = 0
for i in range(1, 2018):
    cur = (cur + steps) % len(buffer) + 1
    buffer.insert(cur, i)
print(buffer[buffer.index(2017) + 1])

cur = target = 0
for i in range(1, 50000001):
    cur = (cur + steps) % i + 1
    if cur == 1:
        target = i
print(target)
