#Crie um programa que faça o computador jogar jokenpô com voçê.
import random
import time

print('''Suas opções:
[0] - pedra
[1] - papel
[2] - tesoura''')
jogada= int(input('Qual é a sua jogada?'))
time.sleep(1)
print('jok')
time.sleep(1)
print('en')
time.sleep(1)
print('po!!!')
itens = ('pedra', 'papel', 'tesoura')
computador= random.randint(0,  2)
print('-='*15)
print('o computador escolheu {}'.format(itens[computador]))

print('o jogador escolheu {}'.format(itens[jogada]))
print('-='*15)
if computador == 0:
    if jogada == 0:
        print('Empate')
    elif jogada == 1:
        print('vc ganhou')
    elif jogada == 2:
        print('computador ganhou')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogada == 0:
        print('computador ganhou')
    elif jogada == 1:
        print('empate')
    elif jogada == 2:
        print('vc ganhou')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogada == 0:
        print('vc ganhou')
    elif jogada == 1:
        print('computador ganhou')
    elif jogada == 2:
        print('empate')
    else:
        print('Jogada inválida')

































