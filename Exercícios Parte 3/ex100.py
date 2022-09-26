print('-~' * 24)
print('Funções para sortear e somar')
print('-~' * 24)
from random import randint
from time import sleep


def sorteia(lista):
    print('Sortenado 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista} , temos {soma}')


# Programa principal
numeros = list()
sorteia(numeros)
somaPar(numeros)
