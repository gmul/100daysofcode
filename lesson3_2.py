# BMI Calculator with Nested IFs

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆


weight = int(weight)
height = float(height)
height2 = height **2
bmi = round(weight / height2 , 2)
#print(int(bmi))
#age = int(input("What is your age? ")

if bmi <= 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi <= 25:
  print (f"Your BMI is {bmi}, you have a normal weight")
elif bmi <= 30:
  print (f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35:
  print (f"Your BMI is {bmi}, you have a normal weight")
elif bmi <= 40:
  print (f"Your BMI is {bmi}, you are clinically obese")
else:
  print("Sorry you are dead")

















