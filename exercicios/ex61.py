#Refaça o desafio 051, lendo o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressão
#usando a estrutura while.

print('='*40)
print('10 primeiros termos de uma PA'.center(40))
print('='*40)
primeiro= int(input('Digite o termo:'))
razão= int(input('Digite a razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -->'.format(termo),end='')
    termo+= razão
    cont += 1
print(' FIM')