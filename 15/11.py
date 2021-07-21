import sys
from collections import Counter

pw = sys.stdin.readline().strip()

def inc(pw):
    a = ord('a')
    z = ord('z')
    next = [ord(c) for c in pw[::-1]]
    for i, c in enumerate(next):
        if c == z:
            next[i] = a
        else:
            next[i] = c + 1
            break
    return ''.join(chr(c) for c in next[::-1])

def next_pw(pw):
    while True:
        pw = inc(pw)
        ords = [ord(c) for c in pw]
        if not any(ords[i] + 2 == ords[i + 1] + 1 == ords[i + 2] for i in range(len(pw) - 2)):
            continue

        if any(c in pw for c in ('i', 'l', 'o')):
            continue

        pairs = i = 0
        while i < len(pw) - 1:
            if pw[i] == pw[i + 1]:
                pairs += 1
                i += 1
            i += 1
        if pairs != 2:
            continue
        return pw

pw = next_pw(pw)
print(pw)
pw = next_pw(pw)
print(pw)
