# Questão: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(l, c):
    total = largura * comprimento
    print(f'A área de um terreno {l} x {c} é de {total}m²')


largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimenro do terreno: '))
area(largura, comprimento)
