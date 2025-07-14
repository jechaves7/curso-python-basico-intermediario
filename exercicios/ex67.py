#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#o programa será interrompido quando o número solicitado for negativo.

while True:
    print('-'*50)
    t=int(input('digite um número para verificar a tabuada: '))
    print('-' * 50)
    if t < 0:
        break
    for ta in range (0,11):
        print('{} x {} = {} '.format(t,ta,t*ta))
print('Finalizado!')
