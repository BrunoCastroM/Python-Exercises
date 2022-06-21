# Questão: A Confederação Nacional de Natação precisa de um programa que leia o ano de
# nascimento de um atleta e mostre sua categoria, de acordo com a idade: 1) Até 9 anos:
# Mirim; 2) Até 14 anos: Infantil; 3) Até 19 anos: Junior; Até 25 anos: Sênior: Acima:
# Master.
import datetime
d=datetime.date.today().year
a=int(input('Digite o ano de nascimento do atleta: '))
i=d-a
if i<=9:
    print('Classificação: Mirim')
elif i<=14:
    print('Classificação: Infantil')
elif i<=19:
    print('Classificação: Junior')
elif i<=25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')