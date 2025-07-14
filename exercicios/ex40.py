#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
#a média atingida:
#média: 5.0: reprovado
#média entre 5.0 e 6.9: Recuperação
#média 7.0 ou superior: aprovado.

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
print('Sua média foi {}'.format(m))
if m < 5:
    print('infelizmente vc foi reprovado!')
elif m > 5 and m < 6.9:
    print('Você foi para a recuperação!')
elif m >= 7:
    print('Parabéns, vc foi aprovado!')


