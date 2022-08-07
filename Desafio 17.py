# Questão: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da Hipotenusa

'''co=float(input('Digite o valor do cateto oposto do triângulo: '))
ca=float(input('Digite o valor do cateto adjacente do triângulo: '))
h=(co**2+ca**2)**(1/2)
print('O valor do cateto oposto é {} e o do cateto adjacente é {}, e a hipotenusa resulta em {:.2f}'.format(co,ca,h))'''

# Esse exercício também pode ser feito assim:²

import math

co = float(input('Digite o valor do cateto oposto do triângulo: '))
ca = float(input('Digite o valor do cateto adjacente do triângulo: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa será = {:.2f}'.format(hi))

'''Esse exercício também pode ser feito assim:³
from math import hypot
co=float(input('Digite o valor do cateto oposto do triângulo: '))
ca=float(input('Digite o valor do cateto adjacente do triângulo: '))
hi=hypot(co,ca)
print('O valor da hipotenusa será = {:.2f}'.format(hi))'''
