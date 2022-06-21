# Questão: Apromore o desafio anterior, mostrando no final: 1) A soma de todos os calores pares, digitados; 2) A soma dos valores da terceira coluna; 3) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_dos_pares = soma_terceira_coluna = maior_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_dos_pares += matriz[linha][coluna]
        print(f'{matriz[linha][coluna]:^5}', end='')
    print()

print(f'A soma dos valores pares digitados é {soma_dos_pares}')

for linha in range(0,3):
    soma_terceira_coluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é: {soma_terceira_coluna}')

for  coluna in range(0, 3):
    if coluna == 0:
        maior_segunda_linha = matriz[1][coluna]
    if matriz[1][coluna] > maior_segunda_linha:
        maior_segunda_linha = matriz[1][coluna]
print(f'O maior valor da segunda linha é: {maior_segunda_linha}')