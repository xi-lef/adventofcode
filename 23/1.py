import re

lines = [l.strip() for l in open(0)]

score = 0
for l in lines:
    m = re.findall(r'\d', l)
    score += int(m[0] + m[-1])
print(score)

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
wordsnums = words.copy()
wordsnums.extend(str(i) for i in range(1, 10))
score = 0
for l in lines:
    def bla(r):
        for i in r:
            for w in wordsnums:
                if l[i :].startswith(w):
                    return w if w not in words else str(words.index(w) + 1)
        raise Exception()
    a = bla(range(len(l)))
    b = bla(range(len(l) - 1, -1, -1))

#    m = re.findall('|'.join([r'\d', *(f'(?=(?:{w}))' for w in words)]), l)
#    a, b = m[0], m[-1]
    score += int(a + b)
print(score)
