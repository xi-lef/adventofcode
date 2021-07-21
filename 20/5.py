import sys

ids = []
for line in sys.stdin:
    a, b = 0, 128

    place = []
    for p in (line[0:7], line[7:10]):
        for c in p:
            if c in ['F', 'L']:
                b -= (b - a) // 2
            else:
                a += (b - a) // 2
        place.append(a)
        a, b = 0, 8

    ids.append(place[0] * 8 + place[1])

ids.sort()
print(ids[-1])
for i in range(len(ids) - 1):
    if ids[i] + 1 != ids[i + 1]:
        print(ids[i] + 1)
