#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#a)Quantos números foram digitados.
#b) a lista de valores, ordenada de forma decrescente.
#c) se o valor 5 foi digitado e está ou não na lista.


lista = []
continuar = ' '
while True:
    n=int(input('Digite um valor:'))
    lista.append(n)
    continuar=input('quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'S':
        n=int(input('Digite um valor:'))
        lista.append(n)
        continuar = input('quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        print('finalizando...')
        break
    while continuar != 'N' and continuar != 'S':
        continuar = input('quer continuar? [S/N]').upper().strip()[0]
print(lista)
print('-=-'*30)
print('foram digitados {} valores.'.format(len(lista)))
lista.sort(reverse=True)
print('a lista em ordem decrescente é {}'.format(lista))
if 5 in lista:
    print('o valor 5 está na lista')
else:
    print('o valor 5 não está na lista')
