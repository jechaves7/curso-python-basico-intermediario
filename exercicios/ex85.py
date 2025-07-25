#Crie um programa onde o usuario possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
#separados os valores pares e impares. No final, mostre os valores pares e impares em ordem crescente.

lista = [[],[]]

valor=0
for c in range (1,8):
    valor=(int(input('Digite o {}º valor: '.format(c))))
    if valor % 2 == 0:
        lista[0].append(valor)
    if valor % 2 == 1:
        lista[1].append(valor)
print('-=-'*30)
lista[0].sort()
lista[1].sort()
print('os valores da lista são {}'.format(lista))
print('os valores pares são {}'.format(lista[0]))
print('os valores impares são {}'.format(lista[1]))