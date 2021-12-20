import re
from copy import deepcopy
from functools import reduce
from itertools import permutations

def magnitude(num):
    if isinstance(num, int):
        return num
    else:
        return 3 * magnitude(num[0]) + 2 * magnitude(num[1])

def explode2(num):
    s = str(num)
    d = 0
    for i, c in enumerate(s):
        if c == '[': d += 1
        elif c == ']': d -= 1
        if d == 5:
            start = i
            break
    else:
        return num

    end = s.find(']', start)
    l, r = map(int, re.findall(r'\d+', s[start : end]))
    nl_end = start
    while not s[nl_end].isdigit():
        nl_end -= 1
        if nl_end < 0:
            break
    else:
        nl_start = nl_end
        while s[nl_start - 1].isdigit():
            nl_start -= 1
        old = int(s[nl_start : nl_end + 1])
        new = old + l
        s = s[: nl_start] + str(new) + s[nl_end + 1 :]
        if len(str(new)) > len(str(old)):
            start += 1
            end += 1

    nr_start = end
    while not s[nr_start].isdigit():
        nr_start += 1
        if nr_start == len(s):
            break
    else:
        nr_end = nr_start
        while s[nr_end + 1].isdigit():
            nr_end += 1
        s = s[: nr_start] + str(int(s[nr_start : nr_end + 1]) + r) + s[nr_end + 1 :]
    return eval(s[: start] + '0' + s[end + 1 :])

def explode(num):
    s = str(num)
    d = 0
    idx = []
    second = False
    for c in s:
        if c == '[':
            d += 1
            idx.append(int(second))
            second = False
        elif c == ']':
            d -= 1
            idx.pop()
        elif c == ',':
            second = True
        if d == 5:
            break
    else:
        return False, num
    idx.pop(0)  # initial 0 because of initial '['

    n = num
    for i in idx[: -1]:
        n = n[i]
    l, r = n[idx[-1]]
    n[idx[-1]] = 0

    for pos, val in ((1, l), (0, r)):
        for p, i in enumerate(idx[:: -1]):
            if i == pos:
                n = num
                for i in idx[: -(p + 1)]:
                    n = n[i]

                if isinstance(n[not pos], int):
                    n[not pos] += val
                    break
                n = n[not pos]
                while not isinstance(n[pos], int):
                    n = n[pos]
                n[pos] += val
                break

    return True, num

def split(num):
    if isinstance(num, int):
        return False, num
    for i in (0, 1):
        n = num[i]
        if isinstance(n, int) and n > 9:
            num[i] = [n // 2, n // 2 + n % 2]
            return True, num
        b, _ = split(n)
        if b:
            return True, num
    return False, num

def add(a, b):
    num = [a, b]
    while True:
        change, num = explode(num)
        if change: continue
        change, num = split(num)
        if change: continue
        break
    return num

nums = [eval(l) for l in open(0)]
orig = deepcopy(nums)
num = reduce(add, nums[1 :], nums[0])
print(magnitude(num))

m = 0
for a, b in permutations(orig, 2):
    m = max(m, magnitude(add(deepcopy(a), deepcopy(b))))
print(m)
