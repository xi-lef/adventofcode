import sys
from functools import lru_cache
from hashlib import md5
from itertools import count

salt = sys.stdin.readline().strip()

@lru_cache(maxsize = None)
def get_hash(i, stretch = 1):
    h = salt + str(i)
    for _ in range(stretch):
        h = md5(h.encode()).hexdigest().lower()
    return h

@lru_cache(maxsize = None)
def in_row(s, n):
    return [s[i] for i in range(len(s) - n + 1) if len(set(s[i:i + n])) == 1]

for stretch in (1, 2017):
    keys = 0
    cur = [in_row(get_hash(i, stretch), 5) for i in range(1, 1001)]
    for i in count():
        r = in_row(get_hash(i, stretch), 3)
        if r and any(r[0] in x for x in cur):
            keys += 1

        cur[i % 1000] = in_row(get_hash(i + 1001, stretch), 5)

        if keys == 64:
            break
    print(i)
