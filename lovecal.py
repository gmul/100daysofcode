
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_score = 0
name1.lower()

if name1.count("t"):
  name1_score += 1
if name1.count("r"):
  name1_score += 1
if name1.count("u"):
  name1_score += 1
if name1.count("e"):
  name1_score += 1

name2_score = 0
name2.lower()

if name2.count("t"):
  name2_score += 1
if name2.count("r"):
  name2_score += 1
if name2.count("u"):
  name2_score += 1
if name2.count("e"):
  name2_score += 1




#print(name1_score)
#print(name2_score)
total_score = int(str(name1_score) + str(name2_score))
#print(total_score)

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together")
else:
  print(f"Your score is {total_score}")


