print('Ficha do Jogador')


def ficha(jogador='<desconhecido>', gols=0):
    print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


# Programa principal
nome = str(input('Nome do Jogador: '))
ngol = str(input('Número de Gols: '))
if ngol.isnumeric():
    ngol = int(ngol)
else:
    ngol = 0
if nome.strip() == '':
    ficha(gols=ngol)
else:
    ficha(nome, ngol)
