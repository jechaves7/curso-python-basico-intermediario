#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
#boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
    nome = str(input('nome:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1,nota2], media])
    resp=str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=-'*30)
print(f'{"No.":<4}{"nome":<10}{"média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=-'*35)
    opc=int(input('Mostrar quais notas dos alunos? (999 interrompe): '))
    if opc == 999:
        print('finalizando...')
        break
    if opc <= len(ficha) -1 :
        print(f'notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')












