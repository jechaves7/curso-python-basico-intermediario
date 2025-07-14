#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
#categoria, de acordo com a sua idade:
#até 9 anos : mirim
#até 14 ano: infantil
#até 19 anos: junior
#até 25 anos: senior
#acima: master

import datetime

ano=int(input('Digite o ano de nascimento:'))
idade=  datetime.date.today().year - ano
print('você que nasceu em {} tem {} anos'.format(ano,idade))
print('dessa forma vc se enquadra na categoria:',end='')
if idade <= 9:
    print('mirim')
elif idade > 9 and idade <= 14:
    print('infantil')
elif idade >14 and idade <= 19:
    print('junior')
elif idade > 19 and idade <=25:
    print('senior')
elif idade > 25:
    print('master')

print('obrigado pela participação!')



























































