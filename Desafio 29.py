# Questão: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
v=float(input('Qual a velocidade que o carro estava andando? '))
if v<=80:
    print('Parabéns, você estava andando a {}Km/h, e por isso não levará multa!'.format(v))
else:
    m=(v-80)*7
    print('Infelizmente você foi MULTADO, pois passou do limite permitido que é de 80km/h\nVocê deverá pagar uma multa de R${:.2f}!'.format(m))
print('Tenha um bom dia e vá para a caixa prega!')