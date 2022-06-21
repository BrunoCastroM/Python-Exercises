# Questão: Faça um programa que calcule a soma entre todos os números ímpares que são
# multiplos de 3 e que se encontram no intervalo de 1 até 500.
s=0 # Isso é um acumulador, ele irá somar.
c=0 # Isso é um contador.
for n in range(1,501,2):
    if n%3==0:
        s=s+n # Posso simplificar assim : s+=n
        c=c+1 # Posso simplificar assim : c+=1
print('A soma de todos os {} números solicitados é: {}'.format (c,s))