import sys

line = sys.stdin.readline().strip()

group = total = trash = i = 0
while i < len(line):
    c = line[i]

    if c == '{':
        group += 1
    elif c == '}':
        total += group
        group -= 1
    elif c == '<':
        i += 1
        while line[i] != '>':
            escaped = line[i] == '!'
            trash += not escaped
            i += 1 + escaped
    i += 1

print(total, trash)
