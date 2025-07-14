### Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
#calcule e mostre o comprimento da hipotenusa.


#co=float(input('Digite um valor: '))
#ca=float(input('digite outro valor: '))
#hip=(co**2+ca**2)**1/2
#print(hip)

#ou

import math
co=float(input('Digite um valor: '))
ca=float(input('digite outro valor: '))
hi=math.hypot(co,ca)
print(hi)
