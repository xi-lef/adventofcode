from operator import add, truediv as div, mul, sub, gt, lt

monkeys = {}

for line in open(0):
    monkey, *rest = line.split()
    if len(rest) == 1:
        val = int(*rest)
    else:
        val = [{'+': add, '-': sub, '*': mul, '/': div}[rest[1]], rest[0], rest[2]]
    monkeys[monkey[: -1]] = val

def solve(m):
    monkey = monkeys[m]
    if isinstance(monkey, int):
        return monkey

    op, a, b = monkey
    return op(solve(a), solve(b))

print(int(solve('root')))

def binsearch(op):
    L = 0
    R = int(1e30)
    while L <= R:
        m = (L + R) // 2
        monkeys['humn'] = m
        res = solve('root')
        if res == 0:
            print(m)
            break
        elif op(res, 0):
            L = m + 1
        else:
            R = m + 1

monkeys['root'][0] = sub
binsearch(gt)
binsearch(lt)
