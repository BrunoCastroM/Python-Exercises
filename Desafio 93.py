# Questão: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome  do jogador e quantas partidas  ele jogou. DEpois vai ler a quantidade
# de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados = {}
gols = []
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dados['Gols'] = gols[:]
dados['Total'] = sum(gols) # O "sum()" serve para somar tudo que está dentro da lista "gols"
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, v in enumerate(dados['Gols']):
    print(f'    Na partida {i + 1}, fez {v} gols')