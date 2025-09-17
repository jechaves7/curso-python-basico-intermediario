#Crie um pequeno sistema modularizado que permita cadastar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

arq='cursoeemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['ver pessoas cadastradas', 'cadastrar novas pessoas','sair do sistema'])
    if resposta == 1:
    #opção de listar um conteúdo de um arquivo!
        lerarquivo(arq)
    elif resposta == 2:
    #opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome=str(input('nome:'))
        idade=leiaint('idade:')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        #opção para sair do programa
        cabeçalho('Saindo do sistema... até logo!')
        break
    else:
        print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(2)