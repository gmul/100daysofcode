# Leap year calculator

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

div_4 = int(year) % 4
div_100 = int(year) % 100
div_400 = int(year) % 400

if div_4 == 0:
  if div_100 == 0:
    if div_400 == 0:
      print("This is a leap year")
    else:
      print("This is not a leap year")
  else:
    print("This is a leap year)")
else:
  print("This is not a leap year")

