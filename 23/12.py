import itertools
rows = []
for l in open(0):
    a, b = l.strip().split()
    b = [int(x) for x in b.split(',')]
    rows.append((a, b))
print(rows)


def is_valid(row, numbers):
    return all(
        len(r) == n
        for r, n in itertools.zip_longest(
            (s for s in row.split(".") if s), numbers, fillvalue = ''
        )
    )

#print(is_valid('#.#.###', [1,1,3]))
print(is_valid('.#....#...###.', [1,1,3]))

def solve(row, numbers):
    if '?' not in row:
        return is_valid(row, numbers)

    a = row.replace('?', '.', 1)
    b = row.replace('?', '#', 1)
    #print(a, b)
    return solve(a, numbers) + solve(b, numbers)

print(sum(solve(r, n) for (r, n) in rows))
