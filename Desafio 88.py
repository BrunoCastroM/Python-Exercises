# Questão: Faça um programa que ajude um jogador da megasena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60,
# para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
total = 1
vezes = int(input('Quantos jogos você quer que eu sorteie? '))
while vezes >= total:
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'Sorteando os {vezes} jogos!')
for i, l in enumerate(jogos):
    print(f'Jogo: {i + 1}: {l}')
    sleep(0.5)