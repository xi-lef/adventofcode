import sys

line = [int(x) for x in sys.stdin.readline().split(',')]

def bla(n):
    nums = {x: i for i, x in enumerate(line[:-1], start = 1)}
    last = line[-1]
    for i in range(len(nums) + 1, n):
        #if last not in nums:
        #    nums[last] = i
        #    last = 0
        #else:
        #    a = nums[last]
        #    nums[last] = i
        #    last = i - a
        nums[last], last = i, i - nums[last] if last in nums else 0

    return last

for i in (2020, 30000000):
    print(f'{i}th: {bla(i)}')
