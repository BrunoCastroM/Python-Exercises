# Questão: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai
# colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteio(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for contador in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é: {soma}')


numeros = []
sorteio(numeros)
somapar(numeros)