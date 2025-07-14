#### o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
a1=input('nome do aluno 1:')
a2=input('nome do aluno 2:')
a3=input('nome do aluno 3:')
a4=input('nome do aluno 4:')
lista=[a1,a2,a3,a4]
random.shuffle(lista)
print(lista)
