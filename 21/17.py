import re

xmin, xmax, ymin, ymax = map(int, re.findall(r'-?\d+', open(0).read()))
assert ymin < 0 and ymax < 0

def lands(xvel, yvel):
    x = y = Y = 0
    while x <= xmax and y >= ymin:
        if x >= xmin and y <= ymax:
            return True, Y
        x += xvel
        y += yvel
        Y = max(Y, y)
        xvel = max(0, xvel - 1)
        yvel -= 1
    return False, Y

for xvel in range(xmin):
    if xmin <= sum(range(xvel + 1)) <= xmax:
        for yvel in range(-ymin, 0, -1):
            l, Y = lands(xvel, yvel)
            if l:
                print(Y)
                break
        break

print(sum(lands(xvel, yvel)[0] for xvel in range(xmax + 1)
                               for yvel in range(ymin, -ymin)))
