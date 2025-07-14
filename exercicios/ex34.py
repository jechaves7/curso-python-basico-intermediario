#Escreva um programa que pergunte qual o salario do funcionario e calcule o valor de seu aumento.
#para salarios superiores a R$ 1.250.00, calcule um aumento de 10%.
#para os inferiores ou iguais, o aumento de 15%.

f=float(input('Digite o seu salário:'))
if f<=1250:
    novo=f+(f*15/100)
else:
    novo=f+(f*10/100)
print('quem ganhava {} agora ganhará {}'.format(f,novo))















