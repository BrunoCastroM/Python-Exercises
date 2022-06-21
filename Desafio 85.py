# Questão: Crie um programa que o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que matenha sepadarados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.

pares = []
impares = []
principal = []
for n in range(1, 8):
    valor = int(input(f'Digite o {n}º valor: '))
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
principal.append(pares[:])
pares.clear()
principal.append(impares[:])
impares.clear()
principal[0].sort()
principal[1].sort()
print(f'Os valores pares digitados foram: {principal[0]}')
print(f'Os valores ímpares digitados foram: {principal[1]}')

'''Esse exercício também pode ser feito assim:²  (Resolução do professor)

numero = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')'''