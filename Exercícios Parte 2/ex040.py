print('Aquele clássico da Média')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é \033[1m{:.1f}\033[m'.format(n1, n2, média))
if média >=5 and média < 7:
    print('O aluno está em \033[36mRECUPERAÇÃO\033[m')
elif média < 5:
    print('O aluno está \033[31mREPROVADO\033[m')
elif média >= 7:
    print('O aluno está \033[33mAPROVADO\033[m')
