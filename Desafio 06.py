# Questão: Crie um algoritmo,o que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('Seu dobro é: {} \nSeu triplo é: {} \nSua raiz quadrada é: {}'.format(n1, n2, n3))
