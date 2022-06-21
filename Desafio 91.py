# Questão: Crie um programa onde 4 jogadores joguem um dado e tenham rasultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem. Sabendo
# que o vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter # Serve para pegar os itens de um dicionário.
jogador = {}
jogador['Jogador 1'] = randint(1, 6)
jogador['Jogador 2'] = randint(1, 6)
jogador['Jogador 3'] = randint(1, 6)
jogador['Jogador 4'] = randint(1, 6)
posicao = {}
for k, v in jogador.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
posicao = sorted(jogador.items(), key=itemgetter(1), reverse=True) # Essa função faz com que os dados dentro do dicionário se torne uma lista, por isso deve-se usar o enumerate ali em baixo em vez do ".items()"
for i, v in enumerate(posicao):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')

'''Esse exercício também pode ser feito assim:²  (Resolução do professor)
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = {}
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')'''