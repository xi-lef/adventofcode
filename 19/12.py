import math
import sys

moons = []
for l in sys.stdin:
    moons.append([int(e.split('=')[1]) for e in l.strip()[1:-1].split(',')])

def sim(pos, steps):
    vel = [[0, 0, 0] for _ in range(len(pos))]

    for _ in range(steps):
        for p, v in zip(pos, vel):
            for o in pos:
                for i in range(len(p)):
                    if p[i] > o[i]:
                        v[i] -= 1
                    elif p[i] < o[i]:
                        v[i] += 1

        for p, v in zip(pos, vel):
            for i in range(len(p)):
                p[i] += v[i]

    return pos, vel

pos, vel = sim([m[:] for m in moons], 1000)
print(sum([sum([abs(v) for v in p]) * sum([abs(v) for v in vel[i]]) for i, p in enumerate(pos)]))

cycles = []
for i in range(3):
    c = 0
    initial_pos = [p[i] for p in moons]
    initial_vel= [0 for _ in range(len(pos))]
    pos = [m[i] for m in moons]
    vel = initial_vel[:]

    while True:
        for j in range(len(pos)):
            for o in pos:
                if pos[j] > o:
                    vel[j] -= 1
                elif pos[j] < o:
                    vel[j] += 1

        for j in range(len(pos)):
            pos[j] += vel[j]

        c += 1
        if pos == initial_pos and vel == initial_vel:
            break
    cycles.append(c)

print(math.lcm(*cycles))
