# Questão: Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas e minúsculas; Quantas letras no total (sem considerar espaços); Quantas letra tem o primeiro nome.

n = input('Digite seu nome completo: ').strip()
print('Seu nome em letras maiúsculas ficará assim: {}'.format(n.upper()))
print('Seu nome em letras minúsculas ficará assim: {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n)-n.count(' ')))
s = n.split()
print('Seu primeiro nome é {} e ele tem {}'.format(s[0], len(s[0])))
