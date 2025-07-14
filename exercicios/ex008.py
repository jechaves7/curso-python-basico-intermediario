###crie um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
v=float(input('Distancia em metros:'))
c=v*100
mm=v*1000
print('A distancia em metros é {}, convertido para centimetros fica {} e em milimetros {}.'.format(v, c, mm))
