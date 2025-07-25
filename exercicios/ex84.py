#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a) Quantas pessoas foram cadastradas.
#b) uma listagem com as pessoas mais pesadas.
#c) uma listagem com as pessoas mais leves.

#lista = []
#continuar = ' '
#totalpessoas=0
#while True:
#    nome = str(input('Digite o nome da pessoa: '))
#    idade = int(input('Digite a idade: '))
#    lista.append(nome)
#    lista.append(idade)
#    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
#    if continuar == 'S':
#        nome = str(input('Digite o nome da pessoa: '))
#        idade = int(input('Digite a idade: '))
#        lista.append(nome)
#        lista.append(idade)
#       continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
#    if continuar == 'N':
#        print('fim. Obrigado!')
#        break

#print(lista)
#print('-=-'*30)
#print('foram cadastradas {} pessoas.'.format(totalpessoas))
#print('as pessoas mais pesadas são {}')
#print('as pessoas mais leves são {}')

#ou
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        mai=men=temp[1]
    else:
        if temp[1]>mai:
            mai=temp[1]
        if temp[1]<men:
            men=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp= input('Quer continuar? [S/N]').upper().strip()[0]
    if resp in 'Nn':
        break
print('-=-'*30)
print(princ)
print('foram cadastradas {} pessoas'.format(len(princ)))
print('as pessoas mais pesadas foram {} kg. peso de'.format(mai), end=' ')
for p in princ:
    if p[1] == mai:
        print('{}'.format(p[0]), end=' ')
print()
print('as pessoas mais leves são {} kg. peso de'.format(men), end=' ')
for p in princ:
    if p[1] == men:
        print('{}'.format(p[0]), end=' ')
print()

