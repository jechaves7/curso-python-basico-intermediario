#Escreva um programa para aprovar o empréstimo bancario para a compra de uma casa. Pergunte o valor da casa,
#o salario do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salario ou então o emprestimo será negado.

print('-=-'*7)
print('Emprestimo bancário')
print('-=-'*7)

casa=float(input('Qual o valor da casa?'))
salario=float(input('qual o seu salário?'))
anos=int(input('Em quantos anos voçê pretende pagar?'))
prestacao=casa/(anos*12)
minimo=salario*(30/100)
print('para pagar uma casa de {} em {} anos vc deve pagar mensalmente {:.2f}'.format(casa, anos,prestacao))

if prestacao > minimo:
    print('Impossivel fazer o emprestimo pois excedeu 30% do seu salário')
elif prestacao <= minimo:
    print('Prestação feita com sucesso. Agradecemos sua escolha.' , end='')

print('Tenha um bom dia!')





























