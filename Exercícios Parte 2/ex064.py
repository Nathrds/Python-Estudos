print('Tratando vários valores v1.0')
n = cont = soma = 0
n = int(input('Digite um número [use 999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [use 999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi de {}.'.format(cont, soma))
