#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#no final, mostre:
#a) Qual é o total gasto na compra
#b) Quantos produtos custam mais de R$ 1000.
#c) Qual é o nome do produto mais barato.


print('-'*40)
print('Loja super barata'.center(40))
print('-'*40)

total=0
maisde1000=0
menor=0
maisbarato=0
cont=0
while True:
    nome=str(input('nome do produto? '))
    preço=float(input('Qual o preço do produto? R$ '))
    cont+=1
    total+=preço
    if preço > 1000:
        maisde1000+= 1
    if cont == 1:
        menor=preço
        maisbarato = nome
    else:
        if preço < menor:
            menor = preço
            maisbarato=nome
    continuar=' '
    while continuar not in 'SN':
        continuar = input('Quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print('Você gastou R$ {} na compra \n{} produtos custaram mais de R$ 1000 \nO produto mais barato foi {}.'.format(total,maisde1000,maisbarato))






































