import sys
from intcode import *
from more_itertools import powerset

prog = get_program()

#for c in run(prog, (ord(c) for s in sys.stdin for c in s)):
#    print(chr(c), end = '')

input = []
vm = run(prog, input)


def recv():
    s = ''
    for c in vm:
        s += chr(c)
        if s.endswith('Command?\n'):
            break
    #print('received:', s)
    return s

def send(msg):
    #print('sending:', msg)
    input.extend(ord(c) for c in msg)
    input.append(ord('\n'))
    return recv()


def solve(inv, ways):
    for comb in powerset(inv):
        drop = inv - set(comb)
        for item in drop:
            send(f'drop {item}')

        msg = send(ways[0])
        if 'typing' in msg:
            print(msg.split('typing ')[1].split()[0])
            exit()

        for item in drop:
            send(f'take {item}')
    assert False


def walk(finish = False, init = None, last = None):
    bad_items = {'escape pod', 'giant electromagnet', 'infinite loop', 'photons', 'molten lava'}
    rev = {'north': 'south', 'south': 'north', 'west': 'east', 'east': 'west'}

    msg = init if init else recv()
    lines = [l.strip() for l in msg.strip().split('\n')]

    try:
        s = lines.index('Items here:')
        e = lines.index('', s)
        items = [i.lstrip('- ') for i in lines[s + 1 : e]]
        for item in items:
            if item in bad_items:
                continue
            send(f'take {item}')
    except:
        pass

    s = lines.index('Doors here lead:')
    e = lines.index('', s)
    ways = [w.lstrip('- ') for w in lines[s + 1 : e]]
    if last:
        ways = [w for w in ways if w != rev[last]]

    if finish and 'pressure-sensitive' in msg:
        msg = send('inv')
        lines = [l.strip() for l in msg.strip().split('\n')]
        inv = {l.lstrip('- ') for l in lines[1 : lines.index('')]}
        solve(inv, ways)

    for way in ways:
        msg = send(way)
        walk(finish, msg, way)
        msg = send(rev[way])
    return msg


walk(True, walk())
