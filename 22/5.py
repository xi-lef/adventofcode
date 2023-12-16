import re
from copy import deepcopy

start, instrs = open(0).read().split('\n\n')

stacks = {}
for stack in list(zip(*start.split('\n')))[1 : -1 : 4]:
    num = int(stack[-1])
    stacks[num] = [x for x in stack[: -1] if not x.isspace()]
stacks2 = deepcopy(stacks)

for instr in instrs.splitlines():
    n, src, dest = (int(x) for x in re.findall(r'\d+', instr))

    stacks[dest] = stacks[src][n - 1 :: -1] + stacks[dest]
    stacks2[dest] = stacks2[src][: n] + stacks2[dest]
    del stacks[src][: n]
    del stacks2[src][: n]

for stack in (stacks, stacks2):
    print(''.join(s[0] for s in stack.values()))
