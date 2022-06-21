# Questão : Crie um pequeno sistema modularizado que permite cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from Desafio115.lib.interface import *
from Desafio115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivo_existe(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Aquivo não encontrado')
    criar_arquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        ler_arquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema...')
        break
    else:
        print('Erro: Digite uma opçao válida!')
