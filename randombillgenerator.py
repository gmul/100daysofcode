import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
test = random.choice(names)
print(test)
