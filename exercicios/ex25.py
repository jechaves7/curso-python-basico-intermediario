#Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome.

nome= input('Qual o seu nome?').strip()
n1=' Silva' in nome
print('Seu nome tem silva? {}'.format(n1))
