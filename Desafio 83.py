# Questão: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.
e = str(input('Digite uma expressão matemática qualquer: '))
l = []
for s in e:
    if s == '(':
        l.append('(')
    if s == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão está válida!!!')
else:
    print('Sua expressão está errada!!!')