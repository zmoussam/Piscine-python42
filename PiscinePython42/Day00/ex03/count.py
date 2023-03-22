def text_analyzer(string):
    upper, lower, punctuation, space = 0, 0, 0, 0
    for i in range(len(string)):
        if string[i].isupper():
            upper += 1
        elif string[i].islower():
            lower += 1
        elif string[i] == 
    print("The text contains " + str(len(string)) + " character(s):")

text_analyzer("hi")