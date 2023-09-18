#importing random library
import random

#this functions calls the game
def game():
    #allowing user to choose rock,paper or scissors
    user_action=input("enter a choice(rock,paper,scissors):")

    possible_actions=["rock","paper","scissors"]

    #generating random action from possible_actions 
    computer_action= random.choice(possible_actions)
    print(f"\nyou chose {user_action},computer chose {computer_action}.\n")

    #checking if both player and user uses same action
    if user_action==computer_action:
        print(f"both players selected {user_action}.it's a tie!")

    #checking if player uses rock    
    elif user_action=="rock":
        if computer_action=="scissors":
           print("rock smashes scissors! you win!")
        else:
           print("paper covers rock! you lose.")

    #checking if player uses paper        
    elif user_action=="paper":
        if computer_action=="rock":
           print("paper covers rock! you win!")
        else:
           print("scissors cuts paper! you lose")

    #checking if player uses scissors
    elif user_action=="scissors":
        if computer_action=="paper":
           print("scissors cuts paper! you win!")
        else:
           print("rock smashes scissors! you lose")

#checking if user wants to play a game
while True:
    a=input("\nWant to play a game!!! (Y/N):")
    if (a=='Y' or a=='y'):
        game()
    else:
        break
    
