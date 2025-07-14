#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo.
print('-=-'*9)
print('Analisador de triangulos')
print('-=-'*9)

s1=float(input('digite o primeiro segmento:'))
s2=float(input('digite o segundo segmento:'))
s3=float(input('digite o terceiro segmento:'))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('os segmentos acima podem formar triangulo')
else:
    print('os segmentos acima não podem formar triangulo')



























