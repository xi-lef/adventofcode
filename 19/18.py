from collections import deque

start = 0
vault = set()
keys = {}
doors = {}

for y, l in enumerate(open(0)):
    for x, c in enumerate(l):
        p = x + y * 1j
        if c == '@':
            start = p
            vault.add(p)
        elif c == '.':
            vault.add(p)
        elif c.islower():
            keys[p] = c
            vault.add(p)
        elif c.isupper():
            doors[p] = c.lower()

def bfs(vault, start, keys):
    visited = set()
    stack = deque([(start, frozenset(), 0)])
    while stack:
        p, k, s = stack.popleft()
        if (p, k) in visited:
            continue
        visited.add((p, k))

        if p in keys:
            k = k | frozenset(keys[p])

        if len(k) == len(keys):
            return s

        for d in (1, -1, 1j, -1j):
            n = p + d
            # completely ignoring doors also works for part 2...
            if n in vault or (n in doors and (doors[n] in k or doors[n] not in keys.values())):
                stack.append((n, k, s + 1))

print(bfs(vault, start, keys))

for d in (0, 1, -1, 1j, -1j):
    vault.remove(start + d)
vaults = [{f for f in vault if f.real < start.real and f.imag < start.imag},
          {f for f in vault if f.real > start.real and f.imag < start.imag},
          {f for f in vault if f.real < start.real and f.imag > start.imag},
          {f for f in vault if f.real > start.real and f.imag > start.imag}]
starts = (start - 1 - 1j, start + 1 - 1j, start - 1 + 1j, start + 1 + 1j)
keys_per_vault = [{k: c for k, c in keys.items() if k in vault} for vault in vaults]

print(sum(bfs(v, s, k) for v, s, k in zip(vaults, starts, keys_per_vault)))
