# Desenvolva um programa que leia o primeiro termo e a razão de uma pa.
# no final, mostre os 10 primeiros termos desta progressão.

#print('='*40)
#print('10 primeiros termos de uma PA'.center(40))
#print('='*40)
#primeiro= int(input('Digite o termo:'))
#razão=int(input('Digite a razão:'))
#for pa in range(0,10):
#    termo= primeiro + (pa * razão)
#    print(termo,end=' -> ')

#ou

print('='*40)
print('10 primeiros termos de uma PA'.center(40))
print('='*40)

#termo= int(input('Digite o termo:'))
#razão= int(input('Digite a razão:'))
#décimo= termo + (10-1) * razão
#for pa in range (termo, décimo, razão):
#    print('a progressão do número {} é {}'.format(termo,pa))
#print('acabou')

#ou


termo= int(input('Digite o termo:'))
razão= int(input('Digite a razão:'))
décimo= termo + (10-1) * razão
for pa in range (termo, décimo+razão, razão):
    print('{}'.format(pa),end='-> ')
print('\nacabou')






















