import itertools
import sys
from hashlib import md5

key = sys.stdin.readline().strip()

pw1 = ''
pw2 = [''] * 8
for i in itertools.count(0):
    if (hash := md5((key + str(i)).encode()).hexdigest()).startswith('0' * 5):
        if len(pw1) < 8:
            pw1 += hash[5]
        if (a := int(hash[5], 16)) in range(8) and pw2[a] == '':
            pw2[a] = hash[6]

        if len(pw1) == len(''.join(pw2)) == 8:
            break
print(pw1, ''.join(pw2))
