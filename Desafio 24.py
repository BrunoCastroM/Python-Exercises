# Questão: Crie um programa que leia o nome de uma cidade e diga se ela começa com o nome "Santo".

c = str(input('Digite o nome da cidade que você nasce: ')).strip()
f = c.lower()
print('santo' in f)

'''Esse exercício também pode ser feito assim:²
c=str(input('Digite o nome da cidad eque você nasceu: ')).strip()
print(c[:5].upper()=='SANTO')'''
