#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
#mostre uma listagem de preços, organizando os dados em forma tabular.

listagem= ('lapis', 1.75,
           'borracha', 2,
           'caderno', 15.90,
           'estojo', 25,
           'transferidor', 4.20,
           'compasso', 9.99,
           'mocila',120.32,
           'caneta', 22.30,
           'livro', 34.90)
print('-'*40)
print('Listagem de preços'.center(40))
print('-'*40)
for l in range(0,len(listagem)):
    if l % 2 == 0:
        print('{:.<30}'.format(listagem[l]),end= '')
    else:
        print('R$ {:>4.2f}'.format(listagem[l]))
print('-'*40)






