from intcode import *

l = get_program()

print(list(run(l[:], iter([1]))))
print(next(run(l[:], iter([5]))))
