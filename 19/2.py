import sys

l = list(map(int, sys.stdin.readline().split(',')))

def bla(l):
    for i in range(0, len(l), 4):
        p = l[i]
        if p == 99:
            break
        a = l[l[i + 1]]
        b = l[l[i + 2]]
        c = l[i + 3]
        r = a + b if p == 1 else a * b
        l[c] = r
    return l[0]

print(bla([l[0], 12, 2, *l[3:]]))

for i in range(100):
    for j in range(100):
        if bla([l[0], i, j, *l[3:]]) == 19690720:
            print(100 * i + j)
            exit()
