numbers = {4,3,2,1,1,1,1,4,4,4,4,2,3}

name = "iiiissssslllllaaaam"

unique_set = set(name)

print(unique_set)

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(dir(unique))