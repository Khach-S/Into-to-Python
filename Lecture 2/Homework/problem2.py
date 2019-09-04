import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", help="odd length string, longer than 7", type=str)
args = parser.parse_args()

old_str = args.str

str_length = len(args.str)
middle = args.str[str_length % 2 - 1:str_length%2 + 2]
new_str = old_str.upper(middle)

print("The old string: ", old_str)
print("Middle 3 characters: ", middle)
print("The new string: ", new_str)