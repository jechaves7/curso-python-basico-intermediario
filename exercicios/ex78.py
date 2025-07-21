#Faça um programa que leia 5 valores números e guarde-os em uma lista. No final, mostre qual foi o maior e p menor valor
#digitado e as suas respectivas posições nas lista.

lista= []
mai=0
menor=0
for c in range (0,5):
    lista.append(input('Digite o {}º valor:'.format(c)))
    if c == 0:
        mai=men=lista[c]
    else:
        if lista[c] > mai:
            mai=lista[c]
        if lista[c] < men:
            men=lista[c]
print('-=-'*20)
print('vc digitou os valores {}'.format(lista))
print('o maior valor digitado foi {} nas posições '.format(mai),end='')
for i,v in enumerate(lista):
    if v == mai:
        print('{}'.format(i),end= ' ')
print()
print('o menor valor digitado foi {} nas posições '.format(men),end='')
for i, v in enumerate(lista):
    if v == men:
        print('{}'.format(i),end= ' ')
print()
print('obrigado',end='')