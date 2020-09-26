import sys


croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cro = sorted(croatia_alphabet, key=len, reverse=True)

input_string = sys.stdin.readline().rstrip('\n')
for c in cro:
    if c in input_string:
        input_string = input_string.replace(c, '_')

print(len(input_string))
