#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileirão, na ordem de colocação. Depois mostre:
#a) os 5 primeiros
#B)os últimos 4 colocados.
#c) times em ordem alfabetica
#d) em que posição está o time do internacional.


tabela= ('Flamengo', 'Cruzeiro', 'Bragantino', 'Bahia',
         'Palmeiras', 'Botafogo', 'Fluminense', 'Atletico-mg',
         'Ceará', 'Mirassol', 'Corinthians', 'Gremio', 'Internacional',
         'Vasco', 'São paulo', 'Santos', 'Vitória', 'Fortaleza',
         'Juventude', 'Sport')
print('a lista de times do brasileirão {}'.format(tabela))
print('-'*100)
print('os 5 primeiros colocados são {}'.format(tabela[0:5]))
print('-'*100)
print('os ultimos 4 colocados foram {}'.format(tabela[-4:]))
print('-'*100)
print('em ordem alfabetica é {}'.format(sorted(tabela)))
print('-'*100)
print('o internacional está na {}ª posição'.format(tabela.index('Internacional')+1))
