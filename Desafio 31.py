# Questão: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.

# d=float(input('Qual é a distância de sua viagem em quilômetros? '))
# v1 = d * 0.5
# v2 = d * 0.45
# if d <= 200:
#     print('O valor a pagar nesta viagem é de: R${:.2f}'.format(v1))
# else:
#     print('O valor a pagar nesta viagem é de: R${:.2f}'.format(v2))

# Esse exercício também pode ser feito assim(de maneira simplificada):²

d = float(input('Qual é a distância de sua viagem em quilômetros? '))
v = d * 0.5 if d <= 200 else d * 0.45
print('O valor a pagar nesta viagem é de: R${:.2f}'.format(v))
