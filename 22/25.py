sum = 0
for line in open(0):
    num = 0
    for i, c in enumerate(line.strip()[:: -1]):
        match c:
            case '=': d = -2
            case '-': d = -1
            case _: d = int(c)
        num += d * (5 ** i)
    sum += num

snafu = []
while sum > 0:
    sum, r = divmod(sum, 5)
    if r <= 2:
        snafu.append(str(r))
    else:
        snafu.append('=' if r == 3 else '-')
        sum += 1
print(''.join(snafu[:: -1]))
