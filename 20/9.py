import sys

lines = []
for l in sys.stdin:
    lines.append(int(l.rstrip('\n')))

invalid = 0
for i in range(25, len(lines)):
    found = False
    for j in range(i - 25, i):
        for k in range(j, i):
            if lines[j] + lines[k] == lines[i]:
                found = True
    if not found:
        invalid = lines[i]

print(f'invalid number: {invalid}')

a = 0
b = 1
s = sum(lines[a:b])

while True:
    if s == invalid:
        break
    elif s < invalid:
        s += lines[b]
        b += 1
    elif s > invalid:
        s -= lines[a]
        a += 1
    if b > len(lines):
        print('hm')
        break

r = lines[a:b]
print(f'weakness: {min(r) + max(r)}')
