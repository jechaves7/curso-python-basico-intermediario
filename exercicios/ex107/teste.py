#Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade.
#Faça tambem um programa que importe esses modulos e use algumas dessas funções.


import moeda

p=float(input('Digite o preço: R$'))
print(f'a metade de R$ {p} p é R$ {moeda.metade(p)}')

