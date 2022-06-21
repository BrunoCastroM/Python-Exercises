# Questão: Elabore um programa que calcule o valor a ser pago por um produto considerando
# o seu preço normal e condiçao de pagamento: 1) À vista dinheiro/cheque: 10% de desconto
# 2) À vista no cartão: 5% de desconto; 3) Em até 2x no catão: Preço normal; 4) 3x ou
# mais no cartão: 20% de juros.
c=float(input('Qual foi o valor da compra? '))
print('''Escolha uma das opções:
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no catão: Preço normal
[4] 3x ou mais no cartão: 20% de juros''')
o=int(input('Qual das opções de pagamento o senhor vai querer?'))
o1=c*0.9
o2=c*0.95
o3=c/2
if o==1:
    print('Nessa opção o valor de R${:.2f} com 10% de desconto ficará R${:.2f}.'.format(c,o1))
elif o==2:
    print('Nesa opção o valor de R${:.2f} com 5% de desconto ficará R${:.2f}.'.format(c,o2))
elif o==3:
    print('Nessa opção sua compra será parcelada em {}x de R${:.2f}, sem juros.'.format(p,o3))
elif o==4:
    par=(int(input('Quantas parcelas? ')))
    o4=(c*1.2)/par
    r=c*1.2
    print('Dividido em {}x a sua parcela ficará R${:.2f}.'.format(par,o4))
    print('Sua compra de R${:.2f} passará para o valor de R${:.2f}.'.format(c,r))
else:
    print('\033[31mOpção Inválida')