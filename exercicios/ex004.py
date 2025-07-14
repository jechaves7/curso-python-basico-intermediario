###Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela?

a=input('digite algo:')
print('O tipo primitivo desse valor é',type(a))
print('só tem espaços?', a.isspace())
print('é um número?', a.isnumeric())
print('é alfabetico?', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('está em maiusculas?', a.isupper())
print('está em minuscula?', a.islower())
print('está capitalizada?', a.istitle())

