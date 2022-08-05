# Questão: Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

n = int(input('Digite um número:'))
t1 = n*1
t2 = n*2
t3 = n*3
t4 = n*4
t5 = n*5
t6 = n*6
t7 = n*7
t8 = n*8
t9 = n*9
t10 = n*10
print('A tabuada desse múmero é:\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}\n{} x {:2} = {:2}'.format(
    n, 1, t1, n, 2, t2, n, 3, t3, n, 4, t4, n, 5, t5, n, 6, t6, n, 7, t7, n, 8, t8, n, 9, t9, n, 10, t10))
