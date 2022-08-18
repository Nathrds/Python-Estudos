print('Comprando números')
pri = int(input('Digite o primeiro valor: '))
seg = int(input('Digite o segundo valor: '))
if pri > seg:
    print('O \033[36mprimeiro\033[m valor é \033[1mMAIOR\033[m')
elif pri < seg:
    print('O \033[36msegundo\033[m valor é \033[1mMAIOR\033[m')
else:
    print('\033[31mNão\033[m existe valor maior, os dois são \033[1mIGUAIS\033[m')
