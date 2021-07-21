import re
import string
import sys

lines = []
for l in sys.stdin:
    l = l.rstrip('\n')
    lines.append(l)

def apply(a, op, b):
    if op == '': return b
    elif op == '+': return a + b
    else: return a * b

def find_end(s):
    depth = 1
    for j, d in enumerate(s):
        if d == '(':
            depth += 1
        elif d == ')':
            depth -= 1
            if depth == 0:
                return j
    return 0

def fix(s):
    prev = ''
    res = ''
    op = ''
    i = 0
    while i < len(s):
        c = s[i]
        if c == '(':
            i += 1
            end = find_end(s[i:])
            bla = fix(s[i: i + end])
            if not prev:
                prev = f'({bla})'
            else:
                new = prev + op + '(' + bla + ')'
                if op == '+':
                    prev = f'({new})'
                else:
                    prev = new
            i += end
        elif c in ['+', '*']:
            op = c
            if op == '*':
                res += prev + op
                prev = ''
        elif c in string.digits:
            if not prev:
                prev = c
            else:
                new = prev + op + c
                if op == '+':
                    prev = f'({new})'
                else:
                    prev = new
        # ignore ' ' and ')'
        i += 1
    return res + prev

def solve(s):
    res = 0
    op = ''
    i = 0
    while i < len(s):
        c = s[i]
        if c == '(':
            i += 1
            end = find_end(s[i:])
            res = apply(res, op, solve(s[i:i + end]))
            i += end
        elif c in ['+', '*']:
            op = c
        elif c in string.digits:
            res = apply(res, op, int(c))
        # ignore ' ' and ')'
        i += 1

    #print(f's: {s}, res: {res}')
    return res

count = 0
count2 = 0
for l in lines:
    count += solve(l)
    #print(fix(l))
    count2 += solve(fix(l))

#print(count)
#print(count2)

class bla(int):
    def __init__(self, x): self.x = x
    def __add__(self, y): return bla(self.x + y)
    def __sub__(self, y): return bla(self.x * y)
    def __mul__(self, y): return bla(self.x + y)

xd = 0
xd2 = 0
for l in lines:
    new = re.sub(r'(\d+)', r'bla(\1)', l.replace('*', '-'))
    #print(new)
    xd += eval(new, {'bla': bla})
    xd2 += eval(new.replace('+', '*'), {'bla': bla})
print(xd)
print(xd2)
