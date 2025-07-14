#Crie um programa que simule o funcionamento de um caixa eletronico. no inicio, pergunte ao usuario qual será o valor
#a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#obs: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 em R$ 1.


print('='*40)
print('BANCO CEV'.center(40))
print('='*40)

valor=int(input('Que valor você quer sacar? R$ '))
total=valor
céd=50
totcéd=0
while True:
    if total >= céd:
        total -= céd
        totcéd+=1
    else:
        if totcéd > 0:
            print('total de {} cédulas de R$ {}.'.format(totcéd,céd))
        if céd == 50:
            céd =20
        elif céd ==20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd=0
        if total== 0:
            break
print('='*40)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
































