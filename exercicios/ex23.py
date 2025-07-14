#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados.
#ex:
#digite um numero: 1834
#unidade: 4 dezena:3 centanas:8 e milhar:1

num=int(input('Digite um número:'))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('possui {} unidades'.format(u))
print('possui {} dezenas'.format(d))
print('possui {} centenas'.format(c))
print('possui {} milhar'.format(m))


#ou
#num=int(input('Digite um número:'))
#n1=str(int(10000+num))
#print('o numero {}, possui {} unidades'.format(num,n1[4]))
#print('o numero {}, possui {} dezenas'.format(num,n1[3]))
#print('o numero {}, possui {} centenas'.format(num,n1[2]))
#print('o numero {}, possui {} milhar'.format(num,n1[1]))
