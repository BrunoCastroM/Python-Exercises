# Questão: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
t=int(input('Digite o primeiro termo da PA: '))
r=int(input('Digite a razão da PA: '))
d=t+(10-1)*r
for n in range(t,d+r,r):
    print(' {} '.format(n),end='→')
print(' É isso!!')

'''Esse exercício também pode ser feito assim:²
t=int(input('Digite o primeiro termo da PA:'))
r=int(input('Digite a razão da PA: '))
for n in range (0,10):
    print('{}'.format(t+r*n),end=' → ')
print(' É isso!!')'''