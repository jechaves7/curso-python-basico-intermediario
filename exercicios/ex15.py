##Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
## e a quantidade de dias pelos quais foi alugado.
## Calcule o preço a pagar. sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.

km=float(input('quantos km percorridos?'))
d=int(input('Quantos dias de aluguel?'))
pp=km*0.15
ppp=d*60
print(pp+ppp)
