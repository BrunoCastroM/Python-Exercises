# Questão: Escreva um programa que pergunte o salário de um funcionário e calcula o valor do seu aumento. Para
# salários superiores a R$1.250.00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s=float(input('Qual é o salário do funcionário?: '))
a1=s*1.1
a2=s*1.15
if s>1250:
    print('Seu Salário depois do aumento ficará: R${:.2f}'.format(a1))
else:
    print('Seu slário depois do aumento será de: R${:.2f}'.format(a2))
