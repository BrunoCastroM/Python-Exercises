# Questão: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da
# função criada: 1) de 1 até 10, de 1 em 1; 2) de 10 até 0, de 2 em 2; 3) uma contagem personalizada.
def contador(inicio, fim, passo):
    from time import sleep
    for i in range(inicio, fim, passo):
        print(i, end=' ')
        sleep(0.5)
    print('Fim!')


contador(0, 11, 1)
contador(10, 0, -2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(i, f, p)

'''Esse exercício também pode ser feito assim:²  (Resolução do professor)
from time import sleep
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 1:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        sleep(0.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:' ))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''