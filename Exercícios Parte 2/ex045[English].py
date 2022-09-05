print('GAME JOKENPÔ: Rock, Paper and Scissors.')
from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
print('''\033[36mYour options:
[ 0 ] ROCK
[ 1 ] PAPER
[ 2 ] SCISSORS\033[m''')
player = int(input('What is your move? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('\033[33m--\033[m' * 12)
print('\033[33mComputer played: {}\033[m'.format(items[computer]))
print('\033[33mPlayer played: {}\033[m'.format(items[player]))
print('\033[33m--\033[m' * 12)
if computer == 0: # computer played ROCK
    if player == 0:
        print('DRAW')
    elif player == 1:
        print('PLAYER WINS')
    elif player == 2:
        print('COMPUTER WINS')
    else:
        print('INVALID MOVE!')
elif computer == 1: # computer played PAPER
    if player == 0:
        print('COMPUTER WINS')
    elif player == 1:
        print('DRAW')
    elif player == 2:
        print('PLAYER WINS')
    else:
        print('INVALID MOVE!')
elif computer == 2: # computer played SCISSORS
    if player == 0:
        print('PLAYER WINS')
    elif player == 1:
        print('COMPUTER WINS')
    elif player == 2:
        print('DRAW')
    else:
        print('INVALID MOVE!')
