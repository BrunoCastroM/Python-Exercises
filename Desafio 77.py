# Questão: Crie um programa que tenhauma tupla com várias palavras (não usar acentos). Dpois disso, você deve mostrar para cada palavra, quais são as suas vogais.
t = ('livro', 'casa', 'mesa', 'banheira', 'mesa', 'porta', 'linguagem')
for l in t:
    print(f'\nNa palavra {l} temos: ',end='')
    for l1 in l:
        if l1.lower() in 'aeiou':
            print(l1, end='')