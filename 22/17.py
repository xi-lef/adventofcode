shapes = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''.split('\n\n')

rocks = []
for shape in shapes:
    rock = set()
    for y, l in enumerate(shape.split()[:: -1]):
        for x, c in enumerate(l):
            if c == '#':
                rock.add(x + 1j * y)
    rocks.append(rock)

pattern = open(0).read().strip()
width = 7
n = 2022
n2 = 1000000000000
highest = index = 0
map = set()
heights = []

def pr():
    s = [list('|' + width * '.' + '|') for _ in range(highest + 3)]
    s.append(list('+' + width * '-' + '+'))
    for r in map:
        s[-int(r.imag + 1)][int(r.real)] = '#'
    print('\n'.join(''.join(l) for l in s))

for step in range(max(n, len(pattern) * len(rocks))):
    #print(f'step {step}'); pr()
    rock = rocks[step % len(rocks)]
    rock = {r + 3 + 1j * (highest + 4) for r in rock}

    while True:
        gas = 1 if pattern[index % len(pattern)] == '>' else -1
        #print(f'gas {gas}, rock {rock}')
        index += 1
        new_rock = {r + gas for r in rock}
        if not any(int(r.real) in (0, width + 1) or r in map for r in new_rock):
            #print('moved by gas')
            rock = new_rock

        new_rock = {r - 1j for r in rock}
        if any(r.imag == 0 or r in map for r in new_rock):
            map.update(rock)
            highest = max(highest, max(int(r.imag) for r in rock))
            break
        rock = new_rock
    heights.append(highest)
print(heights[n - 1])

deltas = [heights[i] - heights[i - 1] for i in range(1, len(heights))]
seq = deltas[-1000 :]
cycles = []
for i in range(len(deltas)):
    if deltas[i : i + len(seq)] == seq:
        cycles.append(i)
#print(cycles)
#print([cycles[i] - cycles[i - 1] for i in range(1, len(cycles))])
cycle_len = cycles[1] - cycles[0]
cycle_height = heights[cycles[1]] - heights[cycles[0]]
#print(cycle_len)

start = cycles[-1]
diff = n2 - start
num_cycles = diff // cycle_len
rest = n2 - (start + num_cycles * cycle_len)
rest_height = heights[cycles[11]] - heights[cycles[11] - rest + 1]
print(heights[start] + num_cycles * cycle_height + rest_height)
