# Questão: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. no final, mostre um boletim contendo uma média de cada um e permita
# que o usuário possa mostrar as notas de cada aluno individualmente.
lista = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])
    escolha = ' '
    while escolha not in 'sn':
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    opcao = int(input(('Mostrar notas de qual aluno? (999 Interrompe): ')))
    if opcao == 999:
        print('Finished')
        break
    if opcao <= len(lista) - 1:
        print(f'As notas de {lista[opcao][0]} são {lista[opcao][1]}')
print('Check back ofter!')

