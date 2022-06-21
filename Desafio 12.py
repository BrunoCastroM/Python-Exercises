# Questão: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
v=float(input('Valor do produto:R$ '))
p=v-(v*0.05)
print('O produto com 5% de desconto sairá por:R$ {:.2f}'.format(p))
