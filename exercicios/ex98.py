#Faça um programa que tenha uma função chamada contador(), que receba 3 parametros: inicio, fim e passo. Seu programa tem
#que realizar 3 contagem atraves da função criada:
#a)de 1 ate 10, de 1 em 1
#b)de 10 ate 0, de 2 em 2
#c)uma contagem personalizada.

from time import sleep

def contador(i,f,p):
    if p<0:
        p*=-1
    if p==0:
        p=1
    print('-=-'*20)
    print('A contagem de {} até {} de {} em {}.'.format(i,f,p,p))
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print('{} '.format(cont), end='')
            sleep(0.5)
            cont  += p
        print('Fim!')
    else:
        cont=i
        while cont >= f:
            print('{} '.format(cont), end='')
            sleep(0.5)
            cont  -= p
        print('Fim!')
    print('-=-'*20)
contador(1,10,1)
contador(10,0,2)
print('-=-'*20)
print('Agora é a sua vez de personalizar a contagem!')
ini=int(input('inicio:  '))
fim=int(input('fim:  '))
passo=int(input('passo:  '))
contador(ini, fim, passo)