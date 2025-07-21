#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter
#apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
#geradas.

lista = []
pares = []
impares = []
continuar=' '
while True:
    lista.append(int(input('digite um valor:')))
    continuar=input('quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'S':
        lista.append(int(input('digite um valor:')))
        n = input('quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        print('finalizando...')
        break
    while continuar != 'S' and continuar != 'N':
        continuar = input('quer continuar? [S/N]').upper().strip()[0]
print(lista)
print('-=-'*30)
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('a lista completa é {}'.format(lista))
print('os numeros pares são {}'.format(pares))
print('os numeros impares são {}'.format(impares))



























