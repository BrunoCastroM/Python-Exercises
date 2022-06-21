import datetime
a=int(input('Digite um ano: '))
if a==0:
   a=datetime.date.today().year
if a%4==0 and a%100!=0 or a%400==0: # Posso usar "and ou "or" para acrescentar mais funções.
    print('O ano de {} é bissexto!'.format(a))
else:
    print('O ano de {} não é bissexto!'.format(a))