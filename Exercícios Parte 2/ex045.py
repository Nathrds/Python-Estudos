print('GAME JOKENPÔ: Pedra, Pepel e Tesoura')
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comput = randint(0, 2)
print('''\033[36mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')
print('\033[33m--\033[m' * 12)
print('\033[33mComputador jogou: {}\033[m'.format(itens[comput]))
print('\033[33mJogador jogou: {}\033[m'.format(itens[jogador]))
print('\033[33m--\033[m' * 12)
if comput == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comput == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')
elif comput == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
