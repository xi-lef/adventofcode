import sys

poly = list(sys.stdin.readline().strip())

def react(poly):
    check = lambda a, b: a != b and a.lower() == b.lower()
    new = []
    for c in poly:
        if new and check(c, new[-1]):
            new.pop(-1)
        else:
            new.append(c)
    return new

after = react(poly)
m = len(after)
print(m)

for c in set([c.lower() for c in after]):
    cur = [a for a in after if c != a != c.upper()]
    m = min(m, len(react(cur)))
print(m)
