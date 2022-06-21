# Questão: Faça um programa que leia a largura e a altura de uma parede em metros, calcula a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
a=float(input('Digite a altura em metros da parede:'))
l=float(input('Digite a largura em metros da parede:'))
m=a*l
t=m/2
print('Você tem uma parede de {}m², e precisará de {} litro(s) de tinta.'.format(m,t))