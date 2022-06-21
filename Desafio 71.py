# Questão: Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
# pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai
# informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui
# cédulas de R$50,00, R$20,00, R$ 10,00, R$ 1,00.

print('BANK BRUNO')
v = int(input('Qual valor você quer sacar? R$ '))
t = v
c = 50
tc = 0
while True:
    if t >= c:
        t = t - c
        tc = tc + 1
    else:
        if tc > 0:
            print(f'Total de {tc} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break