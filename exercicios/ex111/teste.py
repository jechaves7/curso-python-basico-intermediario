#Crie um pacote chamado utilidadescev que tenha dois modulos internos chamados moeda e dado. Transfira todas as funções
#utilizadas nos desafios 107, 108, e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadescev import moeda, dado

p=float(input('Digite o preço: R$'))
moeda.resumo(p,12,20)
help(moeda)