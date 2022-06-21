# Questão: Crie um programa que faça o computador jogar jokenpô com você.
import random
import time
e=int(input('''Jogue comigo:
[0] Pedra
[1] Papel
[2] Tesoura
Qual você escolherá? '''))
i=('Pedra', 'Papel', 'Tesoura') # Fiz uma lista para substiuir os números pelas palavras
c=random.randint(0,2)
print('\033[31mJO!\033[m')
time.sleep(0.5)
print('\033[32mKEN!!\033[m')
time.sleep(0.5)
print('\033[33mPÔ!!!\033[m')
print('Eu escolhi {}!'.format(i[c])) # nesse .format eu transformei o número do computador ("c") de acordo com a ordem da lista "i"
print('Você escolheu {}!'.format(i[e])) # nesse .format eu transformei o número eu escolhi ("e") de acordo com a ordem da lista "i"
if c==0: # Escolha do computador é Pedra nesse caso de acordo com a lista "i"
    if e==0:
        print('Empatamos!')
    elif e==1:
        print('Você ganhou! Que pena! =/')
    elif e==2:
        print('Eu ganhei! Hu Hu XD')
    else:
        print('\033[31mSó pode escolher: Pedra, Papel ou Tesoura. Assim não dá para jogar!\033[31m')
elif c==1: # Escolha do computador é Papel nesse caso de acordo com a lista "i"
    if e==0:
        print('Eu ganhei! Hu Hu XD')
    elif e==1:
        print('Empatamos!')
    elif e==2:
        print('Você ganhou! Que pena! =/')
    else:
        print('\033[31mSó pode escolher: Pedra, Papel ou Tesoura. Assim não dá para jogar!\033[31m')
elif c==2: # Escolha do computador é Tesoura nesse caso de acordo com a lista "i"
    if e==0:
        print('Você ganhou! Que pena! =/')
    elif e==1:
        print('Eu ganhei! Hu Hu XD')
    elif e==2:
        print('Empatamos!')
    else:
        print('\033[31mSó pode escolher: Pedra, Papel ou Tesoura. Assim não dá para jogar!\033[31m')