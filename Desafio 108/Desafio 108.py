#Questão: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

from def_dasafio108 import metade, dobro, aumentar, diminuir, moeda

valor = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda(valor)} é {moeda(metade(valor))}')
print(f'O dobro de {moeda(valor)} é R${moeda(dobro(valor))}')
print(f'Aumentando em 10% o valor de {moeda(valor)} ficará {moeda(aumentar(valor))}')
print(f'Diminuindo em 10% o valor de {moeda(valor)} ficará {moeda(diminuir(valor))}')
