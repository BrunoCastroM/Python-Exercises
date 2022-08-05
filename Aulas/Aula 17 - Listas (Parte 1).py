lanche = ['Pizza', 'Pudim', 'Suco', 'Hámburguer'] # A listas são representadas pelos parenteses "[]". A difrença entre esta e as tuplas é que as listas não imutáveis.


###################### Trocando itens na lista ######################

lanche[2] = 'Picolé' # aqui ele irá trocar o item na posição 2 que seria o 'suco', pois começa a contagem do 0.


###################### Adicionando itens na lista (append() e insert()) ######################

lanche.append('Pão') # Para eu adicionar algo no final da lista eu utilizo o comando "append()", que seria acrescentar em português.

lanche.insert(1, 'Salsicha') # O "insert()" serve para inserir 1 item na lista, e escolher onde ele irá ficar na lista.


###################### Apagando itens na lista (del, pop() e remove() ######################

# Obs: Nessa sessão ele irá eliminar o item e o seu indicador, reorganizando todos os outros que não foram excluídos.

del lanche[5] # O comando "del" serve para apagar a lista, neste caso eu fiz ele apagar o 5 item da lista que seria o "Pão" que eu adicionei em cima.

lanche.pop(5) # Mesma coisa do comando "del" só que usando o "pop()" agora. Obs: Se você não indicar o item que você quer apagar ele vai apagar somente o último.

lanche.remove('Pudim') # Aqui ele irá remover o valor que você indicou. Obs: não importa se foi número ou letra, e se na lista tiver itens repetidos ele só remove o primeiro item.

if 'Pizza' in lanche: # Aqui é se tiver "Pizza" em "Lanche" vai ser tirada
    lanche.remove('Pizza')


###################### Ordenando uma lista (sort() e reverse=True######################

números = [2, 6, 8, 10, 1, 3, 5, 4, 7] # Usando o comando "sort()", eu irei ordenar os itens da lista.
números.sort()
números.sort(reverse=True) # Se eu usar o "reverse = True" dentro do "sort()" ele irá inverter a ordem
print(números)
print(len(números)) # Usando o "len()" ele irá contar quanto itens tem na lista

###################### Outra forma de criar uma lista (list()) ######################

valores = list(range(4, 11)) # Aqui é uma outra forma de criar uma lista, lembrando que no range ele elimina o último.
print(valores)


###################### Usando estruturas de condição e repetição com listas ######################

n = [2, 5, 7, 8, 7, 10, 11]

if 7 in n: # Aqui é se tiver um "7" dentro do "n" ele irá remover
    n.remove(7)
print(n)

while 7 in n: # Aqui é enquanto o "7" estiver dentro do "n" ele irá remover todos os 7 que estiverem na lista "n"
    n.remove(7)
print(n)

valores = [] # aqui eu adicionei valores a lista e pedi para ele colocar cada valor por meio do "for".
valores.append(2)
valores.append(6)
valores.append(7)

for v in valores:
    print(f'{v}...', end='')

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')

números = list() # Aqui eu estou acrescentando 5 números na lista (que está vazia) que estão sendo perguntandos.
for t in range(0, 5):
    números.append(int(input('Digite um valor: ')))
for c, v in enumerate(números): # e aqui eu estou printando a posição e o valor que foi digitado na ordem.
    print(f'Na posição {c} encontrei o valor {v}')


###################### Outras funcionalidades ######################

a = [1, 3, 5, 6, 8]
b = [2, 4, 7, 9, 10]

b = a # desa forma o número 8 sairá nas duas lista, pois o python faz uma ligação entre as duas listas
b[2] = 8
print(a)
print(b)

b = a[:] # Então para eu criar uma cópia, ou seja, eu alterar uma lista sem alterar a outra eu devo colocar "[:]"
b[2] = 8
print(a)
print(b)

