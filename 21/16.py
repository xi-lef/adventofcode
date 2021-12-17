from math import prod

msg = bin(int(open(0).read().strip(), 16))[2 :]
msg = msg.zfill(((len(msg) + 4 - 1) // 4) * 4)

versions = 0
def parse(packet):
    global versions
    o = 0
    version = int(packet[o : o + 3], 2)
    o += 3
    versions += version
    packet_type = int(packet[o : o + 3], 2)
    o += 3

    if packet_type == 4:
        val = ''
        while True:
            grp = packet[o : o + 5]
            o += 5
            val += grp[1 :]
            if grp[0] == '0':
                return o, int(val, 2)

    length_type = int(packet[o])
    o += 1
    vals = []
    if length_type == 0:
        length = int(packet[o : o + 15], 2)
        o += 15
        sub = packet[o : o + length]
        while sub:
            off, val = parse(sub)
            vals.append(val)
            sub = sub[off :]
        o += length
    else:
        amount = int(packet[o : o + 11], 2)
        o += 11
        for _ in range(amount):
            off, val = parse(packet[o :])
            vals.append(val)
            o += off

    func = {0: sum, 1: prod, 2: min, 3: max,
            5: lambda t: t[0] > t[1], 6: lambda t: t[0] < t[1],
            7: lambda t: t[0] == t[1]}[packet_type]
    return o, func(vals)

result = parse(msg)[1]
print(versions)
print(result)
