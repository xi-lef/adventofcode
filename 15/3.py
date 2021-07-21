import sys

line = sys.stdin.readline().strip()
dir = {'^': 1j, 'v': -1j, '>': 1, '<': -1}

def walk(way):
    pos = 0
    x = set()
    for c in way:
        x.add(pos)
        pos += dir[c]
    return x

print(len(walk(line)))
print(len(walk(line[::2]) | walk(line[1::2])))
