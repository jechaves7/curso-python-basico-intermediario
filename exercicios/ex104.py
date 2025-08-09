#Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do python, só que
#fazendo a validação para aceitar apenas um valor númerico.
#ex: leiaint('digite um n')


def leiaint(msg):
    ok = False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print('\033[0;31mErro! Digite um numerp inteiro válido.\033[m')
        if ok:
            break
    return valor




n=leiaint('Digite um número: ')
print(f'você acabou de digitar o número {n}')

