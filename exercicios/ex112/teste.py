#Dentro do pacote utilidadescev que criamos no exercicio 111, temos um modulo chamado dado. crie uma função chamada
#leiadinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
#valores que sejam monetários.

from utilidadescev import moeda, dado

p=dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p,12,20)
