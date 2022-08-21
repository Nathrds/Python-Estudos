print('Índice de Massa Corporal')
peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de \033[4m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('Você está \033[4;35mABAIXO\033[m do PESO normal.')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa do \033[4;35mPESO NORMAL\033[m.')
elif 25 <= imc < 30:
    print('Você está em \033[4;35mSOBREPESO\033[m.')
elif 30 <= imc < 40:
    print('Você está em \033[4;35mOBESIDADE!\033[m')
elif imc >= 40:
    print('Você está em \033[4;35mOBESIDADE MÓRBIDA\033[m, \033[31mcuidado!\033[m')
