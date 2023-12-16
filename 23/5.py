seeds, *maps = open(0).read().split("\n\n")
seeds = [int(x) for x in seeds.split(":")[1].split()]
maps = [
    sorted(
        [tuple(int(x) for x in l.split()) for l in map.splitlines()[1:]],
        key=lambda t: t[1],
    )
    for map in maps
]

locations = []
for seed in seeds:
    for map in maps:
        for dst_start, src_start, n in map:
            if src_start <= seed < src_start + n:
                seed = seed - src_start + dst_start
                break
    locations.append(seed)
print(min(locations))

def solve(seed_ranges):
    for map in maps:
        new_seed_ranges = []
        while seed_ranges:
            seed_start, seed_n = seed_ranges.pop(0)
            prev_src_end = 0
            for dst_start, src_start, n in map:
                if prev_src_end <= seed_start < src_start:
                    # seed_start is not in any mapping -> ID-map it
                    new_n = src_start - seed_start
                    new_seed_ranges.append((seed_start, new_n))
                    seed_ranges.append((src_start, seed_n - new_n))
                    break

                src_end = src_start + n
                if src_start <= seed_start < src_end:
                    # add mapped range to next ranges
                    new_start = seed_start - src_start + dst_start
                    new_n = min(seed_n, src_end - seed_start)
                    new_seed_ranges.append((new_start, new_n))

                    if new_n < seed_n:
                        # add unmapped range to current ranges
                        seed_ranges.append((src_end, seed_n - new_n))
                    break
                prev_src_end = src_end
            else: # no mapping found
                new_seed_ranges.append((seed_start, seed_n))
        seed_ranges = new_seed_ranges

    return min(s[0] for s in seed_ranges)

print(solve([(s, 1) for s in seeds]))
print(solve([(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]))
