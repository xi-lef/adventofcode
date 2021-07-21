import sys
from functools import reduce
from itertools import permutations
from operator import mul

nums = [int(x) for x in sys.stdin]
for i in (2, 3):
    print(next(reduce(mul, x) for x in permutations(nums, i) if sum(x) == 2020))
