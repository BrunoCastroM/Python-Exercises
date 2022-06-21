# Questão: Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = n
c = 1
while c <= 10:
    print('{} → '.format(t), end='')
    t = t + r
    c = c + 1
print('É isso')