# Questão: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os
# dados em forma tabular.
print('-' * 40)
print(f'{"LISTAGEM DE PRODUTOS":^40}')
print('-' * 40)
l = ('Lápis', 1.75,
         'Borracha', 2.00,
         'Caderno', 15.90,
         'Estojo', 25.00,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Livro', 34.90)
for c in range(0, len(l)):
    if c % 2 == 0:
        print(f'{l[c]:.<30}',end='')
    else:
        print(f'R${l[c]:>7.2f}')


'''Esse exercício também pode ser feito assim:² (Minha resolução)
print('LISTAGEM DE PRODUTOS')
print(('Lápis.................R$ 1.75'),
      ('\nBorracha..............R$ 2.00'),
      ('\nCaderno...............R$ 15.90'),
      ('\nEstojo................R$ 25.00'),
      ('\nTransferidor..........R$ 4.20'),
      ('\nCompasso..............R$ 9.99'),
      ('\nMochila...............R$ 120.32'),
      ('\nCanetas...............R$ 22.30'),
      ('\nLivro.................R$ 34.90'))'''

