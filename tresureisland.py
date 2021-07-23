
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


first_choice = input("You must choose to go left or right ")
if first_choice == "right":
  print("GAME OVER")
else:
  print("You have chosesn wisely. You have progressed")
  second_choice = input("You must choose to swim or wait " )


if first_choice == "left" and second_choice == "wait":
  print("You have chosen wisely, on with your quest")
else:
    print("GAME OVER")


third_choice = input("To continue your quest you must choose the red, blue or yellow door ") 
if first_choice == "left" and second_choice == "wait" and third_choice == "yellow":
  print("You won the game!!!")
else:
  print("sorry, you crapped out. GAME OVER")  


end:
print("Thanks for playing")

