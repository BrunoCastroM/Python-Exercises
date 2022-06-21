# Questão: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas
# vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from def_dasafio109 import moeda

valor = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é R${moeda.dobro(valor, True)}')
print(f'Aumentando em 10%, ficará {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo em 10%, ficará {moeda.diminuir(valor, 10, True)}')
