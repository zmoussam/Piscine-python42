for char in "string":
    print(char)

for x in range(10):
    print(x)

buddies = ["piko", "grand", "sub"]
for index in range(len(buddies)):
    print(buddies[index])

for buddy in buddies:
    if buddy == "sub":
        print(buddy, " is your friend")
        break
else:
    print("not found")