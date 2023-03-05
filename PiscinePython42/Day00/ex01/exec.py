import argparse

parser = argparse.ArgumentParser()
parser.add_argument('num1', type=str, help='first number')
# parser.add_argument('num2', type=int, help='second number')

args = parser.parse_args()

print(args.num1)
