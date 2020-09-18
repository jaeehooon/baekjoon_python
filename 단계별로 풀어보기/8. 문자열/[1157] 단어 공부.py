import sys


input_str = sys.stdin.readline().rstrip("\n")
value_list = {}

for c in input_str.upper():
    if c in value_list.keys():
        value_list[c] += 1
    else:
        value_list[c] = 1

if (list(value_list.values()).count(max(value_list.values()))) >= 2:
    print("?")
else:
    for key, value in value_list.items():
        if value == max(value_list.values()):
            print(key.upper())
