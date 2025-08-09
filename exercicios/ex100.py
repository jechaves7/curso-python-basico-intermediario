#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função
#vai sortear 5 números e colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
#sorteados pela função anterior.



from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista:')
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)
        print('{} '.format(n),end='')
        sleep(0.3)
    print('Pronto!')


def somapar(lista):
    soma=0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print('Somando valores pares da {}, temos {}'.format(lista,soma))


números =list()
sorteia(números)
somapar(números)