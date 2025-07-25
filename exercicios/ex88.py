#faça um programa que ajude um jogador da mega sena a criar palpites. o programa vai perguntar quantos jogos serão gerados
#e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random
import time
from os import remove
lista = []
jogos = []
print('-=-'*30)
print('joga na mega sena')
print('-=-'*30)
quant=int(input('Quantos jogos que criar? '))
tot=1
while tot <= quant:
    cont = 0
    while True:
        num= random.randint(1,60)
        if num not in lista:
           lista.append(num)
           cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=-'*3,f'sorteando {quant} jogos', '-=-'*3)
for i,l in enumerate(jogos):
    print('jogo {} : {}'.format(i+1,l))
    time.sleep(2)
print('-=-'*30)
print('Boa sorte!!!')
















