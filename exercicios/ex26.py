# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.
from itertools import count

frase=input('Digite uma frase:').upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('ela aparece pela primeira vez na posição {}'.format(frase.find('A')))
print('ela aparece pela ultima vez na posição {}'.format(frase.rfind('A')))