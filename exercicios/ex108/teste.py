#adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um
#valor monetario formatado.


import moeda

p=float(input('Digite o preço: R$'))
print(f'a metade de  {p} p é  {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de  {p} p é  {moeda.moeda(moeda.dobro(p))}')
