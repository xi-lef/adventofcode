from collections import defaultdict

algo, img = open(0).read().split('\n\n')
algo = [c == '#' for c in algo.strip()]
assert algo[0] != algo[-1]
orig = defaultdict(lambda: algo[-1],
                   {x + y * 1j: c == '#' for y, l in enumerate(img.split())
                                         for x, c in enumerate(l.strip())})

for r in (2, 50):
    img = orig.copy()
    for i in range(r):
        nimg = defaultdict(lambda: i % 2 == algo[0])
        xmin = int(min(x.real for x in img.keys()))
        xmax = int(max(x.real for x in img.keys()))
        ymin = int(min(x.imag for x in img.keys()))
        ymax = int(max(x.imag for x in img.keys()))
        for x in range(xmin - 1, xmax + 2):
            for y in range(ymin - 1, ymax + 2):
                s = [img[x + dx + y * 1j + dy] for dy in (-1j, 0, 1j)
                                               for dx in (-1, 0, 1)]
                s = int(''.join('1' if x else '0' for x in s), 2)
                nimg[x + y * 1j] = algo[s]
        img = nimg
    print(sum(img.values()))

# TODO doesnt work for sample lol
