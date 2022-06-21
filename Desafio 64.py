# Questão: Crie um programa que leia vários números inteiros pelo teclado. O programa só
# vai parar quando o usuário deigitar o valor 999, que é a condição de parada. No Final, mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = 0 # Para simplificar todas essas variáveis podemos escrever assim: n = s = c = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    c = c + 1
    s = s + n
    s1 = s - 999
print('Você digitou {} e a soma entre eles é {}'.format(c - 1, s1))

'''Esse exercício também pode ser feito assim:²
n = c = s = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    c = c + 1
    s = s + n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} e a soma entre eles é {}'.format(c, s))'''