import sys

def text_analyzer(string=None):
        ''' 
            This function counts the number
            of upper characters, lower characters,
            punctuation and spaces in a given text. 
        '''
        if string is None or string == '':
            string = input("What is the text to analyze? \n")
        upper, lower, punctuation, space = 0, 0, 0, 0
        if type(string) != str:
            print("AssertionError: argument is not a string")
            exit()
        print("The text contains " + str(len(string)) + " character(s):")
        for i in range(len(string)):
            if string[i].isupper():
                upper += 1
            elif string[i].islower():
                lower += 1
            elif string[i] == ' ':
                space += 1
            elif not string[i].isdigit():
                punctuation += 1
        print("- " + str(upper) + " upper letter(s)")
        print("- " + str(lower) + " lower letter(s)")
        print("- " + str(punctuation) + " punctuation mark(s)")
        print("- " + str(space) + " space(s)")

lenght = len(sys.argv)

if lenght > 2:
    print("invalid argument!!\n")
elif lenght == 2:
    text_analyzer(sys.argv[1])

#for test 
#$> python3
#>>> from count import text_analyzer
#>>> text_analyzer("Python 2.0, released 2000, introduced
#features like List comprehensions and a garbage collection
#system capable of collecting reference cycles.")
#The text contains 143 character(s):
#- 2 upper letter(s)
#- 113 lower letter(s)
#- 4 punctuatio
#>>> print(text_analyzer.__doc__)
#This function counts the number of upper characters, lower characters,
#punctuation and spaces in a given text.