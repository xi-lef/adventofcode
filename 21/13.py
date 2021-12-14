dots, folds = open(0).read().split('\n\n')
dots = {tuple(map(int, d.split(','))) for d in dots.split()}
folds = [f.strip().split()[-1].split('=') for f in folds.strip().split('\n')]

first = True
for axis, v in folds:
    v = int(v)
    ndots = {d for d in dots if axis == 'x' and d[0] < v
                             or axis == 'y' and d[1] < v}
    for x, y in dots - ndots:
        ndots.add((x if axis == 'y' else v - (x - v),
                   y if axis == 'x' else v - (y - v)))
    dots = ndots

    if first:
        first = False
        print(len(dots))

mx = max(x for x, _ in dots) + 1
my = max(y for _, y in dots) + 1
out = [['#' if (x, y) in dots else ' ' for x in range(mx)] for y in range(my)]
print('\n'.join(''.join(l) for l in out))
