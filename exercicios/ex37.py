#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binario
#2 para octal
#3 para hexadecimal

num=int(input('Digite um número inteiro'))
print('''Escolha uma das bases para conversão:
[1]-binário
[2]-octal
[3]-hexadecimal''')
opçaõ=int(input('Escolha um deles para conversão:'))

if opçaõ==1:
    print('o valor {} convertido para binário fica {}'.format(num,bin(num)[2:]))
elif opçaõ==2:
    print('o valor {} convertido para octal fica {}'.format(num, oct(num)[2:]))
elif opçaõ == 3:
    print('o valor {} convertido para hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('Valor inválido, tente novamente!')
