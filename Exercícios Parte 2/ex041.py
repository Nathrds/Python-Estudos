print('Classificando Atletas')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação \033[34mMIRIM\033[m')
elif idade <= 14:
    print('Classificação \033[33mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação \033[35mJÚNIOR\033[m')
elif idade <= 25:
    print('Classificação \033[32mSÊNIOR\033[m')
else:
    print('Classificação \033[31mMASTER\033[m')
