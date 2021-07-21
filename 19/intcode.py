import sys
from collections import defaultdict


def get_program():
    return list(map(int, sys.stdin.readline().split(',')))


def run(mem, input = None):
    ADD, MUL, IN, OUT, JNZ, JZ, SLT, SEQ, RBO = list(range(1, 10))
    OP_SIZE = [0, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    END = 99

    rel_base = 0
    pc = 0
    mem = defaultdict(int, enumerate(mem))
    in_counter = 0
    if isinstance(input, list):
        orig = input
        input = iter(input)

    while True:
        cur = mem[pc]
        mode, op = divmod(cur, 100)
        if op == END:
            return

        size = OP_SIZE[op]
        args = [mem[pc + i] for i in range(1, size)]
        modes = [(mode // 10 ** i) % 10 for i in range(3)]
        # pos = 0, imm = 1, rel = 2
        reads = [(mem[x], x, mem[rel_base + x])[m] for x, m in zip(args, modes)]
        writes = [(x, None, rel_base + x)[m] for x, m in zip(args, modes)]

        pc += size

        if op in (ADD, MUL):
            a, b = reads[0:2]
            mem[writes[2]] = a + b if (op == ADD) else a * b
        elif op == IN:
            try:
                n = next(input)
                in_counter += 1
            except StopIteration:
                n = -1 # day 23 expects this
                yield -1 # give control back to caller
                input = iter(orig[in_counter:])
            mem[writes[0]] = n
        elif op == OUT:
            yield reads[0]
        elif op in (JNZ, JZ):
            a = reads[0]

            if op == JNZ and a != 0 or op == JZ and a == 0:
                pc = reads[1]
        elif op in (SLT, SEQ):
            a, b = reads[0:2]
            mem[writes[2]] = op == SLT and a < b or op == SEQ and a == b
        elif op == RBO:
            rel_base += reads[0]
        else:
            print('unimplemented instruction', op, 'at', pc - size, ':', op, args, modes)
            break
