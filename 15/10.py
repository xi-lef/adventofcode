import sys
from itertools import groupby

nums = [int(x) for x in list(sys.stdin.readline().strip())]

def do(nums, iter):
    for _ in range(iter):
        #print(''.join([str(x) for x in nums]))
        new = []
        cur = nums[0]
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == cur:
                i += 1
                count += 1
            new.extend([count, cur])
            cur = nums[i % len(nums)]
        nums = new
    return nums

#def do(nums, iter):
#    for _ in range(iter):
#        nums = [x for k, g in groupby(nums) for x in (len(list(g)), k)]
#    return nums

print(len(do(nums, 40)))
print(len(do(nums, 50)))
