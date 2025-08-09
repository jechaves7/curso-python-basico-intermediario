#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (largura
# e comprimento) e mostre a área do terreno.

def área(larg,comp):
    área=larg*comp
    print('A área de um terreno de {} de largura e {} de comprimento é {} m².'.format(larg,comp,área))


print('Controle de terrenos')
print('-=-'*7)

l = float(input('largura (m): '))
c = float(input('comprimento (m): '))
área(l,c)