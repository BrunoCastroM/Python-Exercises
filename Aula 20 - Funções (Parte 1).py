def linha():
    print('_' * 30)
# Do "def" para o programa principal (é o qe está a baixo) é bom colocar duas linhas, pois fica estéticamente mais bonito e o python não reclama.

linha()
print('Hi!')
linha()

def titulo(texto):
    print('_' * 30)
    print(texto)
    print('_' * 30)

# Tudo que está em baixo do "def" é chamado de programa principal
titulo('Curso em Vídeo') # em vez de "print" eu coloco o nome que eu defini, e escrevo a frase. ai ele vai fazer o ciclo que eu coloquei dentro do "def"
titulo('Python é muito bom')

def soma(a, b):
    s = a + b
    print(s)


soma(5, 9)
soma(20, 50)
soma(a=4, b=10) # Se você for explicitar valores, você tem que explicitar todos os valores, se não dará erro.
soma(b=12, a=3)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


soma(5, 8) # Se eu quiser colocar mais de 2 números eu tenho que alterar a "def" e colocar outra variável para completar o 3° número, se não dará erro.

############################# Empacotamento #############################

def contador(* numero): # O "*" (símbulo de desempacotar) serve para pegar vários parâmetros e colocar dentro de "numero" nesse caso. Ai ele irá criar uma tupla com os valores
    print(numero)


contador(1, 5, 8)
contador(8, 0)
contador(5, 2, 6)


def contador(* numero):
    for valor in numero:
        print(f'{valor} ', end='')
    print('Fim!')

contador(1, 5, 8)
contador(8, 0)
contador(5, 2, 6)

def soma(* valores):
    s = 0
    for numero in valores:
        s += numero
        print(f'Somando os valores {valores} temos {s} ')


soma(5, 6)
soma(7, 9, 10)

def contador(* numero):
    tamanho = len(numero)
    print(len(numero))
    print(f'Recebi os valores {numero} e são ao todo {tamanho} números')


contador(1, 5, 8)
contador(8, 0)
contador(5, 2, 6)

def dobra_valor(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 7, 8, 3, 0, 1]
dobra_valor(valores)
print(valores)
