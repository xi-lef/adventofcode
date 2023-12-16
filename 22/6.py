line = open(0).read().strip()

for d in (4, 14):
    for i in range(d, len(line) + 1):
        if len(set(line[i - d : i])) == d:
            print(i)
            break
