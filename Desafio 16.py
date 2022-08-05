# Questão: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

import math

n = float(input('Digite um número real: '))
print('A parte inteira desse número é: {}'.format(math.trunc(n)))

'''Esse exercício também pode ser feito assim:²
from math import trunc
n=float(input('Digite um número real: '))
print('A parte inteira desse número é: {}'.format(trunc(n)))'''

'''Esse exercício também pode ser feito assim:³
n=float(input('Digite um número real: '))
print('A parte inteira desse número é: {}'.format(int(n)))'''
