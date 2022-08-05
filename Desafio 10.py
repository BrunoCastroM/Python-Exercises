# Questão: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input('Digite o valor que você possui em reais: R$'))
c1 = d * 5.33
c2 = d * 6.02
print(f'O seu valor convertido em dólar daria: {c1:.2f}$')
print(f'Seu valor convertido em euro daria:{c2:.2f}€')
