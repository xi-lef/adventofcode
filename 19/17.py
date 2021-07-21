from intcode import *
from random import randint

prog = get_program()

out = ''.join([chr(a) for a in run(prog)]).splitlines()
del out[-1]

scafs = set()
pos = dir = 0
for y, r in enumerate(out):
    for x, c in enumerate(r):
        p = y * 1j + x
        if c == '#':
            scafs.add(p)
        elif c != '.':
            pos = p
            dir = {'^': -1j, 'v': 1j, '>': 1, '<': -1}[c]

total = 0
for s in scafs:
    if all(s + d in scafs for d in (-1j, 1j, -1, 1)):
        total += int(s.real * s.imag)
print(total)

if pos + dir in scafs:
    path = ''
elif pos + dir * 1j in scafs:
    path = 'R,'
    dir *= 1j
elif pos + dir * -1j in scafs:
    path = 'L,'
    dir *= -1j
else:
    path = 'R,R,'
    dir *= -1

while True:
    c = 0
    while pos + dir in scafs:
        c += 1
        pos += dir
    path += str(c) + ','

    if pos + dir * 1j in scafs:
        path += 'R,'
        dir *= 1j
    elif pos + dir * -1j in scafs:
        path += 'L,'
        dir *= -1j
    else:
        path = path.removesuffix(',')
        #path = path[: -1]
        break

def rnd(s = None):
    m = 10
    a = s if s else randint(0, len(path) - m)
    b = randint(a + m, a + 20)
    return path[a : b]

while True:
    A = rnd(0)
    B = rnd()
    C = rnd()

    rem = path
    main = ''
    while rem:
        rem = rem.removeprefix(',')
        #if rem[0] == ',':
        #    rem = rem[1 :]

        for c in ('A', 'B', 'C'):
            p = globals()[c]
            if rem.startswith(p):
                rem = rem.removeprefix(p)
                #rem = rem[len(p) :]
                main += c + ','
                break
        else:
            break
    else:
        main = main.removesuffix(',')
        #main = main[: -1]
        if len(main) <= 20:
            break

#print(f'{A=} {B=} {C=} {main=}')
A = A.removesuffix(',')
B = B.removesuffix(',')
C = C.removesuffix(',')
#if A[-1] == ',': A = A[: -1]
#if B[-1] == ',': B = B[: -1]
#if C[-1] == ',': C = C[: -1]

#A = 'R,6,L,6,R,12'
#B = 'L,6,R,12,L,4,L,6'
#C = 'L,6,L,10,L,10,R,6'
#main = 'B,A,A,C,B,A,C,B,A,C'

prog[0] = 2
input = iter(ord(c) for c in '\n'.join([main, A , B, C, 'n\n']))
out = list(run(prog, input))
#print(''.join([chr(i) for i in out]))
print(out[-1])
