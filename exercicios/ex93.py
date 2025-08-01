#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantos
#partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
#dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas = list()
jogador['nome']=str(input('Digite o nome do jogador: '))
tot=int(input('Quantos partidas jogadas? '))
for c in range(0, tot):
    partidas.append(int(input('     quantos gols na partida {}'.format(c))))
jogador['gols']=partidas[:]
jogador['total']=sum(partidas)
print('-=-'*30)
print(jogador)
print('-=-'*30)
for k, v in jogador.items():
    print('o campo {} tem o valor {}'.format(k,v))
print('-=-'*30)
print('o jogador {} jogou {} partidas.'.format(jogador["nome"],len(jogador["gols"])))
for v, i in enumerate(jogador['gols']):
    print('    => na partida {} fez {} gols.'.format(i,v))
print('foi um total de {} gols.'.format(jogador["total"]))