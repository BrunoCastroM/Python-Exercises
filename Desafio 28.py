# Questão: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time

n = int(input('Em que número de 0 a 5 eu pensei? '))
n1 = random.randint(0, 5)
print('Loading...')
time.sleep(2)
if n == n1:
    print('Parabéns, você acertou és um gênio da lâmpada!!!')
else:
    print('Infelizmente você errou =/, eu pensei no número {}'.format(n1))
