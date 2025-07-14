#Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5! = 5*4*3**2*1 = 120

#import math
#n1=int(input('Digite um número para verificar sua fatorial:'))
#fatorial=math.factorial(n1)
#print('A fatorial do número {:.0f} é {}:'.format(n1,fatorial))

#ou
n=int(input('Digite um número para verificar sua fatorial:'))
c=n
f=1
print('calculando {}! = '.format(n),end='')
while c> 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ', end='')
    f*=c
    c-= 1
print(f)

