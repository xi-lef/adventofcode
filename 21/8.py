lines = [[p.split() for p in l.split('|')] for l in open(0)]

print(len([o for _, os in lines for o in os if len(o) in (2, 4, 3, 7)]))

def patterns_by_len(patterns, n):
    return list(set(p) for p in patterns if len(p) == n)

sum = 0
for patterns, outputs in lines:
    m = {}
    m[1] = patterns_by_len(patterns, 2)[0]
    m[7] = patterns_by_len(patterns, 3)[0]
    m[4] = patterns_by_len(patterns, 4)[0]
    m[8] = patterns_by_len(patterns, 7)[0]

    n069 = patterns_by_len(patterns, 6)
    m[9] = next(n for n in n069 if not (m[8] - n) & m[4])
    m[0] = next(n for n in n069 if not (m[8] - n) & m[7] and n != m[9])
    m[6] = next(n for n in n069 if n not in m.values())

    n235 = patterns_by_len(patterns, 5)
    m[3] = next(n for n in n235 if not (m[8] - n) & m[1])
    m[2] = next(n for n in n235 if len((m[8] - n) & m[4]) == 2)
    m[5] = next(n for n in n235 if n not in m.values())

    m = {''.join(sorted(v)): str(k) for k, v in m.items()}
    sum += int(''.join(m[''.join(sorted(i))] for i in outputs))
print(sum)
