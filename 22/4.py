import re

s = s2 = 0
for l in open(0):
    a, b, c, d = (int(x) for x in re.findall(r'\d+', l))
    s += c >= a and d <= b or a >= c and b <= d
    s2 += a <= d and b >= c
print(s)
print(s2)
