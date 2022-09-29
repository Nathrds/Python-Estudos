print('Transformando módulos em pacotes ex111')

from ex111.utilidadescev import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 35, 22)
