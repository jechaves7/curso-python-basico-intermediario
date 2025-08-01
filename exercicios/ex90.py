#Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
#o conteúdo da estrutura na tela.

aluno = {}
aluno['nome']=str(input('Digite o seu nome: '))
aluno['media']=float(input('Digite a média de {}'.format(aluno['nome'])))
if aluno['media'] <= 4:
     aluno['situação']='reprovado'
if aluno['media'] > 4 and aluno['media'] < 7:
    aluno['situação']='recuperação'
if aluno['media'] >= 7:
    aluno['situação']='aprovado'
print('-=-'*50)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')