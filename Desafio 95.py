# Questão: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
dados = {}
gols = []
time = []
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    gols.clear()
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols) # O "sum()" serve para somar tudo que está dentro da lista "gols"
    time.append(dados.copy())
    while True:
        resposta = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print('Responda apenas "S" ou "N"')
    if resposta == 'N':
        break
print('Cod', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro não existe jogador com código {busca}!')
    else:
        print(f'Desempenho do Jogador {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'No jogo {i + 1} fez {g} gols')