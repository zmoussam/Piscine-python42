# or, and, and not

#syntax 
# if v1and v2
    # do somethings
#elif v1 and not v2
    # do somethings else
#elif not v1 and v2
    # do something
# else
    # somthing else

def mathc_string(str1, str2):
    if str1 == str2:
        print("the strings do match")
    else:
        print("the string dont match")
    
mathc_string("zack", "zakaria")