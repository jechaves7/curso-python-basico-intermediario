#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta
#de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista=[]
for c in range(0,5):
    n=int(input('Digite o {}º valor:'.format(c)))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('adicionado no final da lista')
    else:
        pos=0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print('adicionado na posição {}'.format(pos))
                break
            pos+=1
print('-=-'*30)
print('os valores digitados em ordem foram {}'.format(lista))
