#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando
#ele disser que quer mostrar 0 termos.

print('='*40)
print('Gerador de PA'.center(40))
print('='*40)
primeiro= int(input('Digite o termo:'))
razão= int(input('Digite a razão:'))
termo = primeiro
total=0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -->'.format(termo),end='')
        termo+= razão
        cont += 1
    print('pausa')
    mais = int(input('Quantos termos quer mostrar a mais?'))
print('progressão finalizada com {} termos mostrados.'.format(total))




