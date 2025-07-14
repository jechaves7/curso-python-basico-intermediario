#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
#> a média de idade do grupo.
#> Qual é o nome do homem mais velho.
#> Quantas mulheres tem menos de 20 anos.

somaidade=0
mediaidade=0
maioridade=0
nomevelho = ''
totalmulher20=0
for p in range (1,5):
    print('----- {}° pessoa -----'.format(p))
    nome=input('nome:').strip()
    idade = int(input('idade:'))
    sexo = input('sexo: [M/F]:').strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridade=idade
        nomevelho=nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 +=1

mediaidade += somaidade/4
print('A média de idade do grupo é {} anos'.format(mediaidade))
print('o homem mais velho tem {} anos e se chama {}'.format(maioridade,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totalmulher20))
