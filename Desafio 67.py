# Questão: Faça um programa que mostre a tabuada de vários números, um de cada vez, para
# cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for
# negativo.
n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= -1:
        print('Programa de tabuada encerrado!')
        break
    for m in range(1, 11):
        print(f'{n} x {m:2} = {n * m}')