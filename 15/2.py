import sys

lines = [x.strip().split('x') for x in sys.stdin]

paper = 0
ribbon = 0
for line in lines:
    l, w, h = [int(x) for x in line]
    a = l * w
    b = w * h
    c = h * l
    paper += 2 * (a + b + c) + min(a, b, c)
    ribbon += 2 * (l + h + w - max(l, h, w)) + l * w * h
print(paper, ribbon)
