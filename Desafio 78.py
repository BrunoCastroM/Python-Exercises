# Questão: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
l = []
for c in range(0,5):
    l.append(int(input('Digite um número: ')))
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {max(l)} na(s) posições', end=' ')
for i, v in enumerate(l):
    if v == max(l):
        print(f'{i + 1}...',end=' ')
print()
print(f'O menor valor digitado foi {min(l)} na(s) posições', end=' ')
for i, v in enumerate(l):
    if v == min(l):
        print(f'{i + 1}...', end=' ')


'''Esse exercício também pode ser feito assim:²  (Resolução do professor)
l = []
ma = me = 0
for c in range(0,5):
    l.append(int(input(f'Digite um valor:')))
    if c == 0:
        ma = me = l[c]
    else:
        if l[c] > ma:
            ma = l[c]
        if l[c] < me:
            me = l[c]
print(f'Você digitou os valores {l}')
print(f'O maior valor digitado foi {ma} nas posições: ',end='')
for i, v in enumerate(l):
    if v == ma:
        print(f'{i + 1}...',end='')
print()
print(f'O menor valor digitado foi {me} nas posições: ',end='')
for i, v in enumerate(l):
    if v == me:
        print(f'{i + 1}...',end='')'''