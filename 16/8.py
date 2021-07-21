from collections import defaultdict
import matplotlib.pyplot as plt
import sys

w, h = 50, 6
screen = defaultdict(int)
for l in (l.strip().split() for l in sys.stdin):
    new = screen.copy()
    if l[0] == 'rect':
        a, b = l[1].split('x')
        for x in range(int(a)):
            for y in range(int(b)):
                new[x, y] = 1
    else: # column
        col = int(l[2].split('=')[1])
        val = int(l[4])
        if l[1] == 'row':
            for i in range(w):
                new[i, col] = screen[(i - val) % w, col]
        else:
            for i in range(h):
                new[col, i] = screen[col, (i - val) % h]
    screen = new
print(sum(screen.values()))

on = [k for k, v in screen.items() if v == 1]
X = [x for x, _ in on]
Y = [h - y for _, y in on]
plt.scatter(X, Y)
plt.show()
