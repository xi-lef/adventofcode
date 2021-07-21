import fileinput

t = dict()
for line in fileinput.input():
    words = line.split(' ')
    bag = ' '.join(words[0:2])
    p = ' '.join(words[4:]).split(',')
    if 'no other bags' in line:
        others = []
    else:
        others = [' '.join(x.lstrip().split(' ')[0:3]) for x in p]
    t.setdefault(bag, set()).update(others)

def has(k):
    v = [' '.join(x.split(' ')[1:3]) for x in t[k]]
    return 'shiny gold' in v or any(has(x) for x in v)

print(f'part one: {sum(map(has, t))}')

def count(k):
    sum = 0
    for e in t[k]:
        words = e.split(' ')
        c = int(words[0])
        sum += c + c * count(' '.join(words[1:3]))
    return sum

print(f'part two: {count("shiny gold")}')
