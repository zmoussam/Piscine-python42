name = input("enter your name : ")
age = input("enter your age : ")

def __SayHey(name, age):
    print("hello " + name + " your age is : " + str(age))

__SayHey(name, 23)

def cube(num):
    return num*num*num

result = cube(3) 

print("cube 3 is : "+ str(result))

# power function 

print(3**6)

def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(power(3, 6))
