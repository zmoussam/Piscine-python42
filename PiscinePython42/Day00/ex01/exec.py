import argparse

parser = argparse.ArgumentParser(description='finds the arguments')
parser.add_argument('arguments', nargs='+', help='first argument' )

args = parser.parse_args()
if not args.arguments:
   print('No arguments provided')
else:
    numArg = len(args.arguments)
    print(numArg)
# arg = list(arg)
# arg.reverse()
# arg = arg[::-1]
# arg = arg.swapcase()
