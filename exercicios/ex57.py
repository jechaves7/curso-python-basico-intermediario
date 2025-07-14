#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'f'. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.
m='m'.upper()
f='f'.upper()
sexo=str(input('qual o sexo? [M/F]:')).upper().strip()[0]
while sexo not in 'mf'.upper():
    sexo=str(input('Dados fornecidos incorretamente, informe novamente seu sexo por favor:')).upper().strip()[0]
print('Sexo {} validado com sucesso.'.format(sexo))


































