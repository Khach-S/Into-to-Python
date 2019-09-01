import sys

set2 = {True, 20, 'hello', 7, 8}

input_arg = set(sys.argv[1:])

set2_new = set2 - input_arg

print(set2)
print(set2_new)