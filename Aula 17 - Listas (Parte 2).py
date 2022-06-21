############################## Aprendendo a fazer listas compostas ##############################

t = []
t.append('Bruno')
t.append(29)
g = []
g.append(t[:]) # Se eu não colocar para criar uma cópia "[:]" da primeira lista que seria a (t), ela iria somente mostar 2 listas com maria e 22, quando eu cria uma cóipia ai sim ele irá mostrar o bruno 29 e maria 22 dentro de uma lista.
t[0] = 'Maria'
t[1] = 22
g.append(t[:])
print(g)

l = [['João', 29], ['Maria', 32], ['Joaquim', 35], ['Bruno', 15]] # Aqui é uma estrutura de uma lista dentro de outra lista (Lista Composta)

print(l[0])

print(l[2][1]) # Aqui ele irá aparecer o índice 2 que seria joaquim 35 e dentro dela eu selecionei o item 1 que seria o 35

for p in l: # vai printar cada lista que tiver dentro de "l"
    print(p)

for p in l:
    print(p[1]) # Vai aparecer a posição 1 de cada lista

for p in l:
    print(f'{p[0]} tem {p[1]} anos de idade')

l = []
d = []

for c in range(0,3):
    d.append(str(input('Nome: ')))
    d.append(int(input('Idade: ')))
    l.append(d[:]) # Aqui eu criei uma cópia da lista "d" e acrescentei na lista "l".
    d.clear() # Serve para excluir a lista a lista "d".
print(l)

ma = 0
me = 0

for p in l:
    if p[1] >= 21:
        ma += 1
        print(f'{p[0]} é maior de idade')
    else:
        me += 1
        print(f'{p[0]} é menor de idade')
print(f'Temos o total de {ma} pessoas maiores de idade e {me} menores de idade.')
