# Questão: Escrava um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0.15
# por km rodado.
km=float(input('Quantos quilometros o carro percorreu?: '))
d=int(input('Por quantos dias o carro foi alugado?: '))
t=d*60+km*0.15
print('O valor do aluguel do carro é de: R$ {:.2f}'.format(t))