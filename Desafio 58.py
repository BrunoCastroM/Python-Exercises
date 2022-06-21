# Questão: Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre
# 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final
# quantos plapites foram necessários para vencer.
from random import randint
computador = randint(0,10)
acertou = False
palpite = 0
while not acertou:
    numero = int(input('Em que número eu pensei de 0 a 10? '))
    palpite = palpite + 1
    if computador == numero:
        acertou = True
    else:
        if numero < computador:
            print('Mais!')
        if numero > computador:
            print ('Menos!')
print ('Acertou!, você precisou de {} tentantivas para isso.'.format(palpite))
