# Questão: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo
# teclado (entre 0 e 20) e mostrá-lo por exteso.
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n1 <= 20:
        break
    print('Número inválido!')
print(f'Você digitou o número {n[n1]}')

'''Esse exercício também pode ser feito assim:²
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
v = int(input('Digite um número: '))
while True:
    if v > 20:
        v = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if v < 0:
        v = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Você digitou o número {n[v]}.')'''

###################################### DESAFIO ##########################################

'''n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Número inválido!')
    r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
print('Programa encerrado!')'''