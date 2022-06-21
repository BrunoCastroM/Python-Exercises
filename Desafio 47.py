# Questão: Crie um programa que mostre na tela todos os números pares que estão no intervalo
# entra 1 e 50.
for n in range(1,51):
    if n%2==0:
        print(n, end=' ') # Esse "end=' '" só serve para juntar a linha que seria em baixo para ficar do lado da de cima.
print('É só isso')

'''Esse exercício também pode ser feito assim:²
for n in range(2,51,2):
    print(n, end=' ')
print('É só isso')'''