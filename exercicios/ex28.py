#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o úsuario venceu ou perdeu.


#import random
#nume=int(input('digite um numero para descobrir se é igual ao do pensado pelo computador'))
#num=int(random.randint(1,5))
#print(num)
#if nume == num:
#    print('voçê acertou')
#else:
#    print('voçê errou')


##ou##

import random
import time
from random import randint
computador=randint(0,5) # faz o computador pensar
print('-=-'*20)
print('vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador=int(input('Em que número eu pensei?')) #jogador tenta advinhar
print('processando...')
time.sleep(3)
if jogador == computador:
    print('parabens! voçe conseguiu me vencer!')
else:
    print('ganhei, eu pensei no número {} e não no {}'.format(computador,jogador))

