#Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o
#valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
#(desconsiderando o flag).
cont=0
soma=0
while True:
    n=int(input('Digite o valor (999 para parar):'))
    if n == 999:
        break
    cont += 1
    soma += n

print('foram digitados {} números e a soma entre eles foi de {}'.format(cont,soma))