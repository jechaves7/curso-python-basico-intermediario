# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#a) quantas vezes apareceu o valor 9.
#b) em que posição foi digitado o primeiro valor 3.
#c) quais foram os números pares.
from operator import index

num= (int(input('Digite um número:')),
       int(input('Digite um número:')),
       int(input('Digite um número:')),
       int(input('Digite um número:')))
print('vc dgitou os valores {}'.format(num))
print('o valor 9 apareceu {} vezes'.format(num.count(9)))
if 3 in num:
    print('o valor 3 apareceu na posição {}'.format(num.index(3)+1))
else:
    print('o valor 3 não foi digitado em nenhuma posição')
print('os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')