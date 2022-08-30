print('Divination Game v2.0')
from random import randint
computer = randint(0, 10)
print('Hi, I’m your computer. I just thought of a number between 0 and 10.')
print('Can you guess which one it was?')
gotit = False
guesses = 0
while not gotit:
    player = int(input('What’s your guess? '))
    guesses += 1
    if player == computer:
        gotit = True
    else:
        if player < computer:
            print('More... Try one more time.')
        elif player > computer:
            print('Less... Try one more time.')
print('You got it with {} attempts. Congratulations!'.format(guesses))
