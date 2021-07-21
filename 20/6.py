import sys
import string

count = 0
q = set(string.ascii_lowercase)
#q = set()
for line in sys.stdin:
    line = line.rstrip('\n')
    if not line:
        count += len(q)
        #q.clear()
        q = set(string.ascii_lowercase)
        continue
    #q.update([c for c in line])
    q.intersection_update([c for c in line])

print(count)
