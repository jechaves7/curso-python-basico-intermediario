#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes infromações:
#-Quantidade de notas
#-a maior nota
#-a menor nota
#-a média da turma
#-a situação (opcional)
#adicione também as docsstrings.

def notas (*n,sit=False):
    """
    ---> função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r=dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >=7:
            r['situação'] ='Boa'
        elif r['média'] >=5:
            r['situação'] = 'razoável'
        else:
            r['situação'] = 'ruim'
    return r

#p principal

resp=notas (5.5,2.5,1.5, sit=True)
print(resp)
help(notas)