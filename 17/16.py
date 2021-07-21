import sys
from string import ascii_lowercase as alc

moves = sys.stdin.readline().strip().split(',')
n = 16
progs = [alc[i] for i in range(n)]

def dance(progs):
    for move in moves:
        m = move[0]
        if m == 's':
            o = int(move[1:])
            progs = progs[-o:] + progs[:n - o]
        elif m == 'x':
            a, b = map(int, move[1:].split('/'))
            progs[a], progs[b] = progs[b], progs[a]
        else:
            a, b = progs.index(move[1]), progs.index(move[3])
            progs[a], progs[b] = progs[b], progs[a]
    return progs

seen = set()
times = 1000000000
for i in range(times):
    k = tuple(progs)
    if k in seen:
        cycle = i
        break
    seen.add(k)

    progs = dance(progs)
    if i == 0:
        print(''.join(progs))

for i in range(times % cycle):
    progs = dance(progs)

print(''.join(progs))
