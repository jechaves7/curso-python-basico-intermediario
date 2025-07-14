#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem cosniderar os espaços)
#Quantas letras tem o primeiro nome

nome=input('Digite seu nome por favor:').strip()
print('{}, Estou analisando seu nome...'.format(nome))
print('seu nome em maisculo é {}'.format(nome.upper()))
print('seu nome em minusculo é {}'.format(nome.lower()))
print('seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
#print('seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#ou
separa=nome.split()
print('seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
