lines = open(0).readlines()

def mix(key, times):
    numbers = [int(x) * key for x in lines]

    size = len(numbers)
    indices = list(range(size))
    for i in list(range(size)) * times:
        val = numbers[i]
        idx = indices.index(i)
        #print('\nmove value', val, 'at index', idx)
        #print('indices', indices)
        #print([numbers[j] for j in indices])

        ni = (idx + val + 0) % (size - 1)
        #if ni == 0: ni = size

        indices.remove(i)
        indices.insert(ni, i)

    #print([numbers[i] for i in indices])

    i = indices.index(numbers.index(0))
    return sum(numbers[indices[(i + o) % size]] for o in (1000, 2000, 3000))

print(mix(1, 1))
print(mix(811589153, 10))
