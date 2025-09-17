#modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor
#retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda

p=float(input('Digite o preço: R$'))
print(f'a metade de  {p} p é  {moeda.metade(p, True)}')
print(f'o dobro de  {p} p é  {moeda.dobro(p, True)}')
