# Questão: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

d = datetime.date.today().year
n = int(input('Digite o seu ano de nascimento: '))
i = d - n
print('Quem nasceu em {} tem {} anos em {}'.format(n, i, d))
if i == 18:
    print('Você tem que se alistar imediatamente!')
elif i < 18:
    i1 = 18 - i
    print('Ainda faltam {} anos para alistamento'.format(i1))
    a1 = d + i1
    print('Seu alistamento será em {}'.format(a1))
elif i > 18:
    i2 = i - 18
    print('Você já deveria ter se alistado há {} anos'.format(i2))
    a2 = d - i2
    print('Seu alistamento foi em {}'.format(a2))


'''Esse exercício também pode ser feito assim:(Esse foi eu que fiz)²
import datetime
a=int(input('Em que ano você nasceu? '))
d=datetime.date.today().year
a1=d-a
a2=a1-18
a3=18-a1
a4=d+(18-a1)
a5=d-(a1-18)
print('Quem nasceu em {} tem {} anos em {}.'.format(a,a1,d))
if a1>18:
    print('Você já fez o alistamento? Pois você já deveria ter feito isso há {} anos.'.format(a2))
elif a1<18:
    print('Faltam {} anos para o alistamento.'.format(a3))
if a4>=2022:
    print('Seu alistamento será em {}'.format(a4))
else:
    print('Seu alistamento foi em {}'.format(a5))'''
