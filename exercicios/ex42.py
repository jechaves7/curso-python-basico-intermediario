#Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de trinagulo será formado:
#equilatero: todos os lados iguais
#isosceles: dois lados iguais
#escaleno: todos os lados diferentes

s1=float(input('digite o primeiro segmento:'))
s2=float(input('digite o segundo segmento:'))
s3=float(input('digite o terceiro segmento:'))
if s1<s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('os segmentos acima podem formar triangulo ', end='')
    if s1==s2==s3:
        print('equilatero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isosceles')
else:
     print('os segmentos acima não podem formar triangulo')



























