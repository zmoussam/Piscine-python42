import string
import sys

def remove_puctuation(s):
    deletetion_symbols = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    newStr = ""
    for c in s:
        if c not in deletetion_symbols:
            newStr += c
    return newStr

length = len(sys.argv)
if (not length == 3) or not sys.argv[2].isdigit():
    print("ERROR")
    exit()

splitLst = remove_puctuation(sys.argv[1]).split()
lst = []
for i in range(len(splitLst)):
    if len(splitLst[i]) > int(sys.argv[2]):
        lst.append(splitLst[i])
print(lst)