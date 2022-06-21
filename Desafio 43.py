# Questão: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcula seu
# IMC e mostre seu status, de acordo com a tabela abaixo: 1) Abaixo de 18.5: Abaixo do peso
# 2) Entre 18.5 e 25: Peso ideal; 3) 25 até 30: Sobrepeso; 4) 30 até 40: Obesidade
# 5) Acima de 40: Obesidade mórbida.
p=float(input('Qual é o seu peso? '))
a=float(input('Qual sua altura? '))
imc= p/(a**2)
print('O seu IMC é {:.1f}'.format(imc))
if imc<18.5:
    print('Você está Abaixo do Peso')
elif imc<25:
    print('Você está com o Peso ideal')
elif imc<30:
    print('Você está com Sobrepeso')
elif imc<40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade Mórbida')