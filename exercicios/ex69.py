#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa devará perguntar
#se o usuário quer ou não continuar. No final, mostre:
#a)quantas pessoas tem mais de 18 anos.
#b)quantos homens foram cadastrados.
#c)quantas mulheres tem menos de 20 anos.

print('-'*40)
print('Cadastre uma pessoa'.center(40))
print('-'*40)
acumulador=0
maiores=0
homens=0
mulheresmenos20=0
while True:
    idade=int(input("idade:"))
    sexo=' '
    while sexo not in'MF':
        sexo=str(input('Sexo: [M/F]:')).upper().strip()[0]
    if idade > 18:
        maiores+=1
    if sexo == 'M':
        homens+=1
    if idade < 20 and sexo == 'F':
         mulheresmenos20+=1

    print('-' * 40)
    continuar=' '
    while continuar not in 'S/N':
        continuar=input('quer continuar? [S/N]').upper().strip()[0]
    if continuar == 'N':
        break
print('{} pessoas tem mais de 18 anos \n{} são homens \n{} são mulheres com menos de 20 anos.'.format(maiores,homens,mulheresmenos20))


#print('Finalizado')


























