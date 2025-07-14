###Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math
a=float(input('Digite um angulo:'))
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print('O valor do angulo é {}.\nseu valor do seno é {:.2f}.\no cosseno {:.2f}.\na tangente {:.2f}.'.format(a,s,c,t))
