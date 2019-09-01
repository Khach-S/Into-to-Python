import argparse

dict1 = {2 : 'value 2' , 5 : 'value 5'}

parser = argparse.ArgumentParser()

parser.add_argument("key", type = str)
parser.add_argument("value", type = str)
args = parser.parse_args()

dict1[args.key] = args.value

print(dict1)