import sys

line = sys.stdin.readline().strip()

def bla(line):
    count1 = count2 = i = 0
    while i < len(line):
        c = line[i]
        if c == '(':
            x = i + line[i:].index('x')
            end = i + line[i:].index(')')
            num = int(line[i + 1:x])
            rep = int(line[x + 1:end])

            count1 += rep * num
            count2 += rep * bla(line[end + 1:end + 1 + num])[1]

            i = end + num
        else:
            count1 += 1
            count2 += 1
        i += 1

    return count1, count2

print(*bla(line))
