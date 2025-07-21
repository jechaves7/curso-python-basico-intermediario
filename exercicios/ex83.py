#Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. seu aplicativo deverá analisar se a
#expressão passada está com os parenteses abertos e fechados na ordem correta.

expr=str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('sua expressão está correta.')
else:
    print('sua expressão está errada.')