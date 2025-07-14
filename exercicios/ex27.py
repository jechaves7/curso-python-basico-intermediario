# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
#EX: Ana Maria de Souza
#primeiro: Ana
#ultimo: souza

n= input('Qual o seu nome?').strip()
nome= n.split()
print('Seu primeiro nome é {}.'.format(nome[0]))
print('seu ultimo nome é {}.'.format(nome[len(nome)-1]))





