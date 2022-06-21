# Questão: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
# importe esse módulo e use algumas dessas funções.

import def_dasafio107
valor = float(input('Digite um preço: R$ '))


print(f'A metade de R${valor:.2f} é R${def_dasafio107.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${def_dasafio107.dobro(valor):.2f}')
print(f'Aumentando em 10% R${valor:.2f} ficará R${def_dasafio107.aumentar(valor):.2f}')
print(f'Diminuindo em 10% R${valor:.2f} ficará R${def_dasafio107.diminuir(valor):.2f}')

'''
Esse exercício também pode ser feito assim:²
from def_dasafio107 import metade, dobro, aumentar, diminuir

valor = float(input('Digite um preço: R$ '))

print(f'A metade de R${valor:.2f} é R${metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${dobro(valor):.2f}')
print(f'Aumentando em 10% R${valor:.2f} ficará R${aumentar(valor):.2f}')
print(f'Diminuindo em 10% R${valor:.2f} ficará R${diminuir(valor):.2f}')
'''