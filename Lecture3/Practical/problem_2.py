import sys

list1 = ["hello", 1, True]
print("List 1: ", list1)

new_list = list1.copy()

print("Arguments: ", str(sys.argv[1:]))

new_list.extend(sys.argv[1:])

print("New list: ", new_list)
