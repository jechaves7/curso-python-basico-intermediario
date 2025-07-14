#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#a maioridade e quantas ja são maiores.

import datetime
atual= datetime.date.today().year
totmaior=0
totmenor=0
for pess in range (1,8):
    p1= int(input('Informe o seu ano de nascimento da {}° pessoa'.format(pess)))
    nascimento= atual-p1
    print('essa pessoa tem {} anos'.format(nascimento))
    if nascimento >= 18:
        print('Essa pessoa é maior de idade')
        totmaior += 1
    else:
        print('Essa pessoa não é maior de idade')
        totmenor += 1

print('Ao todo tivemos {} maiores de idade.'.format(totmaior))
print('Ao todo tivemos {} menores de idade.'.format(totmenor))

