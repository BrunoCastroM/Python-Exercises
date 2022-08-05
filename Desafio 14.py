# Questão: Escreva um programa que converta uma temperatura digitada em celsius e converta para fahrenheit.

t = float(input('Digite a temperatura em celcius:'))
c = ((t * 9) / 5) + 32
print('A temperatura convertida para fahrenheit é: {:.1f}'.format(c))
