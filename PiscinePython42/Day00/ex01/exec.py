import sys

#print("Python version", sys.version)

# stdin, stdout, stderr (input, output and error channels)  control

#sys.stdout.write('hello\n')

# Control channel

#fd = open('my_stdout.txt', 'w')

#sys.stdout = fd 

#print('hellllllllloooooooo')
#sys.stdout.close()
#sys.stdout = sys.__stdout__
#print("hello again")

# Max int size

# Commande line arguments

#print("Sys argv: ", sys.argv)
#for path in sys.path:
 #   print("Path: ", path)

#print("argc: ", len(sys.argv))
def my_reverse(str):
    return str[::-1]

lenght = len(sys.argv)

if lenght == 1:
    sys.exit()
    
result = ""
i = lenght - 1
while i > 0:
    result += my_reverse(sys.argv[i]).swapcase()
    if i != 1:
        result += " "
    i -= 1
print(result)

