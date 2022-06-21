# Questão: Crie um programa que leia vários números inteiros pelo teclado. No final da
# Excução, mostre  a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usu'rio se ele quer ou nao continuar a digitar valores.
r = 's'
n = c = s = ma = me = 0
while r == 's':
    n = int(input('Digite um número: '))
    c = c + 1
    s = s + n
    if c == 1: # Essa parte do if é para mostrar qual é o maior e o menor número digitado.
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
    r = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
print('Foram {} números digitados e a média entre eles é {:.1f}'.format(c, s/c))
print('O maior valor foi {} e o menor valor foi {}'.format(ma,me))