from collections import defaultdict

lines = [l.strip() for l in open(0).readlines()]

schematic = defaultdict(lambda: '.')
for y, l in enumerate(lines):
    for x, c in enumerate(l):
        schematic[x + y * 1j] = c

max_x = len(lines[0])
max_y = len(lines)
skip = False
score = 0
for y in range(max_y):
    for x in range(max_x):
        k = x + y * 1j
        if not schematic[k].isdigit() or (skip and schematic[k - 1].isdigit()):
            continue
        skip = False

        for dy in (-1j, 0, 1j):
            for dx in (-1, 0, 1):
                neighbor = schematic[k + dx + dy]
                if neighbor.isdigit() or neighbor == '.':
                    continue

                # neighbor is a symbol -> find start and end of number
                l = lines[y]
                x_end = x
                while (x_end < len(l) and l[x_end].isdigit()):
                    x_end += 1
                while (x > 0 and l[x - 1].isdigit()):
                    x -= 1
                score += int(l[x : x_end])
                skip = True
                break
            else:
                continue
            break
print(score)

score = 0
for y in range(max_y):
    for x in range(max_x):
        k = x + y * 1j
        if schematic[k] != '*':
            continue

        skip = False
        numbers = []
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                neighbor = schematic[k + dx + dy * 1j]
                if not neighbor.isdigit():
                    skip = False
                    continue
                if skip:
                    continue
                skip = True

                l = lines[y + dy]
                x_start = x + dx
                x_end = x_start
                while (x_end < len(l) and l[x_end].isdigit()):
                    x_end += 1
                while (x_start > 0 and l[x_start - 1].isdigit()):
                    x_start -= 1
                numbers.append(int(l[x_start : x_end]))
            skip = False
        if len(numbers) == 2:
            score += numbers[0] * numbers[1]
print(score)
