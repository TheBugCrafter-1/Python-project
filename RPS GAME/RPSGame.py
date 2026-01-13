import random 


print("===================")
print('Rock Paper Scissors')
print("===================")

computers = ['rock', 'paper', 'scissors'] 
Player_choice = input("Select One Option: ROCK, PAPER, SCISORR")

computer_choice = random.choice(computers)
print("Computer chose:", computer_choice)


if Player_choice == computer_choice:
    print("THIS IS DRAWWWW!!!")

elif Player_choice == "rock" and computer_choice == "scissor":
    print("Player wins")
elif Player_choice == 'rock' and computer_choice == "paper":
    print('Computer wins')
elif Player_choice == "paper" and computer_choice == "rock":
    print('Player wins')


 

