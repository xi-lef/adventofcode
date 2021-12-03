import re
import sys

ls = [re.match(r'(\w+) (\d+)', l).groups() for l in sys.stdin]
ls = [(a, int(b)) for a, b in ls]

x = d = d2 = 0
for l in ls:
    match l:
        case 'forward', a:
            x += a
            d2 += d * a
        case 'down', a:
            d += a
        case 'up', a:
            d -= a
print(x * d)
print(x * d2)
