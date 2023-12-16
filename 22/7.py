cwd = root = {}

for line in open(0):
    match line.split():
        case '$', 'cd', '/': cwd = root
        case '$', 'cd', c: cwd = cwd[c]
        case '$', 'ls': pass
        case 'dir', name: cwd[name] = {'..': cwd}
        case size, name: cwd[name] = int(size)

part1 = 0
part2 = 1e99

def size(dir, need = 1e99):
    global part1, part2
    total = 0
    for k, v in dir.items():
        if isinstance(v, int):
            total += v
        elif k != '..':
            total += size(v, need)

    if total <= 100000:
        part1 += total
    if total >= need:
        part2 = min(part2, total)
    return total

total = size(root)
print(part1)

need = 30000000 - (70000000 - total)
size(root, need)
print(part2)
