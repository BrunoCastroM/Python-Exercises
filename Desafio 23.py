# Questão: Faça um programa que leia um número de 0 a 9999 e mostre a na tela cada um dos dígitos separados.Ex:
# Digite um número: 4932
# Unidade: 2 Dezena: 3 Centena: 9 Milhar: 4

n = int(input('Digite um número: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print('Analisando o número {}, é possével definir:'.format(n))
print('Unidade: {}\nDezenas: {}\nCentenas: {}\nMilhares: {}'.format(u, d, c, m))

'''Esse exercício também pode ser feito assim:² (Porém ele não sairá o número 0)
n=int(input('Digite um número: '))
n1=str(n)
print('Analisando o número {}, é possível definir:'.format(n))
print('Unidades: {}\nDezenas: {}\nCentenzas: {}\nMilhares: {}'.format(n1[3],n1[2],n1[1],n1[0]))'''
