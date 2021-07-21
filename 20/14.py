import sys

mem = {}
mem1 = {}

def bla(mask, a, b):
    if not 'X' in mask:
        or_mask = int(mask.replace('Y', '0'), 2)
        and_mask = int(mask.replace('Y', '1'), 2)
        #print(f'writing {b} to {a & and_mask | or_mask}')
        mem[a & and_mask | or_mask] = b
        return
    bla(mask.replace('X', '0', 1), a, b)
    bla(mask.replace('X', '1', 1), a, b)

for l in sys.stdin:
    l = l.rstrip('\n')
    if l.startswith('mask = '):
        mask = l[7:]
        or_mask = int(mask.replace('X', '0'), 2)
        and_mask = int(mask.replace('X', '1'), 2)
        float_mask = mask.replace('0', 'Y').replace('1', 'Y')
        continue

    a = int(l[4:l.find(']')])
    b = int(l[l.find('=') + 1:])
    mem1[a] = b & and_mask | or_mask
    bla(float_mask, a | or_mask, b)

print(f'part one: {sum(mem1.values())}')
print(f'part two: {sum(mem.values())}')
