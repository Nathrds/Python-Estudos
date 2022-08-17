print('Par ou Ímpar?')
n = int(input('Digite um número qualquer: '))
r = n % 2
from time import sleep
print('Processando...')
sleep(2)
if r == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
