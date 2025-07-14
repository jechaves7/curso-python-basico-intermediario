#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

#f=input('Digite a frase:').strip().upper()
#palavras=f.split()
#junto= ''.join(palavras)
#inverso= ''
#for letra in range(len(junto)-1, -1,-1):
#    inverso += junto[letra]
#print(junto,inverso)
#if junto == inverso:
#    print('é um palindromo')
#else:
#    print('não é palindromo')


#ou
f=input('Digite a frase:').strip().upper()
palavras=f.split()
junto= ''.join(palavras)
inverso= junto[::-1]
print(junto,inverso)
if junto == inverso:
    print('é um palindromo')
else:
    print('não é palindromo')