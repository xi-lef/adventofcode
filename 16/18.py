import sys

input = sys.stdin.readline().strip()

for r in (40, 400000):
    l = input
    c = 0
    for _ in range(r):
        c += l.count('.')
        l = '.' + l + '.'
        #new = ''
        #for i in range(1, len(l) - 1):
        #    #if l[i - 1 : i + 2] in ('^^.', '.^^', '^..', '..^'):
        #    #if (l[i - 1] == '^') ^ (l[i + 1] == '^'):
        #    if l[i - 1] != l[i + 1]:
        #        new += '^'
        #    else:
        #        new += '.'
        #l = new
        l = ''.join(['^' if l[i - 1] != l[i + 1] else '.' for i in range(1, len(l) - 1)])
    print(c)
