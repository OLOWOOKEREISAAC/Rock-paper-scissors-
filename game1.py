import random


print('Rock, Paper, Scissors...')
Player = input('Please enter your name: ')
Instructions = [ 'P is for Paper', 'S is for Scissors', 'R is for Rock']



weapons ={'P' :'Paper', 'p' :'Paper', 'S' : 'Scissors', 's' : 'Scissors', 'R' : 'Rock', 'r' : 'Rock'}
cpu_choice = ['P', 'S', 'R']


def play_game():
    winner = 'none'
    while winner == 'none':
        for values in Instructions:
            print(values)

        CPU = random.choice(cpu_choice)
        players_weapon= input('Enter one weapon(P/S/R): ')
        try:
            print(Player, '(' ,weapons[players_weapon] ,') : CPU (',weapons[CPU] , ')' )
        except:
            print('Invalid input')


        if players_weapon == 'R' or players_weapon =='r' and CPU == 'R':
            print('Awww, Its a Tie. You both choose Rock')
        elif players_weapon == 'P' or players_weapon == 'p'  and CPU == 'P':
            print('Awww, Its a Tie. You both choose Paper')
        elif players_weapon == 'S' or players_weapon == 's' and CPU == 'S':
            print('Awww, Its a Tie. You both choose Scissors')
        elif players_weapon == 'R' or players_weapon == 'r' and CPU == 'P':
            winner = 'CPU'
            print('Awww, CPU won, Paper beats Rock.')
            
        elif players_weapon == 'P' or players_weapon == 'p' and CPU == 'S':
            print('Awww, CPU won, Scissors beats Paper.')
            winner = 'CPU'
        elif players_weapon == 'S' or players_weapon == 's' and CPU == 'R':
            print('Awww, CPU won, Rock beats Scissors.')
            winner = 'CPU'
        elif players_weapon == 'R' or players_weapon == 'r' and CPU == 'S':
            print('Hurray, You won, Rock beats scissors.')
            winner = 'Player'
        elif players_weapon == 'P' or players_weapon == 'p' and CPU == 'R':
            print('Hurray, You won, Paper beats Rock.')
            winner = 'Player'
        elif players_weapon == 'S' or players_weapon == 's' and CPU == 'P':
            print('Hurray, You won, Scissors beats Paper.')
            winner = 'Player'
        else:
            print('Error!!!\nThat\'s not a valid weapon')

 
play_game() 
