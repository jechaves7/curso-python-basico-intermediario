#Crie um programa que vai gerar cinco números aleátorios e colocar em uma tupla. Depois disso, mostre a listagem de
#números gerados e também indique o menor e o maior valor que estão na tupla.

import random
num=(random.randint(1,10), random.randint(1,10),
     random.randint(1,10),random.randint(1,10),
     random.randint(1,10))
print('os valores sorteadoa foram {}'.format(num))
print('o maior valor sorteado foi {}'.format(max(num)))
print('o menor valor sorteado foi {}'.format(min(num)))

