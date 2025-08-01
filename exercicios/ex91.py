#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
#dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogada 1': randint(1,6),
        'jogada 2': randint(1,6),
        'jogada 3': randint(1,6),
        'jogada 4': randint(1,6)}
ranking = list()
print('valores sorteados: ')
for k, v in jogo.items():
    print('{} tirou {} no dado.'.format(k,v))
    sleep(1)
ranking=sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-=-'*30)
print('Ranking dos jogadores: ')
for i, v in enumerate(ranking):
    print('{}º lugar: {} com {}'.format(i+1, v[0],v[1]))
    sleep(1)
print()
print('Obrigado pela participação!')