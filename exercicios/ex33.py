#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

#n1=int(input('digite o primeiro número:'))
#n2=int(input('digite o segundo número:'))
#n3=int(input('digite o terceiro número:'))
#print('o valores são:\n{}\n{}\n{}'. format(n1,n2,n3))
#if n1<n2 and n1<n3:
#    print('o menor valor foi {}'.format(n1))
#if n2<n1 and n2<n3:
#   print('o menor valor foi {}'.format(n2))
#if n3<n1 and n3<n2:
#    print('o menor valor foi {}'.format(n3))


#if n1>n2 and n1>n3:
#    print('o maior valor foi {}'.format(n1))
#if n2>n1 and n2>n3:
#    print('o maior valor foi {}'.format(n2))
#if n3>n1 and n3>n2:
#    print('o maior valor foi {}'.format(n3))



#ou
n1=int(input('digite o primeiro número:'))
n2=int(input('digite o segundo número:'))
n3=int(input('digite o terceiro número:'))
menor=n1
if n2<n1 and n2<n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3

maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))














