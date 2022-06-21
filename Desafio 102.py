# Questão: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que
# será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(numero=1, show=True):
    """
    Calcula o Fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (Opcional) Se inserir o valor "True" no show lá em baixo irá mostrar a conta, se inserir o valor "False" só irá mostrar o resultado.
    :return: O valor Fatorial de um número n
    """
    f = 1
    for c in range(numero, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f

n = int(input('Digite um número: '))
print(f'{fatorial(n, show=True)}')  # Se eu colocar "True" ele irá mostrar o cálculo feito para chegar no valor. Porém, se eu digitar "False" ele irá mostrar somente o resultado.
help(fatorial)