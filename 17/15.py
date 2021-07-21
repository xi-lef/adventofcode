import sys

a = int(sys.stdin.readline().split()[-1])
b = int(sys.stdin.readline().split()[-1])
fa, fb = 16807, 48271

def gen(s, f, m):
    while True:
        s = s * f % 2147483647
        if m == 1 or s % m == 0:
            yield s

for r, ma, mb in ((40000000, 1, 1), (5000000, 4, 8)):
    gen_a = gen(a, fa, ma)
    gen_b = gen(b, fb, mb)
    #print(sum(1 for _ in range(r) if next(gen_a) & 0xffff == next(gen_b) & 0xffff))
    c = 0
    for _ in range(r):
        x = next(gen_a)
        y = next(gen_b)
        if x & 0xffff == y & 0xffff:
            c += 1
    print(c)
