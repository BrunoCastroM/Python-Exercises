# Questão: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: 1) Quantas vezes apareceu o valor 9;  2) Em que posição foi digitado o priemiro valor 3;
# 3) Quais foram os números pares.

n = (int(input('Digite um número: ')),            # Dentro de um input eu já posso fazer uma tupla para deixar sóuma variável para todas.
     int(input('Digite outro número: ')),
     int(input('Digite mais outro número: ')),
     int(input('Digite mais outro número: ')))
print(f'Você digitou os valores: {n}')
print(f'O valor 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor 3 apareceu na posição {n.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados foram: ',end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
