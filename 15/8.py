import sys

lines = [l.strip() for l in sys.stdin]

mem = 0
enc = 0
for l in lines:
    i = 1
    enc += 6
    while i < len(l) - 1:
        c = l[i]
        if c == '\\':
            if l[i + 1] == 'x':
                enc += 4
                i += 3
            else:
                enc += 3
                i += 1
        mem += 1
        enc += 1
        i += 1

orig = sum(len(l) for l in lines)
print(orig - mem)
print(enc - orig)
