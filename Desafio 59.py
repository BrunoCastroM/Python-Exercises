# Questão: Crie um programa que leia dois valores e mostre um menu como as opções de baixo:
# [1] Somar; [2] Multiplicar; [3] Maior; [4] Novos números; [5] Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
número1 = (int(input('Digite um número: ')))
número2 = (int(input('Digite outro número: ')))
opção = 0
while opção != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        print('{} + {} = {}'.format(número1, número2, número1 + número2))
    elif opção == 2:
        print ('{} x {} = {}'.format(número1, número2, número1 * número2))
    elif opção == 3:
        if número1 > número2:
            print('Entre {} e {} o maior é {}'.format(número1, número2, número1))
        elif número1 < número2:
            print('Entre {} e {} o maior é {}'.format(número1, número2, número2))
    elif opção == 4:
        print('Informe outros números que você quer!')
        número1 = int(input('Primeiro valor: '))
        número2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida!')
    sleep(1)
print('Programa encerrado!')