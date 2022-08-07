# Questão: Crie um program que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

n = str(input('Digite seu completo: ')).strip()
input('Seu nome tem silva? {}'.format('SILVA' in n.upper()))
