print('Verificando as primeiras letras de um texto')
# A cidade começa com a palavra "SANTO"?
cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')
