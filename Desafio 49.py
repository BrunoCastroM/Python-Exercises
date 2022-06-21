# Questão: Refaça o Desafio 09, mostrando a tabuada de um número que o usuário escolher,
# só que gora utilizando um laço for.
n=int(input('Digite um número: '))
for m in range(1,11):
    t=n*m
    print('{} x {:2} = {}'.format(n,m,t)) #Posso simplificar e tirar a fórmula de cima (t=n*m) e colocar "n*m" em vez do "t" que está dentro do .format