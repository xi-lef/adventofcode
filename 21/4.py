import sys
from more_itertools import grouper

numbers = [int(x) for x in sys.stdin.readline().strip().split(',')]
sys.stdin.readline()

boards = []
for l in grouper(sys.stdin, 6):
    boards.append([[int(x) for x in r.strip().split()] for r in l if r and r != '\n'])
num = len(boards)

for n in numbers:
    for i, b in enumerate(boards):
        b[:] = [[None if x == n else x for x in r] for r in b]
        for ways in (b, zip(*b)):
            for r in ways:
                if r.count(None) == 5:
                    if sum(1 for b in boards if b) in (1, num):
                        print(n * sum(x for r in b for x in r if x))
                    b[:] = []
