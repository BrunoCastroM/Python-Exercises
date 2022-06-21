# Questão: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo
# inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('Erro: Por favor, digite um número inteiro válido!')
            continue
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError, KeyboardInterrupt):
            print('Erro: Por favor, digite um número float válido!')
            continue
        else:
            return n


numero1 = leia_int('Digite um valor: ')
numero2 = leia_float('Digite um número flutuante: ')
print(f'O valor digitado foi: {numero1}, e o real foi {numero2}')