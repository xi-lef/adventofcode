lines = [[int(x) for x in l.split()] for l in open(0)]

part1 = part2 = 0
for line in lines:
    sequences = [line]
    while not all(x == 0 for x in sequences[-1]):
        s = sequences[-1]
        sequences.append([s[i] - s[i - 1] for i in range(1, len(s))])
    part1 += sum(s[-1] for s in sequences)
    part2 += sequences[0][0] + (sum(-s[0] for s in sequences[1 :: 2]) +
                                sum( s[0] for s in sequences[2 :: 2]))
print(part1)
print(part2)
