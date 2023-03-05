friends  = [1, "codezilla", True , False, [1, "islam"]]
Family = ["html", "css", "javascript"]
print(friends)
print(friends[4][1])
print(friends[1:])
print(friends[1:4])

# friends += Family
friends.extend(Family) # the same thing
print(friends)
friends.append("python3")
print(friends)
friends.insert(9, "PHP")
print(friends)
friends.remove("codezilla")
print(friends)
whatWasPoped = friends.pop()
print(whatWasPoped)
print(friends.index("html"))
print(friends.count("javascript"))
# friends.sort() must be all same type

friends_copy = friends.copy() # Shallow copy
print(friends)
print(friends_copy)
friends.clear()
print(friends)
