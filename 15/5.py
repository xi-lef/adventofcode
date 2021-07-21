import sys

strings = [l.strip() for l in sys.stdin]

print(sum([(sum([s.count(v) for v in 'aeiou']) >= 3
            and any([c for i, c in enumerate(s[:-1]) if c == s[i + 1]])
            and not any([b in s for b in ['ab', 'cd', 'pq', 'xy']]))
           for s in strings]))

print(sum([(any([s.count(s[i:i + 2]) > 1 for i in range(0, len(s) - 1)])
            and any([s[i] == s[i + 2] for i in range(len(s) - 2)]))
           for s in strings]))
