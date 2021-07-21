import sys

w1 = sys.stdin.readline().split(',')
w2 = sys.stdin.readline().split(',')

X = {}
path = {}

def walk(w, mark):
    pos = 0
    total = 1
    for i in w:
        d, v = i[0], int(i[1:])
        while v > 0:
            if d == 'R':
                pos += 1
            elif d == 'L':
                pos -= 1
            elif d == 'U':
                pos += 1j
            elif d == 'D':
                pos -= 1j
            if mark:
                path[pos] = total
            else:
                if pos in path: #and pos not in X:
                    X[pos] = total
            v -= 1
            total += 1

walk(w1, True)
walk(w2, False)
print(min([int(abs(x.real) + abs(x.imag)) for x in X]))
print(min(X[k] + path[k] for k in X))
