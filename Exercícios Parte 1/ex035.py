print('Analisando Triângulo v1.0')
print('---' * 15)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[4;34mPODEM\033[m formar um triângulo!')
else:
    print('Os segmentos acima \033[4;31mNÃO\033[m podem formar um triângulo!')
