# Questão: Crie um programa que leia vários n[umeros inteiros pelo teclado. O programa só
# vai para quando o usuário digitar o valor 999, que é a condição de parada. No final mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = c = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'Foram digitados {c} números e a soma entre ele foi {s}.')