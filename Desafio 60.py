#Questão: Faça um programa que leia um número qualquer e mostre seu fatorial. Ex: 5! =
# 5 x 4 x 3 x 2 x 1 = 120
'''Esse exercício também pode ser feito assim:²
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é = {}'.format(n, f))'''

n = int(input('Digite um número para calcular o seu fatorial: '))
f = 1
for n in range(n, 0, -1):
    f = f * n
    n = n - 1
print('Seu fatorial é {}'.format(f))

'''Esse exercício também pode ser feito assim:³
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c = c - 1
print('{}'.format(f))'''