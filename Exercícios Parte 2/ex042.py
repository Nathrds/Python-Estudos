print('Analisando Triângulos v2.0')
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[4;34mPODEM\033[m formar um triângulo!', end='')
    if r1 == r2 == r3:
        print(' \033[34mEQUILÁTERO.\033[m')
    elif r1 != r2 != r3 != r1:
        print(' \033[34mESCALENO.\033[m')
    else:
        print(' \033[34mISÓSCELES.\033[m')
else:
    print('Os segmentos acima \033[4;31mNÃO\033[m podem formar um triângulo!')
