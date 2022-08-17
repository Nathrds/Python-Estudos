print('Conversor de Moedas')
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.09
euro = real / 5.25
print('Com R${:.2f} você pode comprar US${:.2f} e Euro{:.2f}.'.format(real, dolar, euro))
