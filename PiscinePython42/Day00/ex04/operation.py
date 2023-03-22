import sys

lenght = len(sys.argv)

if lenght > 3:
    print("AssertionError: too many arguments!!")
elif lenght < 3:
    print("Usage: python operations.py <number1> <number2>\n\
    Example:\n\
    python operations.py 10 3")
else:
    if sys.argv[1].isdigit() and sys.argv[2].isdigit():
        try:
            print("sum:        " + str(int(sys.argv[1]) + int(sys.argv[2])))
            print("Difference: " + str(int(sys.argv[1]) - int(sys.argv[2])))
            print("Product:    " + str(int(sys.argv[1]) * int(sys.argv[2])))
            print("Quotient:   " + str(int(sys.argv[1]) / int(sys.argv[2])))
            print("Remainder:  " + str(int(sys.argv[1]) % int(sys.argv[2])))
        except ZeroDivisionError:
            print("Quotient:   ERROR (division by zero)")
            print("Remainder:  ERROR (module by zero)")
    else:
        print("AssertionError: only integers")
