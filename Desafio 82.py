# Questão: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
l1 = []
l2 = []
l3 = []
while True:
    n = (int(input('Digite um número: ')))
    l1.append(n)
    if n % 2 == 0:
        l2.append(n)
    else:
        l3.append(n)
    p = ' '
    while p not in 'sn':
        p = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if p == 'n':
        break
print(f'A lista completa é: {l1}')
print(f'A lista de pares é: {l2}')
print(f'A lista de ímpares é: {l3}')




'''Esse exercício também pode ser feito assim:² (Resolução do professor)
l1 = []
l2 = []
l3 = []
while True:
    l1.append((int(input('Digite um número: '))))
    p = ' '
    while p not in 'sn':
        p = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if p == 'n':
        break
for i, v in enumerate(l1):
    if v % 2 == 0:
        l2.append(v)
    else:
        l3.append(v)
print(f'A lista completa é: {l1}')
print(f'A lista de pares é: {l2}')
print(f'A lista de ímpares é: {l3}')'''