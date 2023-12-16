from collections import defaultdict

steps = open(0).read().strip().split(',')

part1 = 0
boxes = defaultdict(dict)
for step in steps:
    operation = '=' if '=' in step else '-'
    label = step.split(operation)[0]
    label, _, focal = step.partition(operation)

    box_no = hash = 0
    for c in step:
        if c == operation:
            box_no = hash
        hash = (hash + ord(c)) * 17 % 256
    part1 += hash

    box = boxes[box_no]
    if operation == '-':
        box.pop(label, None)
    else: # '='
        box[label] = int(focal)
print(part1)

part2 = 0
for box_no, box in boxes.items():
    # insertion order is kept, so the order is correct
    for pos, focal in enumerate(box.values(), start = 1):
        part2 += (box_no + 1) * pos * focal
print(part2)
