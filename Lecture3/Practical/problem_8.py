import sys

set1 = {1, 7, 8, 'Python', False}
print(set1)

print("Argumenst: ", str(sys.argv[1:]))
x = sys.argv[1:]
set1.update(x)
print(set1)