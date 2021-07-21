import sys
from hashlib import md5

passcode = sys.stdin.readline().strip()

def get_ways(path, pos):
    hash = md5((passcode + path).encode()).hexdigest()
    open = list(map(lambda c: c in ('b', 'c', 'd', 'e', 'f'), hash[:4]))
    if pos.imag > 0 and open[0]: yield ('U', -1j)
    if pos.imag < 3 and open[1]: yield ('D', 1j)
    if pos.real > 0 and open[2]: yield ('L', -1)
    if pos.real < 3 and open[3]: yield ('R', 1)

visited = set()
correct = set()

def walk(path = '', pos = 0):
    if pos == 3 + 3j:
        correct.add(path)
        return

    if path in visited:
        return
    visited.add(path)

    for (d, i) in get_ways(path, pos):
        walk(path + d, pos + i)

walk()
k = lambda x: len(x)
print(min(correct, key = k), len(max(correct, key = k)))
