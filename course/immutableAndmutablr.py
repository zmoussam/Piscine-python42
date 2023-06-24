'''
    Learn the 5 must-know concepts
'''
#----1-----immutable vs mutable type

# str    |  list
# int    |  set
# float  |  dict
# bool   |
# bytes  |
# tuple  |

# x = (1, 2)
# y = x
# x = (1, 2, 3)
# print(x, y)

# x = [1, 2]
# y = x
# x[0] = 100 
# x = [9, 0]
# print(x, y)

# def get_largest_numbers(numbers, n):
#     numbers.sort()
    
#     return numbers[-n:]

# nums = [2, 3, 4, 1, 34, 123, 321, 1]

# print(nums)

# largest = get_largest_numbers(nums, 2)
# print(largest)
# print(nums)

#----2-----List comprehensions

# x = [i for i in range(10)]
# print(x)

# x = [i for i in range(10) if i % 2 == 0]
# print(x)

#----3-----Fuction argument and parameter types

def complicated_function(x, y, z = 10):
    print(x, y, z)
    pass
complicated_function(1, y = 3)