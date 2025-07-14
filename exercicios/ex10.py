##Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
##considere uss1,00 = rs 3,27

n=float(input('Quantos reais vc tem na carteira? R$: '))
n1=(n/3.27)
print('vc possui R$:{:.2f}, convertendo para dolares fica USS :{:.2f}'.format(n,n1))

