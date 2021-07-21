import sys

l = sys.stdin.readline().strip('\n')

print(l.count('(') - l.count(')'))

f = 0
for i, b in enumerate(l, start = 1):
    f += 1 if b == '(' else -1
    if f == -1:
        print(i)
        break
