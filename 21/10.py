lines = [l.strip() for l in open(0)]

score1 = 0
scores2 = []
for l in lines:
    s = []
    for c in l:
        if c in '([{<':
            s.append({'(': ')', '[': ']', '{': '}', '<': '>'}[c])
        elif s.pop() != c:
            score1 += {')': 3, ']': 57, '}': 1197, '>': 25137}[c]
            break
    else:
        tmp = 0
        for c in s[:: -1]:
            tmp *= 5
            tmp += {')': 1, ']': 2, '}': 3, '>': 4}[c]
        scores2.append(tmp)

print(score1)
print(sorted(scores2)[len(scores2) // 2])
