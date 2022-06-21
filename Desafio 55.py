#Questão: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.
ma=0
me=0
for d in range(1,6):
    p=float(input('Digite o peso da {}ª pessoa: '.format(d)))
    if d==1:
        ma=p
        me=p
    else:
        if p>ma:
            ma=p
        if p<me:
            me=p
print('O maior peso foi {}Kg'.format(ma))
print('O menor peso foi {}Kg'.format(me))