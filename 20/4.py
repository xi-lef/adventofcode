import sys
from itertools import chain
from string import hexdigits

cur = {}
passports = []
for l in chain(sys.stdin, ' '):
    l = l.strip()
    if not l:
        passports.append(cur)
        cur = {}
        continue

    for e in l.split():
        a, b = e.split(':')
        if a != 'cid':
            cur[a] = b

p1 = p2 = 0
for pp in passports:
    if len(pp) < 7:
        continue
    p1 += 1

    if not (1920 <= int(pp['byr']) <= 2002
            and 2010 <= int(pp['iyr']) <= 2020
            and 2020 <= int(pp['eyr']) <= 2030):
        continue

    hgt = pp['hgt']
    cm = hgt.endswith('cm')
    if not (cm or hgt.endswith('in')):
        continue
    hgt = int(hgt[:max(hgt.find('cm'), hgt.find('in'))])
    if not (cm and (150 <= hgt <= 193) or not cm and (59 <= hgt <= 76)):
        continue

    hcl = pp['hcl']
    if hcl[0] != '#' or len(hcl) != 7 or not all(c in hexdigits for c in hcl[1:]):
        continue

    if pp['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        continue

    pid = pp['pid']
    if len(pid) != 9 or not pid.isdecimal():
        continue

    p2 += 1

print(p1, p2)
