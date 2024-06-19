# We have to develop a Rock, Paper, Scissors game
import random

print("Welcome to the rock paper scissors game\n")
man_choose = input("Choose 1 for Rock, 2 for Paper, 3 for Scissors\n")

comp_choose = random.randint(1, 3)

if man_choose == 1:
    if comp_choose == 1:
        print("Game tie. Play next round")
    elif comp_choose == 2:
        print("You loose. Better luck next time")
    else:
        print("You won against the computer.")
elif man_choose == 2:
    if comp_choose == 2:
        print("Game tie. Play next round")
    elif comp_choose == 1:
        print("You loose. Better luck next time")
    else:
        print("You won against the computer.")
else:
    if comp_choose == 3:
        print("Game tie. Play next round")
    elif comp_choose == 1:
        print("You loose. Better luck next time")
    else:
        print("You won against the computer.")

print("Run the program again to play next round")

