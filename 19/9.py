from intcode import *

program = get_program()
print(next(run(program, iter([1]))))
print(next(run(program, iter([2]))))
