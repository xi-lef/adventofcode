# Advent of Code

Solutions for all years; written in Python 3.

## Usage

All solutions expect the input via `stdin`. If the input is, for example, in a file called `1`,
getting the solution is as simple as one of the following:

```shell
python 1.py < 1
pypy3 1.py < 1
```

The solution will be output on `stdout` on two separate lines, for part 1 and part 2 respectively.

For most days, PyPy is faster than CPython---however, if PyPy does not work (e.g., due to
usage of `@cache`), CPython is at least as fast as PyPy.
