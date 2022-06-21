# Questão: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno cosseno e tangente desse
# ângulo.
import math
an=float(input('Digite o ângulo que você deseja: '))
s=math.sin(math.radians(an))
c=math.cos(math.radians(an))
t=math.tan(math.radians(an))
print('O valor em Seno é: {:.2f}\nO valor em cosseno: {:.2f}\nO valor em tangente é: {:.2f}'.format(s,c,t))

'''Esse exercício também pode ser feito assim:²
from math import radians,sin,cos,tan
an=float(input('Digite o ângulo que você deseja: '))
s=sin(radians(an))
c=cos(radians(an))
t=tan(radians(an))
print('O valor em Seno é: {:.2f}\nO valor em cosseno: {:.2f}\nO valor em tangente é: {:.2f}'.format(s,c,t))'''