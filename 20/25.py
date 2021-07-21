import sys

pk_card = int(sys.stdin.readline())
pk_door = int(sys.stdin.readline())

val = 1
def trans(num):
    global val
    val = val * num % 20201227
    return val

for i in range(12):
    bla = trans(17807724)
    print(i, bla)

val = 1
i = 1
while True:
    if trans(7) == pk_card:
        ls_card = i
        break
    i += 1
print('loop size card', ls_card)

val = 1
for i in range(ls_card):
    bla = trans(pk_door)
print(bla)
