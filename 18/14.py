import sys

sinput = sys.stdin.readline().strip()
input = int(sinput)

recipes = [3, 7]
e1, e2 = 0, 1
n = len(str(input))

while True:
    r1 = recipes[e1]
    r2 = recipes[e2]
    s = r1 + r2

    if s >= 10:
        recipes.append(s // 10)
    recipes.append(s % 10)

    if sinput in ''.join(str(x) for x in recipes[-n - 1:]):
        break

    e1 = (e1 + 1 + r1) % len(recipes)
    e2 = (e2 + 1 + r2) % len(recipes)

print(''.join(str(x) for x in recipes[input:input + 10]))
print(''.join(str(x) for x in recipes).index(sinput))
