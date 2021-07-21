import copy
import sys

lines = [l.split() for l in sys.stdin]

def exec(lines):
    visited = set()
    ip = 0
    acc = 0
    while ip < len(lines) and ip not in visited:
        visited.add(ip)

        l = lines[ip]
        if l[0] == 'nop':
            ip += 1
        elif l[0] == 'jmp':
            ip += int(l[1])
        else: # acc
            acc += int(l[1])
            ip += 1

    return acc, ip == len(lines)

print(exec(lines)[0])

for i in range(len(lines)):
    l = lines[i]
    if l[0] == 'acc':
        continue

    cp = copy.deepcopy(lines)
    cp[i][0] = 'jmp' if l[0] == 'nop' else 'nop'
    acc, term = exec(cp)
    if term:
        print(acc)
        break
