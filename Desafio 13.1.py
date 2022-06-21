# Questão: Crie um programa que calcule o valor do produto com 10% de desconto à vista, e se
#for à prazo com 15% de juros.
p=float(input('Qual o valor do produto?: R$'))
d=p-(p*0.1)
j=p*1.15
print('Seu produto à vista sairá por: R${:.2f}\nSe for à prazo sairá por: R${:.2f}'.format(d,j))