# Questão: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números geradose também
# indique o menor e maior valor que estão na tupla.
from random import randint
ma = 0
me = 0
a = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números são: {a}')
print(f'O maior valor sorteado foi {max(a)}') # Em tuplas, lista e dicionários você pode usar a função "max()" para colocar o maior valor dentro dela e o "min()" para o menor valor.
print(f'O menor valor sorteado foi {min(a)}')