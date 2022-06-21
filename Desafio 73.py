#Questão: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# 1) Os 5 primeiros; 2) Os últimos 4 colocados.; 3) Times em ordem alfabética; 4) Em que posção esttá o time do Flamengo.
t = ('América-MG', 'Athetico-PR', 'Atlético-Go', 'Avaí', 'Botafogo',
     'Ceará-SC', 'Corinthians', 'Coritiba', 'Cuiabá', 'Flamengo',
     'Fluminense', 'Fortaleza', 'Fluminense', 'Goiás', 'Internacional',
     'Juventude', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo')
print(f'Lista dos time do Brasileirão: {t}')
print(f'Os 5 primeiros são: {t[:5]}')
print(f'Os 4 últimos são: {t[-4:]}')
print(f'Os time em ordem alfabética são: {sorted(t)}')
print(f'O Flamengo está na {len(t[10])}ª colocação') # Jeito mais descomplicado de fazer isso é usando o index para a lista, Ex:

                                                     # print(f'O Flamengo está na {t.index("Flamengo") + 1}ª colocação')

                                                     # Obs: É necessário colocar aspas duplas dentro do index, ou você terá que fazer ele pelo .format, com as aspas duplas "" ele irá intender a interpolação.
