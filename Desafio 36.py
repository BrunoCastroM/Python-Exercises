# Questão: Escreva um programa para aprovaar o empréstimo bancário para compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Qual o valor da casa? '))
s = float(input('qual o valor do seu salário? '))
a = int(input('Em quantos anos você deseja pagar a casa? '))
v1 = (c / a) / 12
v2 = s * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(
    c, a, v1))
if v1 <= v2:
    print('Parabéns, você poderá fazer o empréstimo para comprar sua casa própria')
else:
    print('Infelizmente não poderá retirar o empréstimo')
