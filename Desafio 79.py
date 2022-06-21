# Questão: Crie um programa que o usuário possa digitar vários valores numéricos e cadastre-os em um alista. Caso o número já exista lá dentro, ele não será adcionado. No final, serão exbidos
# todos os valores únicos digitados, em ordem crescente.
l = []
while True:
    n = int(input('Digite um valor: '))
    if n not in l:
        l.append(n)
        print('Valor adcionado com sucesso!')
    else:
        print('Valor duplicado não é possivel inserir')
    p = ' '
    while p not in 'sn':
        p = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if p == 'n':
        break
l.sort()
print(f'Você digitou os valores: {l}')