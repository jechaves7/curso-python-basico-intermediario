#Crie um programa que leia vários numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os
#valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
#a digitar valores.

resp='s'
soma=quant=media=maior=menor=0
while resp in 'Ss':
    num=int(input('Digite um numero:'))
    soma+=num
    quant+=1
    if quant == 1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num < menor:
            menor=num

    resp=str(input('quer continuar? [S/N]')).upper().split()[0]

media=soma/quant
print('você digitou {} números e a sua média foi {}'.format(quant,media))
print('o maior valor foi {} e o menor foi {}'.format(maior,menor))
