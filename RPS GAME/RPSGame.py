import random 

print("===================")
print('Rock Paper Scissors')
print("===================")



def WhoWin(computer_choice, Player_choice):
    if computer_choice == Player_choice:
        return 'This is a D R A W W W !!!'
    elif computer_choice == "rock" and Player_choice == "scissors":
        return 'computer W I N !'
    elif computer_choice == "paper" and Player_choice == 'scissors':
        return"player W I N "
    elif computer_choice == 'paper' and Player_choice == 'rock':
        return"Player W I N"
    elif Player_choice == 'paper' and computer_choice == 'scissors':
        return 'Computer W I N'
    elif Player_choice == 'rock' and computer_choice == 'scissors':
        return 'Computer W I N'
    elif Player_choice == 'paper' and computer_choice == "rock":
        return 'computer W I N'
    else:
        return"Invalid choice, try again" 
    

count = 0

while count < 5: 
    computers = ['rock', 'paper', 'scissors'] 

    Player_choice = input("Select One Option: ROCK, PAPER, SCISORR: ").lower()

    print(f'Round {count + 1}/5')

    PlayerChoice = Player_choice
    print(f'Player Choose: {PlayerChoice}')

    computer_choice = random.choice(computers)
    print("Computer chose:", computer_choice)

    result = WhoWin(computer_choice, Player_choice)
    print(result)

    count += 1 

print('Game Over ')




    
    





 

