# Questão: desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
s=0
c=0
for n in range(0,7):
    n1=int(input('Digite um número (Somarei apenas aqueles que foram par): '))
    if n1%2==0:
        s=s+n1
        c=c+1
print('Você digitou {} números pares que e a soma deles deu {}'.format(c,s))