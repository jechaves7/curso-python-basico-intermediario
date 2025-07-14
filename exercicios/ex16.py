# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
#por exempolo: digite um número: 6.127. o numero 6.127 tem a parte inteira 6.

#import math
#n=float(input('Digite um número'))
#print('o número é {} e sua parte inteira é {}.'.format(n, math.trunc(n)))

###ou
#from math import trunc
#n=float(input('digite um valor: '))
#print('o valor é {} e sua parte inteira é {}'.format(n, trunc(n)))

###ou

n=float(input('digite um valor: '))
print('o valor digitado é {} e sua parte inteira é {}.'.format(n,int(n)))
