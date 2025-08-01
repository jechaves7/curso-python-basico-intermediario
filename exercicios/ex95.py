#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
#aproveitamento de cada jogador.
time = list()
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador['nome']=str(input('Digite o nome do jogador: '))
    tot=int(input('Quantos partidas {} jogou?'.format(jogador["nome"])))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input('     quantos gols na partida {}'.format(c+1))))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=-'*30)
print('cod ',end='')
for i in jogador.keys():
    print('{:<15}'.format(i),end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print('{:>3} '.format(k),end='')
    for d in v.values():
        print('{:<15}'.format(str(d)),end='')
    print()
print('-'*30)
while True:
    busca= int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('ERRO! Não existe jogador com código {}!'.format(busca))
    else:
        print(' -- LEVANTAMENTO DO JOGADOR: {}'.format(time[busca]["nome"]))
        for i, g in enumerate(time[busca]['gols']):
            print('    No jogo {} fez {} gols.'.format(i+1,g))
    print('-'*40)
print('<<VOLTE SEMPRE>>')