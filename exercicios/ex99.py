#Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros. Seu programa
#tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*num):
    cont=maior=0
    print('-=-'*30)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print('{} '.format(valor), end='')
        sleep(0.3)
        if cont==0:
            maior=valor
        else:
            if valor>maior:
                maior=valor
        cont+=1
    print('Foram informados {} valores ao todo.'.format(cont))
    print('o maior valor informado foi {}'.format(maior))


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()