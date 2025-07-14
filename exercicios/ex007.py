### desenvolva um programa que leia duas notas de um alnuo, calcule e mostre sua média.

n1=float(input('Qual a primeira nota?'))
n2=float(input('Qual a segunda nota?'))
s=n1+n2
m=s/2
print('A soma das notas é {}, e sua média é {:.3f}'.format(s, m))
