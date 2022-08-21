print('Conversor de Bases Numéricas')
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
\033[32m[ 1 ] converter em BINÁRIO\033[m
\033[36m[ 2 ] converter em OCTAL\033[m
\033[35m[ 3 ] converter em HEXADECIMAL\033[m''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a \033[32m{}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a \033[36m{}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[35m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')
    