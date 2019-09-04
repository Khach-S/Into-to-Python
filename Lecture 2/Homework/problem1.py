import argparse

import datetime

current_date = datetime.datetime.today()

parser = argparse.ArgumentParser()
parser.add_argument("--num_y", type=int)
parser.add_argument("--num_d", type=int)
args = parser.parse_args()

final = datetime.datetime(current_date.year + args.num_y)

print("Current date: ", current_date)
print("Given years: ", args.num_y)
print("Given days: ", args.num_d)
print("Final date: ", final)