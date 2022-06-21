# Questão: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicioário se por acaso a CTPS for diferente de zero, o dicinário receberá também
# o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime # Essa é outra forma de colocar o ano atual, a outra forma poderia ser a mesma usada no desafio 54.
dados = {}
dados['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.now().year - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (Digite 0 para não tenho): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')