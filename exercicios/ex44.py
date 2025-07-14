#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
#condição de pagamento:
# á vista dinheiro / cheque: 10% desconto.
#á vista no cartão: 5% desconto.
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('loja guanabara'))

p= float(input('preço das compras:'))
print('''formas de pagamentos
[1] - á vista dinheiro / cheque
[2] - á vista no cartão
[3] - 2x no cartão
[4] - 3x no cartão''')
o=int(input('Qual é a opção?'))
if o == 1:
    total= p - (p*10/100)
    print('voçê comprou á vista e teve 10% de desconto. O preço a pagar com o desconto custa {} R$'.format(total))
elif o == 2:
    total1= p -(p*5/100)
    print('voçê comprou no cartão a vista e teve 5% de desconto. O preço a pagar com o desconto custa {} R$'.format(total1))
elif o == 3:
    x2= p/2
    print('Sua compra foi parcelada em 2x de {}'.format(x2))
    print('voçê comprou no cartão parcelando em 2x e o preço se mantém o normal, que custa {}'.format(p))
elif o == 4:
    total2= p + (p*20/100)
    totalparc=int(input('Quantas parcelas?'))
    parcelas= total2 /totalparc
    print('Sua compra foi parcelada em {}x de {} R$ com juros '.format(totalparc,parcelas))
    print('Sua compra de R$ {} vai custar {} no final'.format(p,total2))
else:
    print('Opção inválida, tente novamente!!!')
print('Obrigado pela preferencia!!!!!!')




































