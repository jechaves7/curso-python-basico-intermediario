#Faça um programa que tenha uma funcção chamada ficha(), que receba dois parametros opcionais: o nome de um jogador e
#quantos gols ele marcou. o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
#sido informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
    print(f'o jogador {jog} fez {gol} gols no campeonato.')


#p principal
n=str(input('nome do jogador: '))
g=str(input('número de gols: '))
if g.isnumeric():
    g=int(g)
else:
    g=0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)