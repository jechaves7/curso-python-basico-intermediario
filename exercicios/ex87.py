#Aprimore o exercicio anterior, mostrando no final:
#a)a soma de todos os valores pares digitados.
#b)a soma dos valores da terceira coluna.
#c)o maior valor da segunda linha.

matriz = [[0,0,0], [0,0,0], [0,0,0]]
spar=mai=scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('digite o valor para {}, {}'.format(l,c)))
print('-=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c] % 2 == 0:
            spar+=matriz[l][c]
    print()
print('-=-'*30)
print('A soma dos valores pares é {}'.format(spar))
for l in range(0,3):
    scol+=matriz[l][2]
print('a soma da coluna 3 é {}'.format(scol))
for c in range(0,3):
    if c == 0:
        mai=matriz[1][c]
    elif matriz[1][c]>mai:
        mai=matriz[1][c]
print('o maior valor da segunda linha é {}'.format(mai))