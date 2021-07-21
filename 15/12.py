import json
import sys

count = 0
def parse_int(s):
    i = int(s)
    global count
    count += i
    return i

input = sys.stdin.readline().strip()
json.loads(input, parse_int = parse_int)
print(count)

def parse_obj(o):
    if 'red' in o.values():
        return {}
    return o

j = json.loads(input, object_hook = parse_obj)
count = 0
json.loads(str(j).replace("'", '"'), parse_int = parse_int)
print(count)

#new = ''
#i = 0
#stack = []
#while i < len(input):
#    c = input[i]
#    if c in ('[', '{'):
#        stack.append((c, len(new)))
#    elif c in (']', '}'):
#        stack.pop()
#
#    if input[i:].startswith('"red"') and stack[-1][0] == '{':
#        _, start = stack.pop()
#        new = new[:start] + '{}'
#
#        depth = 1
#        while depth != 0:
#            i += 1
#            depth += input[i] == '{'
#            depth -= input[i] == '}'
#    else:
#        new += c
#    i += 1
#
#count = 0
#json.loads(new, parse_int = parse_int)
#print(count)
