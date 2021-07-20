
age = input("What is your current age?")

#Write your code below this line 
total_days = 80 * 365
total_weeks = 80 * 52
total_months = 80 * 12

days = total_days - int(age) * 365
weeks = total_weeks - int(age) * 52
months = total_months - int(age) * 12

print(f"You have {days} days, {weeks} weeks and {months} left")

