# Questão: Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem: O primeiro valor é maior; o Segundo valor é mior; ou Não existe valor maior, os dois são iguais.

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro valor que você digitou é maior!')
elif n1 < n2:
    print('O segundo valor que você digitou é maior!')
else:
    print('Os dois valores são iguais')
