import sys

input = [int(x) for x in sys.stdin.readline().strip()]
first = input[0]
cupsdict = {}
for i in range(len(input)):
    cupsdict[input[i]] = input[(i + 1) % len(input)]

def strfy(cups, start = 1):
    bla = []
    i = cups[start]
    while i != start:
        bla.append(str(i))
        i = cups[i]
    return ''.join(bla)


def play(cups, moves):
    cur = first
    m = max(cups.keys())
    for i in range(moves):
        #print('move', i + 1, strfy(cups, cur), 'cur', cur)
        a = cups[cur]
        b = cups[a]
        c = cups[b]
        cups[cur] = cups[c]

        dest = cur
        while dest in [cur, a, b, c]:
            dest -= 1
            if dest == 0:
                dest = m

        cups[dest], cups[c] = a, cups[dest]

        cur = cups[cur]

    return cups

cups1 = play(cupsdict.copy(), 100)
print(strfy(cups1))

numcups = 10 ** 6
d2 = cupsdict.copy()
i = len(d2)
while i != numcups:
    i += 1
    d2[i] = i + 1
d2[input[-1]] = 10
d2[numcups] = first
cups2 = play(d2, 10 ** 7)
a = cups2[1]
b = cups2[a]
print(a, b, a * b)
