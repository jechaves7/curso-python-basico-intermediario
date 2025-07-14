### um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome dos escolhidos.

import random

a1=input('Digite o nome do primeiro aluno:')
a2=input('Digite o nome do segundo aluno:')
a3=input('digite o nome do terceiro aluno:')
a4=input('Digite o noke do quarto aluno:')
lista=[a1,a2,a3,a4]
sorteio=random.choice(lista)
print(sorteio)

