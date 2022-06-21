# Questão: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.
d=float(input('Digite o valor que você possui em reais: R$'))
c1=d*5.33
c2=d*6.02
print('O seu valor convertido em dólar daria: {:.2f}$'.format(c1))
print('Seu valor convertido em euro daria:{:.2f}€'.format(c2))