import sys

r, c = map(int, sys.stdin.readline().strip()[: -1].split('row ')[1].split(', column '))
num = sum(range(r)) + sum(range(r + 1, r + c))
#num = sum(range(r + c)) - r

code = 20151125
for _ in range(num):
    code = code * 252533 % 33554393
print(code)
