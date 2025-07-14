#Faça um programa que leia um ano qaulquer e mostre se ele é bissexto.
import datetime
ano=int(input('Qual o ano? coloque 0 para analisar o ano atual:'))
if ano ==0:
    ano = datetime.date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('o ano de {} é bissexto'.format(ano))
else:
    print('o ano de {} não é bissexto'.format(ano))











