from hashlib import md5
import itertools
import sys

key = sys.stdin.readline().strip()

for i in itertools.count(0):
    if md5((key + str(i)).encode()).hexdigest().startswith('0' * 5):
        print(i)
        break
for i in itertools.count(0):
    if md5((key + str(i)).encode()).hexdigest().startswith('0' * 6):
        print(i)
        break
