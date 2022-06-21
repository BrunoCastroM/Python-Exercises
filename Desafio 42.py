# Questão: Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado: 1) Equilátero: todos os lados iguais; 2) Isóceles:
# dois lados iguais; Escaleno: todos os lados diferentes.
t1=float(input('Digite o valor do primeiro segmento: '))
t2=float(input('Digite o valor do segundo segmento: '))
t3=float(input('Digite o valor do terceiro segmento: '))
if t1+t2>t3 and t2+t3>t1 and t1+t3>t2:
    print('Os segmentos acima PODEM formar um triângulo ',end='') # Esse ,end='' serve para colocar a continuidade da frase de baixo.
    if t1==t2==t3:
        print('EQUILÁTERO!')
    elif t1!=t2 and t2!=t3 and t3!=t1: # Posso fazer assim também if r1!=r2!=r3!=r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo')