# Questão: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre: 1) Qual é o total gasto na compra;
# 2) Quantos produtos custam mais de R$ 1000,00; 3) Qual é o nome do produto mais barato.
print('MEGA SALDÃO!')
s = 0
pr = 0
c = 0
me = 0
ba = ''
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$ '))
    c = c + 1
    s = s + p
    q = ' '
    while q not in 'sn':
        q = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if q == 'n':
        break
    if p > 1000:
        pr = pr + 1
    if c == 1: # Posso simplificar essa parte do preço e nome do produto mais barato escrevendo isso: "if c == 1 or p < me:", ai nesse caso eu tiro o else de baixo.
        me = p
        ba = n
    else:
        if p < me:
            me = p
            ba = n
print(f'Total da compra foi de R${s:.2f}')
print(f'Temos {pr} produto(s) custando mais de R$1000,00')
print(f'O produto mais barato foi o(a) {ba} que custa R${me}')
