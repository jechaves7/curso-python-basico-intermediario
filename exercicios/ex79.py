#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o numero já
#exista lá dentro, ele não será adicionado. no final, serão exibidos todos os valores únicos digitados, em ordem
#crescente.
from os import remove

#lista=[]
#continuar=' '
#while True:
#    n=(int(input('digite um valor:')))
#    if n not in lista:
#        lista.append(n)
#    continuar=input('Quer continuar? [S/N]:').upper().strip()[0]
#    if continuar == 'S':
#        n = (int(input('digite um valor:')))
#        if n not in lista:
#            lista.append(n)
#        continuar = input('Quer continuar? [S/N]:').upper().strip()[0]
#    if continuar == 'N':
#        break
#    if continuar != 'N' and continuar != 's':
#        print('error! execute novamente o aplicativo.')
#print('obrigado e tente novamente')
#print('os números digitados foram {}'.format(sorted(lista)))

#ouu

números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('valor duplicado! não vou adicionar...')
    r=str(input('quer continuar? [S/N]'))
    if r in 'Nn':
        break
print('-='*30)
números.sort()
print('você digitou os valores {}'.format(números))