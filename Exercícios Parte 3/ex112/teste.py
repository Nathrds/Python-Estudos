print('Entrada de dados monetários ex112')

from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)
