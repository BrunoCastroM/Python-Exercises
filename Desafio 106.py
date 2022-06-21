# Questão: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
# usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: Use cores.
from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;30m'
     );


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[5], end='')
    sleep(1)



def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)

comando = ''
while True:
    titulo('Sistema de ajuda PyHELP!', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)