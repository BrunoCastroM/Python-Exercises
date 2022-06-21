def pergunta(frase):
    tamanho = len(frase) + 4
    print('~' * tamanho)
    print(f'  {frase}')
    print('~' * tamanho)


pergunta(str(input('Digite uma uma palavra: ')))