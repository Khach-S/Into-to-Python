import argparse

import datetime

current = datetime.datetime.today()
final = datetime.datetime()

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type = int)
parser.add_argument("--num_d", type = int)
args = parser.parse_args()

final = current + args.num_y

print("Current date: ", current)
print("Given years: ", args.num_y)
print("Given days: ", args.num_d)
print("Final date: ", final)