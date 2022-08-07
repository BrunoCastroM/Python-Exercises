# Questão: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

t1 = float(input('Digite o valor do primeiro segmento: '))
t2 = float(input('Digite o valor do segundo segmento: '))
t3 = float(input('Digite o valor do terceiro segmento: '))
if t1 + t2 > t3 and t2 + t3 > t1 and t1 + t3 > t2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
