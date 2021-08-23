import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator")
numletters = int(input("How many letters would you like in your password?\n "))
numsymbols = int(input(f"How many symbols would you like in your password?\n "))
numnumbers = int(input(f"How many numbers would you like in your password?\n "))

password = ""

for numletter in range(1, numletters + 1):
    password += random.choice(letters)
  

  

for numsymbols in range(1, numsymbols + 1):
    password +=  random.choice(symbols)
    

for nunumbers in range(1, numnumbers + 1):
    password += random.choice(numbers)
    

print(password)