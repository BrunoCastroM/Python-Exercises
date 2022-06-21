# Questão: Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
d=datetime.date.today().year
c=0
c1=0
for p in range(1,8):
    a=int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    i=d-a
    if i<=18:
        c=c+1
    else:
        c1=c1+1
print('Ao todo tivemo(s) {} pessoa(s) menore(s) de idade.'.format(c))
print('E {} pesso(s) maior(es) de idade'.format(c1))