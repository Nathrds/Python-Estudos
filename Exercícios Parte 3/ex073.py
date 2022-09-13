print('Tuplas com Times de Futebol')
times = ('São Paulo', 'São Caetano', 'Corinthians', 'Juventude', 'Grêmio',
         'Atlético-MG', 'Fluminense', 'Santos', 'Cruzeiro', 'EC Vitória',
         'Coritiba', 'Goiás', 'Ponte Preta', 'Athletico-PR', 'Vasco da Gama',
         'Guarani', 'Figueirense', 'Flamengo', 'Bahia', 'Paysandu', 'Internacional',
         'Paraná', 'Portuguesa', 'Palmeiras', 'Gama', 'Botafogo')
print('---' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('---' * 20)
print(f'Os 5 primeiros times são: {times[0:5]}')
print('---' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('---' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('---' * 20)
print(f'O Guarani está na {times.index("Guarani")+1}ª posição.')
