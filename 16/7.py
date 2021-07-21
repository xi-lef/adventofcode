import sys

ips = [l.strip() for l in sys.stdin]

valid = set()
inside = False
for ip in ips:
    for i in range(len(ip) - 3):
        c = ip[i:i + 4]
        if c[0] == '[':
            inside = True
            continue
        elif c[0] == ']':
            inside = False
            continue

        if c[0] == c[3] != c[1] == c[2]:
            if not inside:
                valid.add(ip)
            else:
                valid.discard(ip)
                break
print(len(valid))

count = 0
inside = False
for ip in ips:
    aba_out = set()
    aba_in = set()
    for i in range(len(ip) - 2):
        c = ip[i:i + 3]
        if c[0] == '[':
            inside = True
            continue
        elif c[0] == ']':
            inside = False
            continue

        if c[0] == c[2] != c[1]:
            if inside:
                aba_in.add(c)
            else:
                aba_out.add(c)

    for aba in aba_out:
        if aba[1] + aba[0] + aba[1] in aba_in:
            count += 1
            break
print(count)
