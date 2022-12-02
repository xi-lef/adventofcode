inv = []
s = 0
for l in open(0):
    if l.isspace():
        inv.append(s);
        s = 0
    else:
        s += int(l)

inv.sort()
print(inv[-1])
print(sum(inv[-1:-4:-1]))
