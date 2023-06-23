import string
import sys

length = len(sys.argv)
if (not length == 3) or not sys.argv[2].isdigit():
    print("ERROR")
    exit()
for p in sys.argv[1].punctuation:
    split_string = sys.argv[1].replace(p, '')
lst = split_string.split()
print(lst)