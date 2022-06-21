# Questão: Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
t = n
c = 1
t1 = 0
m = 10
while m != 0:
    t1 = t1 + m
    while c <= t1:
        print('{} → '.format(t), end='')
        t = t + r
        c = c + 1
    print('Pausa')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('Processo encerrado!')