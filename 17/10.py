import sys
from functools import reduce
from more_itertools import grouper
from operator import xor


def knot_round(lengths, rounds = 1):
    circle = list(range(256))
    size = len(circle)
    cur = skip = 0
    for _ in range(rounds):
        for l in lengths:
            rev = [circle[i % size] for i in range(cur, cur + l)]
            rev.reverse()

            for i in range(l):
                circle[(cur + i) % size] = rev[i]

            cur = (cur + l + skip) % size
            skip += 1
    return circle


def dense(sparse):
    dense = [reduce(xor, g) for g in grouper(sparse, 16)]
    return ''.join([hex(v)[2:].zfill(2) for v in dense])


def knot_hash(input):
    sparse = knot_round([ord(c) for c in input] + [17, 31, 73, 47, 23], 64)
    return dense(sparse)


if __name__ == '__main__':
    input = sys.stdin.readline().strip()

    c = knot_round([int(x) for x in input.split(',')])
    print(c[0] * c[1])
    print(knot_hash(input))
