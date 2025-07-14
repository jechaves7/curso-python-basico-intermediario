#melhore o jogo do desafio 028 onde o computador vai ''pensar'' em um número entre 0 e 10. só que agora o jogador
#vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


import random
import time
from idlelib.sidebar import temp_enable_text_widget
from random import randint
computador=randint(0,10) # faz o computador pensar
print('sou seu computador... acabei de pensar em um número entre 0 e 10')
print('será que vc consegue advinhar qual numero foi?')
tentativas=0
acertou= False
while not acertou:
    jogador = int(input('Qual é o palpite?'))
    print('processando...')
    time.sleep(1)
    tentativas+=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... tente novamente')
        else:
            print('menos... tente novamente')

print('acertou')
print('vc tentou {} vezes para acertar'.format(tentativas))