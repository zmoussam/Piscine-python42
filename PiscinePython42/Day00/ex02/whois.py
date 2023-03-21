import sys 

lenght = len(sys.argv)

if lenght > 2: 
    print("AssertionError: more than one argument are provided")
elif lenght == 2 and not sys.argv[1].isnumeric():
    print("AssertionError: argument is not an integer")
else:
    if int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even")
    else:
        print("I'M Odd")
