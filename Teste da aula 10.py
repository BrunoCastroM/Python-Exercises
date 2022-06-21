n1=float(input('Qual foi a sua primeira nota: '))
n2=float(input('Qual foi sua segunda nota: '))
m=(n1+n2)/2
print('Sua média é: {:.2f}'.format(m))
if m>=6:
    print('Você está bem!')
else:
    print('Você está passando mal!')