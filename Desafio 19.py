# Questão: Um preofessor quer sortear um dos seus quatro alunos para apagar o quadro. FAça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

n1 = input('Digite o primeiro nome de um aluno: ')
n2 = input('Digite o segundo nome de um aluno: ')
n3 = input('Digite o terceito nome de um aluno: ')
n4 = input('Digite um quarto nome de um aluno: ')
l = [n1, n2, n3, n4]
e = random.choice(l)
print('O aluno Escolhido para a escravidão será: {}'.format(e))
