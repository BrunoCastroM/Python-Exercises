dados = {'nome': 'Pedro', 'idade': '29'} # Os dicionários são representados por "{ }".

print(dados['nome']) # Aqui vai sair o nome do "Pedro".
print(dados['idade'])

dados['sexo'] = 'Masculino' # Essa é a forma que se adiciona um dado em um dicioário. Em vez de adcionar pelo comando "append()". Nesse caso ele irá criar o dado "sexo" e colocará no final dele.


############################## Eliminando Dados de um Dicioário ##############################

del dados['idade'] # Aqui dentro dos dados ele irá deletar a idade.


############################## Extraindo Dados de um Dicionário ##############################

filme = {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}

print(filme.values()) # Aqui só vai aparecer os valores e não as chaves ("Star Wars", "1977", "George Lucas").
print(filme.keys()) # Aqui só vai aparecer as chaves ("titulo", "ano", "diretor").
print(filme.items()) # Aqui vai aparecer todos os itens dentro do dicionário.

for k in filme.keys(): # Aqui vai ser criado um laço que vai mostrar todas as chaves.
    print(f'O {k}')

for v in filme.values(): # Aqui vai ser criado um laço que vai mostrar todos os valores.
    print(f'O {v}')

for k, v in filme.items(): # Aqui vai ser criado um laço que vai mostrar todos os itens dentro do dicionário na ordem. O "items()" se comporta da mesma maneira que o "enumerate()"
    print(f'O {k} é {v}')

filmes = [{'titulo': 'Vigadores', 'ano': '2012', 'diretor': 'Joss Whedon'}, {'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}, {'titulo': 'Matrix', 'ano': '1999', 'diretor': 'George Wachowski'}]
# Em cima foi criado uma lista, que dentro dela tem dicionários.

print(filmes[0]['ano']) # Aqui eu pegaria dentro do íncice 0 da lista que seria o dicionário dos vingadores e sairia "2012".
print(filmes[2]['titulo']) # Aqui sairia "matrix".

brasil = []
estado1 = {'UF':'Teresina', 'Sigla': 'PI'}
estado2 = {'UF':'Fortaleza', 'Sigla': 'CE'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[0]['Sigla'])
print(brasil[1]['UF'])
print(brasil[1]['Sigla'])

pais = list()
federacao = dict()

for c in range(0, 2):
    federacao['UF'] = str(input('Uniade Federativa: '))
    federacao['Sigla'] = str(input('Sigla do Estado: '))
    pais.append(federacao.copy())  # Em vez de usar "[:]" para fazer a cópia que nem na lista, quando o item vem de um dicionário (como neste caso) e eu quero colocar dentro da lista eu tenho que utilizar a função ".copy()".
#print(pais)

for e in pais:
    print(e)
    for k in e.keys(): # Aqui ele irá mostar "UF" e "Sigla"
        print(k)
    for v in e.values(): # Aquei ele irá mostrar o valor que você digitou nos input.
        print(v)
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')