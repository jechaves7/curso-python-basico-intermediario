#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro e mostre uma
#mensagem com tamanho adaptavel.
#ex:
#escreva('olá, mundo!')
#saida:
#~~~~~~~~~~~~
#olá, mundo!
#~~~~~~~~~~~~

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print('  {}'.format(msg))
    print('~'*tam)

escreva ('oi')
escreva ('curso em python')
escreva ('etero')