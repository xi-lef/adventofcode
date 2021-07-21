import sys

rules = {}
for l in sys.stdin:
    l = l.rstrip('\n')
    if not l:
        break
    num, rule = l.split(':')
    num = int(num)
    if '"' in rule:
        rules[num] = rule[2]
    else:
        rules[num] = [[int(x.strip()) for x in possibility.strip().split(' ')]
                      for possibility in rule.split('|')]

#print(rules)
msgs = [l.rstrip('\n') for l in sys.stdin]

def check(msg, match = [0]):
    empty = (len(msg) == 0) + (len(match) == 0)
    if empty > 0:
        return empty == 2

    next = rules[match[0]]
    if type(next) == str:
        if msg[0] != next:
            return False
        else:
            return check(msg[1:], match[1:])

    return any(check(msg, poss + match[1:]) for poss in next)

c = 0
for msg in msgs:
    if check(msg):
        c += 1
print(c)

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

c = 0
for msg in msgs:
    c += check(msg)
print(c)

#def bla(rule, stop = False):
#    #print(rule)
#    if rule not in rules:
#        return set(rule), set(), set()
#
#    l = set()
#    rec = set()
#    end = set()
#    for poss in rules[rule]:
#        cur = {''}
#        past = False
#        for part in poss:
#            if stop and part == rule:
#                past = True
#                end = cur
#                continue
#            hm, rec, _ = bla(part, part == rule)
#            if past:
#                end = set(c + a for c in end for a in hm)
#            else:
#                cur = set(c + a for c in cur for a in hm)
#        l.update(cur)
#    if stop:
#        rec = l
#    return l, rec, end

#all = set(bla(0)[0])
#print('all', all)
#rules[8] = [[42], [42, 8]]
#rules[11] = [[42, 31], [42, 11, 31]]
#s8, rec8, end8 = bla(8)
#s11, rec11, end11 = bla(11)
#print(s8, rec8, end8)
#print(s11, rec11, end11)

#c = c2 = 0
#n = set()
#for msg in msgs:
#    if msg in all: c += 1
#        continue
#
#    for si, rec, end in [(s8, rec8, end8), (s11, rec11, end11)]:
#        for s in si:
#            if msg.startswith(s):
#                i = len(s)
#                while i < len(msg):
#                    hit = False
#                    for e in rec:
#                        if msg[i:].startswith(e):
#                            i += len(e)
#                            hit = True
#                            break
#                    if not hit:
#                        break
#                else:
#                    c2 += 1
#                    n.add(msg)
#                    break
#                if msg[i:] in end:
#                    n.add(msg)
#                    c2 += 1
#
#print(c, c2)
#print(n)
