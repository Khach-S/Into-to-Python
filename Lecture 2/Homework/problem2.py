import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="odd length string, longer than 7", type=str)
args = parser.parse_args()

old_str = args.str

str_length = len(args.str)

first_part_length = int((str_length - 3) / 2)
last_part_length = first_part_length
middle_part = args.str[str_length // 2 - 1:str_length//2 + 2]
middle_part_uppercased = middle_part.upper()
first_part = args.str[:first_part_length]
last_part = args.str[int(first_part_length) + 3:]
new_str = first_part + middle_part_uppercased + last_part

print("The old string: ", old_str)
print("Middle 3 characters: ", middle_part_uppercased)
print("The new string: ", new_str)