numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
myList = list(map(lambda x: x*2, numbers))

print(myList)

print("--------------------------------")

names = ["ali","mehdi","reza"]
sayNameUpper = map(lambda name:name.upper(),names)
print(list(sayNameUpper))
