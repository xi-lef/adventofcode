import re
from copy import deepcopy
from dataclasses import dataclass
from functools import reduce
from operator import add, mul, pow
from typing import Callable

@dataclass
class Monkey:
    items: list[int]
    op: Callable
    const: int
    test: int
    true: int
    false: int

input = [m.splitlines() for m in open(0).read().split('\n\n')]

monkeys : list[Monkey] = [None for _ in range(len(input))]
for m in input:
    num = int(*re.findall(r'\d+', m[0]))
    items = [int(x) for x in re.findall(r'\d+', m[1])]
    op = {'+': add, '*': mul}[m[2].split()[-2]]
    const = m[2].split()[-1]
    if const == 'old':
        op = pow
        const = 2
    else:
        const = int(const)
    test = int(m[3].split()[-1])
    true = int(m[4].split()[-1])
    false = int(m[5].split()[-1])

    monkeys[num] = Monkey(items, op, const, test, true, false)

lcm = reduce(mul, (m.test for m in monkeys))

for rounds, div in ((20, 3), (10000, 1)):
    inspected = [0 for _ in range(len(monkeys))]
    monkeys_ = deepcopy(monkeys)

    for round in range(rounds):
        for i, monkey in enumerate(monkeys_):
            for item in monkey.items:
                inspected[i] += 1
                item = monkey.op(item, monkey.const) // div % lcm
                if item % monkey.test == 0:
                    next = monkey.true
                else:
                    next = monkey.false
                monkeys_[next].items.append(item)
            monkey.items = []

    inspected.sort()
    print(inspected[-1] * inspected[-2])
