# Questão: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal; e 3 para hexadecimal.

n = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
e = int(input('Qual é sua escolha?: '))

if e == 1:
    print('{} convertido para Binário é = {:b}'.format(n, n))
    # Obs: O print poderia ser assim: print('{} convertido para Binário é = {}'.format(n,bin(n))), o {:b} serve para converter
    # em Binário sem precisar colocar dentro do .format().
elif e == 2:
    print('{} convertido para Octal é = {:o}'.format(n, n))
    # Obs: O print poderia ser assim: print('{} convertido para Binário é = {}'.format(n,oct(n))), o {:o} serve para converter
    # em Octonal sem precisar colocar dentro do .format().
elif e == 3:
    print('{} convertido para Hexadecimal é = {:X}'.format(n, n))
    # Obs: O print poderia ser assim: print('{} convertido para Binário é = {}'.format(n,oct(n))), o {:x} (letras minúsculas ou
    # {:X} (letras maiúsculas serve para converter em Octonal sem precisar colocar dentro do .format().
else:
    print('Opção inválida. Tente novamente!')
