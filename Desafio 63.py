# Questão: Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elemtnos de uma Sequência de Fibonacci.
print('Sequência de Fibonacci')
n = int(input('Quantos temos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} → {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c = c + 1
print(' → FIM!!!')