#Questão: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
n=int(input('Digite um número: '))
if n%2==0: #Para saber se o número é par ou impar é só dividir o número por 2 e verificar o resto da divisão, se for = 0, então é par, já se for ímpar será sempre o resto = 1
    print('Par')
else:
    print('Ímpar')