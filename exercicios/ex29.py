#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h,
#mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

#ve=int(input('Qual a velocidade do carro?'))
#if ve >= 80:
#    print('vc foi multado.')
#    print('sua multa é de',ve*7)
#else:
#    print('parabens, voce está diirigindo com segurança!')

###ou
ve=float(input('Qual a velocidade do carro?'))
if ve > 80:
    print('vc foi multado.')
    multa=(ve-80)*7
    print('voçe deve pagar uma multa de {}R$'.format(multa))
print('Tenha um bom dia! dirija com segurança!')
