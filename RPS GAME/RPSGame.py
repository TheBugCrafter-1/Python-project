import random 

print("===================")
print('Rock Paper Scissors')
print("===================")

computers = ['rock', 'paper', 'scissors'] 
Player_choice = input("Select One Option: ROCK, PAPER, SCISORR: ")

computer_choice = random.choice(computers)
print("Computer chose:", computer_choice)


PlayerChoice = Player_choice
print(f'Player Choose: {PlayerChoice}')


def WhoWin(computer_choice, Player_choice):
    if computer_choice == Player_choice:
        print("THIS IS DRAWWW!!!")
    elif computer_choice == "rock" and Player_choice == "scissors":
        print(f"Computer W I N ")
    elif computer_choice == "paper" and Player_choice == 'scissors':
        print(f"Player W I N ")
    elif computer_choice == 'scissors' and Player_choice == 'rock':
        print("Player W I N")
    else:
        print("syntex error")


WhoWin(computer_choice, Player_choice )


 

