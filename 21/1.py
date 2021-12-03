import sys

vals = [int(l) for l in sys.stdin]
print(sum(a < b for a, b in zip(vals, vals[1 :])))
print(sum(a < b for a, b in zip(vals, vals[3 :])))
#print(sum(sum(vals[i : i + 3]) < sum(vals[i + 1 : i + 4]) for i in range(len(vals) - 3)))
