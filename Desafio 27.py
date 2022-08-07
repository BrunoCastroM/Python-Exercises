# Questão: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o priemiro e o último nome separadamento.Ex: Ana Maria de Souza; primeiro = Ana; último = Souza.

n = str(input('Digite seu nome completo: ')).strip()
n1 = n.split()
print('''Seu primeiro nome é: {}
seu último nome é: {}'''.format(n1[0], n1[len(n1) - 1]))
