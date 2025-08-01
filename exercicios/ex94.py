#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
#os dicionários em uma lista. No final, mostre:
#a)Quantas pessoas cadsastradas
#b)A média de idade.
#c) Uma lista com mulheres.
#d) uma lista com idade acima da média.
galera = list()
pessoa = {}
soma=média=0
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Digite seu nome: '))
    while True:
        pessoa['sexo']=str(input('Digite seu sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('erro! Responda M ou F.')
    pessoa['idade']=int(input('Digite sua idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp=str(input('Quer Continuar? [S/N]')). upper()[0]
        if resp in 'SN':
            break
        print('Erro! responda S ou N.')
    if resp == 'N':
        break
print('-=-'*30)
print('A) Ao todo temos {} pessoas cadastradas.'.format(len(galera)))
média = soma/len(galera)
print('B) A média de idade é de {:5.2f} anos.'.format(média))
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print('{}'.format(p["nome"]),end='')
print()
print('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('      ',end='')
        for k, v in p.items():
            print('{} = {}; '.format(k,v),end='')
        print()
print('<<Encerrado>>')