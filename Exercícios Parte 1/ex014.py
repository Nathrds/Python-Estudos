print('Conversor de Temperaturas')
temp = float(input('Informe a temperatura em ºC: '))
novo = (temp * (9/5)) + 32
# ou ((9 * temp) / 5) + 32
print('A temperatura de {}ºC corresponde a {}ºF.'.format(temp, novo))
