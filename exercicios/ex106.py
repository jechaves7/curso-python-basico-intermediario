#Faça um mini-sistema que utilize o interactive help do python. o usuário vai digitar o comando e o manual vai aparecer.
#quando o usuário digitar a palavra 'fim', o programa vai se encerrará.
#obs: use cores.
from time import sleep
c = ('\033[m',        #0 -sem cor
     '\033[0;30;41m', #1 -cor vermelha
     '\033[0;30;42m', #2 -cor verde
     '\033[0;30;43m', #3 -cor amarelo
     '\033[0;30;44m', #4 -cor azul
     '\033[0;30;45m', #5 -cor roxo
     '\033[0;30;107m'    #6 -cor branca
 );


def ajuda(com):
    titulo(f'acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo (msg, cor=0):
    tam=len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end= '')
    sleep(1)


#p principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyhelp', 2)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)