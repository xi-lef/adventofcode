s = s2 = 0
for l in open(0):
    a = 'ABC'.index(l[0])
    b = 'XYZ'.index(l[2])

    s += b + 1
    if a == b:
        s += 3
    elif b == (a + 1) % 3:
        s += 6

    s2 += b * 3
    #if b == 0:
    #    m = (a - 1) % 3
    #elif b == 1:
    #    m = a
    #else:
    #    m = (a + 1) % 3
    #s2 += m + 1
    s2 += (a + b - 1) % 3 + 1
print(s)
print(s2)
