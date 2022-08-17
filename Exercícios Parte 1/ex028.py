print('Jogo da Adivinhação v.1.0')
from random import randint
from time import sleep
comput = randint(0, 5) # Faz o computador "pensar"
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('---' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('Processando....')
sleep(3)
if jogador == comput:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(comput, jogador))
