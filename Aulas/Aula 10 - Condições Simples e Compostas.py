c=int(input('Quantos anos tem seu carro? '))
if c<=3:
    print('Seu carro é novo!')
    print('Parabéns!')
else:
    print('Então seu carro é uma lata velha!')
    print('Nós temos vários planos de consórcio para você ser enganado, que tal escolher um deles?')

'''Essa condição também pode ser feito assim (de maneira simplificada):²
c=int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo!'if c<=3 else'Seu carro é velho!')