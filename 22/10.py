from itertools import count

instrs = iter(l.split() for l in open(0))

crt = [['.' for _ in range(40)] for _ in range(6)]
sum = 0
reg = 1
add = None
for cycle in count(1):
    y, x = divmod(cycle, 40)
    if reg in range(x - 2, x + 1):
        crt[y][x - 1] = '#'

    if (cycle - 20) % 40 == 0:
        sum += cycle * reg

    if add is not None:
        reg += add
        add = None
        continue

    try:
        instr = next(instrs)
    except:
        break
    if instr[0] == 'addx':
        add = int(instr[1])
print(sum)

for l in crt:
    print(''.join(l))
