# Questão: Desenvolva um programa que leia as duas llnotas de um aluno, calcule  e mostre a sua média.

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
m = (n1 + n2) / 2
print('A sua média é = {:.2f}'.format(m))
