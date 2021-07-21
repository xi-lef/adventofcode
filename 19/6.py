import sys

l = [l.strip().split(')') for l in sys.stdin.readlines()]
d = {b: a for a, b in l}

c = 0
for k in d:
    while k in d:
        c += 1
        k = d[k]
print(c)

me = []
k = 'YOU'
while k in d:
    k = d[k]
    me.append(k)
santa = []
k = 'SAN'
while k in d:
    k = d[k]
    santa.append(k)

for o in me:
    for p in santa:
        if o == p:
            common = o
            break
    else:
        continue
    break

print(me.index(common) + santa.index(common))
