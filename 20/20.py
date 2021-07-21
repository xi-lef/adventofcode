from collections import Counter, defaultdict
import math
import sys

tiles = {}
num = 0
tile = []
for l in sys.stdin:
    l = l.rstrip('\n')
    if l.startswith('Tile'):
        num = int(l[5:9])
        continue
    if not l:
        tiles[num] = tile
        tile = []
        continue
    tile.append(l)

borders = {}
for num, lines in tiles.items():
    l = ''
    r = ''
    for line in lines:
        l += line[0]
        r += line[-1]
    borders[num] = [lines[0], l, r, lines[-1]]

border_to_id = defaultdict(list)
border_counter = Counter()
for id, bs in borders.items():
    for b in bs:
        x = b[::-1] if b[::-1] in border_counter else b
        border_to_id[x].append(id)
        border_to_id[x[::-1]].append(id)

        border_counter.update([x])
#print(border_counter)

uniqs_per_tile = Counter()
for b, c in border_counter.items():
    if c == 1:
        uniqs_per_tile.update(border_to_id[b])
#print(uniqs_per_tile)

corners = [id for id, c in uniqs_per_tile.items() if c == 2]
#print(corners)
print(math.prod(corners))

# rotate right
def rotate(tile, amount):
    for _ in range(amount):
        tile = list(zip(*tile[::-1]))
    return [''.join(row) for row in tile]

def flipx(tile): return tile[::-1]
def flipy(tile): return [row[::-1] for row in tile]

def left_side(tile):   return ''.join([row[0] for row in tile])
def right_side(tile):  return ''.join([row[-1] for row in tile])
def top_side(tile):    return tile[0]
def bottom_side(tile): return tile[-1]

start = flipy(rotate(tiles[corners[0]], 2)) # TODO
n = int(math.sqrt(len(borders)))
ids = [corners[0]]
image = [start]

while len(image) != len(tiles):
    if len(image) % n == 0:
        prev_i = -n
        get_prev = bottom_side
        get_next = top_side
    else:
        prev_i = -1
        get_prev = right_side
        get_next = left_side

    prev_side = get_prev(image[prev_i])
    a, b = border_to_id[prev_side]
    next_id = a if a != ids[prev_i] else b
    ids.append(next_id)
    next = tiles[next_id]

    for i in range(4):
        rot = rotate(next, i)
        if get_next(rot) == prev_side:
            image.append(rot)
            break
        rot = flipx(rot)
        if get_next(rot) == prev_side:
            image.append(rot)
            break

#print(image)
cropped = [[line[1:-1] for line in tile[1:-1]] for tile in image]
#print(cropped)

final = ['' for _ in range(n * 8)]
for i, tile in enumerate(cropped):
    for j, line in enumerate(tile):
        final[j + i // n * 8] += (line)
#print('\n'.join(final))

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]

def count_monsters(image):
    count = 0
    for line in range(len(image) - 2):
        cur = image[line: line + 3]
        for start in range(len(cur[0]) - len(monster[0])):
            bad = False
            for i, l in enumerate(cur):
                for j, c in enumerate(l[start:start + len(monster[0])]):
                    if monster[i][j] == '#' != c:
                        bad = True
            if not bad:
                count += 1
    return count

m = 0
for i in range(4):
    rot = rotate(final, i)
    m = max(m, count_monsters(rot))
    m = max(m, count_monsters(flipx(rot)))
#print(m)
print(''.join(final).count('#') - m * ''.join(monster).count('#'))
