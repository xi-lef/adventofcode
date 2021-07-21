import sys

l = [l.strip().split(': ') for l in sys.stdin]
fw = {int(d): int(r) for d, r in l}

def get_sev(offset = 0):
    sev = caught = 0
    for d, r in fw.items():
        if (d + offset) % (2 * r - 2) == 0:
            caught = True
            sev += d * r
    return sev, caught

print(get_sev()[0])

o = 0
while get_sev(o)[1]:
    o += 1
print(o)
