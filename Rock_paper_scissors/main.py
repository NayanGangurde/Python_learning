from random import choice
import time
Rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock"""

Paper = r"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
Paper"""

Scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors"""

hand = [Rock, Paper, Scissors]

game_play = 'Y'
while game_play == 'Y':

    comp_hand = choice(hand)
    user_hand = int(input("Please select number for your choice:1:-Rock, 2:- Paper, 3:- Scissors==="))
    if user_hand == 1:
        print("Your choice:-" + Rock)
        print("Computer choice:-" + comp_hand)
        if comp_hand == Rock:
            print("Draw")
        elif comp_hand == Paper:
            print("You lose")
        elif comp_hand == Scissors:
            print("You win")
    elif user_hand == 2:
        print("Your choice:-" + Paper)
        print("Computer choice:-" + comp_hand)
        if comp_hand == Rock:
            print("You won")
        elif comp_hand == Paper:
            print("Draw")
        elif comp_hand == Scissors:
            print("You Lose")

    elif user_hand == 3:
        print("Your choice:-" + Scissors)
        print("Computer choice:-" + comp_hand)
        if comp_hand == Rock:
            print("You lose")
        elif comp_hand == Paper:
            print("You won")
        elif comp_hand == Scissors:
            print("Draw")
    else:
        print("Wrong Choice")
    game_play =  input("Want to play again Enter Y or N:").upper()

