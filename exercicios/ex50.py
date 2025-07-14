# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que foram pares.
# se o valor digitado for impar, desconsidere-o.

valor=0
cont=0
for num in range (1,7):
    num = int(input('Digite o {} valor:'.format(num)))
    if num % 2 == 0:
        valor = valor + num
        cont= cont + 1
print('vc informou {} numeros pares e sua soma foi {}'.format(cont, valor))