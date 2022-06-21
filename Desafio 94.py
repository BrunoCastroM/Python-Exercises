# Questão: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# 1) Quantas pessoas foram cadastradas; 2) A média de idade; 3) Uma lista com as mulheres; 4) Uma lista de pessoas com idade acima da média.
galera = []
pessoa = {}
soma_das_idades = 0
divisor = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('Por favor, digitar apenas "M" ou "F"')
    pessoa['Idade'] = int(input('Idade: '))
    soma_das_idades += pessoa['Idade']
    divisor += 1
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? (S/N): ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Por favor, digitar apenas "S" ou "N"')
    if resposta == 'N':
        break
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma_das_idades / divisor
print(f'A média das idades é: {media:.2f}')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('Lista de pessoas que estão acima da média')
for p in galera:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()