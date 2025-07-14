#Desenvolva um programa que pergunte a distancia da viagem em km. Calcule o preço da passagem, cobrando
# R$ 0,50 por km para viagens de até 200km e R$ o,45 para viagens mais longas.

#viagem=float(input('Qual a distancia percorrida?'))
#print('a distancia da viagem é {:.0f} KM.'.format(viagem))
#n1=float(viagem * 0.50)
#n2=float(viagem * 0.45)
#if viagem <= 200:
#    print('o preço a pagar pela viagem foi de {:.2f} R$'.format(n1))
#else:
#    print('o preço a pagar pela viagem foi de {:.2f} R$'.format(n2))

##ou

#distancia=float(input('Qual a distancia da sua viagem?'))
#print('voce está prestes a começar uma viagem de {} km'.format(distancia))
#if distancia <= 200:
#    preço = distancia * 0.50
#else:
#    preço = distancia * 0.45
#print('E o preço da sua passagem vai ser de R$ {}'. format(preço))
#print('obrigado pela preferencia!')


#ouu
distancia=float(input('Qual a distancia da sua viagem?'))
print('voce está prestes a começar uma viagem de {} km'.format(distancia))
preço = distancia*0.50 if distancia <=200 else distancia * 0.45
print('E o preço da sua passagem vai ser de R$ {}'. format(preço))
