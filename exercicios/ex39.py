#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
#se ele ainda vai se alistar ao serviçi militar, se é a hora de se alistar ou se ja passou do tempo de alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

#nome=input('Digite seu nome:')
#idade=int(input('Digite sua idade:'))
#if idade < 18 :
#    print('vc ainda não está na idade para relizar o alistamento.')
#elif idade > 18:
#    print('Já passou do tempo de alistamento.')
#else:
#    print('Voçê está no prazo de alistamento, CORREEEE!')
#nesse aqui ainda falta informar o tempo.


###ou
import datetime

ano=int(input('Digite seu ano de nascimento:'))
atual=datetime.date.today().year
idade=atual-ano
print('quem nasceu em {} tem {} anos em {}'.format(ano,idade,atual))

if idade < 18 :
    tempo=18-idade
    datadoalistamento=atual + tempo
    print('vc ainda não está na idade para relizar o alistamento. faltam {} anos'.format(tempo))
    print('Seu alistamento será em {}.'.format(datadoalistamento))
elif idade > 18:
    tempo1=idade-18
    datadoalistamento1 = atual - tempo1
    print('Já passou do tempo de alistamento, passou {} anos'.format(tempo1))
    print('Seu alistamento foi em {}.'.format(datadoalistamento1))
else:
    print('Voçê está no prazo de alistamento, CORREEEE!')

#Adicione dps o cadastro só para homens, ja que só eles podem se alistar. e adicione também um tempo para processamento.