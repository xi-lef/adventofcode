from collections import Counter
import sys

w, h = 25, 6
#w, h = 2, 2
n = w * h

pixels = sys.stdin.readline().strip('\n')
layers = []
counts = []

for i in range(0, len(pixels), n):
    layers.append(l := pixels[i:i + n])
    counts.append(Counter(l))

#print(counts)
a = min(counts, key = lambda f: f['0'])
print(a['1'] * a['2'])

image = ['2'] * n

for l in layers:
    for i, v in enumerate(l):
        if image[i] == '2':
            image[i] = v

for i in range(0, n, w):
    print(''.join(image[i: i + w]).replace('0', ' '))
