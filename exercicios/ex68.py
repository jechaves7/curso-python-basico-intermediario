#Faça um programa que jogue par ou impar com o computador. O jogo s´será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random
acumulador=0
while True:
    j=int(input('Diga um valor:'))
    computador=random.randint(0,10)
    total=j+computador
    tipo= ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I]')).strip().upper() [0]
    print('vc jogou {} e o computador {}. Total de {}.'.format(j,computador,total))
    print('Deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('vc venceu')
            acumulador+=1
        else:
            print('vc perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('venceu')
            acumulador+=1
        else:
            print('perdeu')
            break
    print('Vamos jogar novamente...')
print('Game over! você perdeu {} vezes.'.format(acumulador))



