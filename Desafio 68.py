# Questão: Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que
# ele consquistou no final do jogo.
from random import randint
v = 0
while True:
    n = int(input('Diga um valor: '))
    a = randint(0, 10)
    t = n + a
    e = ' '
    while e not in 'PI':
        e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador {a}. O total deu {t}',end='. ')
    print('DEU PAR!' if t % 2 == 0 else 'DEU ÍMPAR!') # isso é uma forma de fazer uma estrututura condicional em uma linha só
    if e == 'P':
        if t % 2 == 0:
            print('Você venceu')
            v = v + 1
        else:
            print('Você perdeu!')
            break
    elif e == 'I':
        if t % 2 == 1:
            v = v + 1
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game over!, Você venceu {v} vezes')


'''Esse exercício também pode ser feito assim:² (Minha resolução)

from random import randint
from time import sleep
e = ''
v = 0
while True:
    a = randint(0, 10)
    n = int(input('Diga um valor: '))
    e = str(input('Par ou Ímpar? [P/I] ')).strip().lower()[0]
    if e == 'p':
        if (n + a) % 2 == 0:
            print(f'Você jogou {n} e o computador {a}. O total deu {n + a} e isso é um número PAR')
            print('Parabéns você venceu!')
            v = v + 1
        else:
            print(f'Você jogou {n} e o computador {a}. O total deu {n + a} e isso é um número ÍMPAR')
            print('Infelizmente você perdeu!')
            break
    if e ==  'i':
        if (n + a) % 2 == 1:
            print(f'Você jogou {n} e o computador {a}. O total deu {n + a} e isso é um número ÍMPAR')
            print('Parabéns você venceu!!')
            v = v + 1
        else:
            print(f'Você jogou {n} e o computador {a}. O total deu {n + a} e isso é um número PAR')
            print('Infelizmente você perdeu!')
            break
    sleep(1)
    print('Vamos jogar novamente...')
print(f'Você ganhou {v} veze(s)')'''