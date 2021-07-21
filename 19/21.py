from intcode import *

prog = get_program()

# (!A | !B | !C) & D = !(A & B & C) & D
part1 = '''OR A J
AND B J
AND C J
NOT J J
AND D J
WALK
'''

# !(A & B & C) & D & (H | (E & I)) | !A
part2 = '''OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
AND I T
OR H T
AND T J
NOT A T
OR T J
RUN
'''

# !(A & B & C) & D & (E | H)
part2 = '''OR A J
AND B J
AND C J
NOT J J
AND D J
OR E T
OR H T
AND T J
RUN
'''

for input in (part1, part2):
    out = list(run(prog, (ord(c) for c in input)))
    if out[-1] < 256:
        print(''.join(chr(i) for i in out if i < 256))
    else:
        print(out[-1])
