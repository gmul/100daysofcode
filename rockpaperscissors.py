#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
Rock Paper Scissors

"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# list
game_images = [rock, paper, scissors]

player_choice = int(input("What do you choose, type 0 for Rock, 1 for paper or 2 for Scissors.\n "))

if player_choice >= 3 or player_choice < 0:
     print("You typed and invalid number")
else:
    print("\nYou chose")
    print(game_images[player_choice])

    computer_choice = random.randint(0, 2 )
    print("Computer chose:")
    print(game_images[computer_choice])
        
    #2 beast 1
    # 1 beats 0
    # 0 beats 2




    if computer_choice == player_choice:
        print("It's a draw")
    elif player_choice == 0 and computer_choice == 2:
        print("You win!!!!")
    elif computer_choice == 0 and player_choice == 2:
        print("You Lose!")
    elif computer_choice > player_choice:
        print("computer wins!!!")
    elif player_choice > computer_choice:
        print("You win")    
    elif computer_choice == player_choice:
        print("It's a draw")




#if player_choice == 1 and computer_choice == 0:
    print("You win!!!")
