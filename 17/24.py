import sys

comps = {tuple(map(int, l.split('/'))) for l in sys.stdin}

longest = mlongest = 0
def build(bridge, last):
    m = sum(sum(c) for c in bridge)
    l = len(bridge)
    global longest, mlongest
    if l >= longest:
        longest = l
        mlongest = max(mlongest, m)

    for c in (c for c in comps - bridge if last in c):
        m = max(m, build(bridge | {c}, c[0] if c[1] == last else c[1]))
    return m

print(build(set(), 0))
print(mlongest) # TODO wrong with python3.8+
