#Crie um programa que tenha uma função chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.

def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano
    if idade<16:
        return f'com {idade} anos: Não vota.'
    elif 16 <=idade < 18 or idade > 65:
        return f'com {idade} anos: voto é opcional.'
    else:
        return f'Com {idade} anos: voto obrigatório.'


#programa principal
nasc=int(input('em que ano vc nasceu? '))
print(voto(nasc))