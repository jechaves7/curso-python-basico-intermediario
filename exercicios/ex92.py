#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionario
#se por acaso a ctps for diferente de zero, o dicionario receberá também o ano de contratação e o salário, calcule e
#acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

dicio = {}
import datetime
dicio['nome']=str(input('Digite seu nome: '))
nasc=int(input('Digite o ano de nascimento: '))
dicio['idade']= datetime.datetime.now().year - nasc
dicio['carteira de trabalho']=int(input('Digite sua carteira de trabalho (digite 0 se não houver): '))
if dicio['carteira de trabalho']!= 0:
    dicio['ano da contratação']=int(input('Digite o ano de contratação: '))
    dicio['salário']=float(input('Digite seu salário: '))
    dicio['aposentadoria'] = dicio['idade']+((dicio['ano da contratação'] + 35) - datetime.datetime.now().year)
print('-=-'*30)
for k, v in dicio.items():
    print('{} é {}'.format(k,v))
print('-=-'*30)
