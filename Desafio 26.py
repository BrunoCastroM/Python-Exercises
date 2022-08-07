# Questão: Faça um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "a"; 2) Em que posição ela aparece a primeira vez; 3)Em que posição ela aparece a última vez.

l = str(input('Escreva uma frase: ')).strip().lower()
print('''A letra "a", parece {} vezes
A primeira letra "a" apareceu na posição: {}
Aúltima letra "a" Apareceu na posição: {}'''.format(l.count('a'), l.find('a')+ 1, l.rfind('a')+1))

# Obs: Dá para pular a linha para baixo sem usar o operador "\n", que nem eu fiz acima somente colocando 3 aspas de cada lado
