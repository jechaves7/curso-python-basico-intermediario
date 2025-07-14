#Crie um programa que leia dois valores e mostre um menu como o ao lado na tela: Seu programa deverá realizar a
#operação solicitada em cada caso.
# 1- somar
# 2- multiplicar
# 3- maior
# 4- novos numeros
# 5- sair do programa


v1=float(input('Digite o primeiro valor:'))
v2=float(input('Digite o segundo valor:'))
opcao=0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao=int(input('>>>>>> Qual é a sua opção?'))
    if opcao == 1:
        soma = v1 + v2
        print('A soma dos valores é {:.0f}'.format(soma))
    elif opcao == 2:
        produto= v1*v2
        print('A multiplicação dos valores é {:.0f}'.format(produto))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior dos valores é {:.0f}'.format(maior))
    elif opcao == 4:
        print('informe os valores novamente:')
        v1 = float(input('Digite o primeiro valor:'))
        v2 = float(input('Digite o segundo valor:'))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opção informada incorretamente, tente novamente.')
    print('=-='*10)
print('voçê saiu do programa.')



