# Questão: Faça um programa que leia o nome e o peso de várias pessoas, guardado tudo em uma lista. No final, mostre: 1) Quantas pessoas foram cadastradas. 2) Uma listagem com as pessoas mais pesadas.
# 3) Uma listagem com as pessoas mais leves.
temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('Nome: ')))
    temporaria.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja continuar? [S/N} ')).strip().lower()[0]
    if escolha == 'n':
        break
print(f'Ao todo, você cadastrou {len(principal)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de',end=' ')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end =' ')
print()
print(f'O menor peso foi de {menor}Kg.')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end='')