##Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

p=float(input('Qual o preço do produto?'))
np=p*0.05
npp=p-np
print('O valor do primeiro produto é{}, com o desconto fica{}.'.format(p,npp))
