import sys
from collections import deque

line = sys.stdin.readline().split()
players = int(line[0])
turns = int(line[-2])

def play(turns):
    circle = deque([0])
    scores = [0] * players
    #cur = 0
    for t in range(turns + 1):
        #print(circle)
        #size = len(circle)
        marble = t + 1

        if marble % 23 == 0:
            #rm = (cur - 7) % size
            #scores[t % players] += marble + circle[rm]
            #del circle[rm]
            #cur = (rm) % size
            circle.rotate(7)
            scores[t % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            #new = (cur + 1) % size + 1
            #circle.insert(new, marble)
            #cur = new
            circle.rotate(-1)
            circle.append(marble)
    return scores

print(max(play(turns)))
print(max(play(turns * 100)))
