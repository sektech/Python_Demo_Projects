import random

choices = ['Rock','Paper','Scissor']
computer = random.choice(choices)

cpu_score = 0
player_score = 0
while (True):
    player = input(f'Enter your choice {list(choices)}')
    if (player == computer):
        print ("Its a tie")
    elif (player == 'Rock'):
        if (computer == 'Paper'):
            print(f'you lose, computer {computer} covers player {player}')
            cpu_score += 1
        else:
            print(f'you win, player {player} covers computer {computer}')
            player_score +=1
    elif (player == 'Paper'):
        if (computer == 'Scissor'):
            print(f'you lose, computer {computer} covers player {player}')
            cpu_score += 1
        else:
            print(f'you win, player {player} covers computer {computer}')
            player_score += 1
    elif (player == 'Scissor'):
        if (computer == 'Paper'):
            print(f'you lose, computer {computer} covers player {player}')
            cpu_score += 1
        else:
            print(f'you win, player {player} covers computer {computer}')
            player_score += 1
    else:
        print("Game End!!! \n Final scores ")
        print(f'player scores : {player_score}')
        print(f'Computer scores : {cpu_score}')
        break;



