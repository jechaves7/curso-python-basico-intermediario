## Faça um programa que leia a largura e a altura de uma parede em metro, calcule a sua areá e a quantidade de
##tinta necessaria para pintá-la, sabendo que cada litro de tinta, pinta uma area de 2m².

a=float(input('qual a altura?'))
l=float(input('qual a largura?'))
ar=a*l
t=ar/2
print('A altura da parede é{}, \n a largura{}, \na are{},\n e a quantidade de tinta gasta é{}.'.format(a,l,ar,t))




