########################## Interactive Help ##########################

help()  # Use o "help()" no console do python para digitar a função que você está em dúvida e verificar o que ela faz.

help(print)  # Não precisa ser pelo console se quiser rodar o programa é so colocar a função que esteja em dúvida dentro dos "()"

exit()  # Vai sair da ajuda interativa.

print(input.__doc__) # Essa função "__doc__" faz a mesma coisa do "help()", só que ela pode dar uma inforção que não tinha no "help()"


def contador(i, f, p): # As """ triplas servem para fazer o "docstring", então quando você chamar o comando help ele vai dizer o que você escreveu dentro das aspas.
    """ Faz uma contagem e mostra na tela.
    Para i: Início da contagem
    Para f: Fim da contagem
    Para p: Passos da contagem
    return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p

help(contador)


########################## Parâmetros Opcionais ##########################

def somar(a, b, c = 0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4) # Nessa situação como eu so coloquei o valor das variáveis "a" e "b" ele vai dar um erro, pois falta o valor da variável "c,
            # porém eu posso resolver isso usando os parametros opcionais colocando na variável "c" lá de cima "= 0", isso quer dizer que se
            # eu não colocar nenhum parâmetro para a variável "c" ela vai contar como se fosse = 0.


########################## Escopo de Variáveis ##########################

def teste(b):
    global a # 5. Isso aqui serve para eu dizer que eu quero transformar variável global "a" = 2 na variável local "a" = 8, então até o 2 vai se tornar 8.
    a = 8  # 4. Aqui eu criei uma variável local, que neste caso irá existir uma variável "a" global = 2 e uma variável local "a" = 8
    b += 8 # 1. isso aqui é uma "variável local", ou seja, ela so vai funcionar dentro da indentação que ela está.
    print(f'Na função teste, A vale {a}')
    print(f'Na função teste, B vale {b}')


a = 2 # 2. isso aqui e uma "variável global"
print(f'No programa principal A vale {a}')
teste(a) # 3. Como "a" é uma variável global ela vai funcionar para todas as funções. Então na função def ali em cima ele vai pegar o valor da variável "a" colocar na "b"
         # e depois irá somar o valor "2 + 8". Porém se eu fizer o chamamento da variável "a" dentro da função "def teste(b)" ela vai me retornar o valor dela mesmo, que seria "2".
         # Se eu for tentar chamar a variável "b" para o escopo global que seria a função principal, iria dar erro, pois ela somente está valendo para dentro da função "def teste(b)".


########################## Retorno de Valores ##########################


def somar (a=0, b=0, c=0):
    s = a + b + c
    return s   # A função "return" serve para retornar o valor que está dentro do programa local e jogar para o programa global. E toda vez que você chamar a função "def" nesse caso
               # o "somar()" ele irá mostrar o valor que está no return (nesse caso seria o valor de "s").


resposta = somar(2, 3, 5)
print(f'A resposta é {resposta}')

print(somar(3, 2, 5)) # posso também fazer dessa forma escrevendo logo o print sem criar uma variável (nesse caso sem criar a "resposta")

r1 = somar(5, 1, 3)
r2 = somar(5, 1)
r3 = somar(5)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')


def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'A fatorial de {n} é = {fatorial(n)}')


f1 = fatorial(6)
f2 = fatorial(2)
f3 = fatorial(3)
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(numero):
    if numero % 2 == 0:
        return 'Esse número é par'  # Posso também colocar "True" ou "False" dentro do "return". Nesse caso eu coloquei uma frase.
    else:
        return 'Esse número não é par'

num = int(input('Digite um número: '))
print(par(num))