lanche = ('Pizza', 'Pudim', 'Suco', 'Hámburguer') # A tuplas são representadas pelos parenteses "()"

print(lanche)

# Uma tupla é imutável, ou seja, se você fez ela só irá poder mudar ela se trocar o valor dentro dela, se for tentar colocar uma variável para trocar qualquer elemento dentro dela não irá funcionar. Ex:
# lanche = ('Pizza', 'Pudim', 'Suco', 'Hámburguer')
# lanche[1] = 'Refrigerante'
# print(lanche[1]) # isso não irá funcionar pois tuplas são imutáveis.

print(lanche[1]) # Na hora de fazer a referência a tupla ou qualquer outra coisa, você deve colocar sempre colchetes "[]"

print(lanche[0:3]) # Nesse caso o terceiro elemento que seria o hámburguer não irá aparecer, pois ele exclúi o último elemento

print(lanche[-2:]) # Se colocar o "-" ele começa a contar de trás, so que não começa com o 0, e sim pelo -1 já.

print(len(lanche)) # Aqui ele irá falar quantos itens tem na tupla

for comida in lanche: # Utilizando o for eu vou colocar 1 print para cada item que eu coloquei dentro da tupla.
    print(f'Eu vou comer {comida}')

for comida in range(0, len(lanche)): # Esse aqui dará o mesmo resultado do de cima, só que esse foi utilizando o range.
    print(lanche[comida]) # Nesse caso ele irá enumerar as tuplas, porém vai colocar os nomes de cada item.

for comida in range(0, len(lanche)): # Aqui vai contar apartir do 0 o tanto de itens que tem a tupla
    print(comida)

for comida in range(0, len(lanche)):
    print(f'Vou comer {lanche[comida]} na posição {comida}')

for posição, comida in enumerate(lanche):  # Esse daqui de baixo funciona do mesmo jeito do de cima, só que usando a função "enumerate" e colocando mais 1 endereçamento que seria o "pos"
    print(f'Vou comer {comida} na posição {posição}')

print(sorted(lanche)) # O comando "sorted" ordena os itens da tupla, serve tanto para letras, quanto para números.

##############################  Trabalhando Tuplas com Números  #############################################

n1 = (3, 1, 2, 4)
n2 = (5, 6, 7, 5, 9, 10)
n3 = n1 + n2 # Nas tuplas se você somá-las ele irá juntar as duas tuplas.

print(n3)

print(sorted(n3)) # Vai ordenar os números

print(len(n3)) # Vai contar quantos elementos tem nas tuplas.

print(n3.count(5)) # Vai contar quantos "5" tem nas tuplas.

print(n3.index(6)) # Aqui vai printar a posição que o número 6 está. OBS: Começa a cotar do 0.

print(n3.index(5, 5)) # Aqui ele irá mostrar a posição em que o 5 está depois de 5 números cotados, nesse caso ele irá o registrar o 5 que está na 7 posição.


pessoa = ('Bruno', 29, 'M', 77.5) # Nas tuplas você pode colocar dados de qualquer tipo e misturar, como números e letras dentro de uma mesma tupla.
# Você pode apagar qualquer coisa com o comando del, nesse caso se eu escrevesse  del(pessoa), o print de baixo iria dar erro.
print(pessoa)