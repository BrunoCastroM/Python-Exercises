n=str(input('Qual é o seu nome?')).strip().lower()
if n=='bruno':
    print('Que nome lindo você tem!')
elif n=='pedro' or n=='gustavo' or n=='maria':
    print('Seu nome é bem costumeiro para os padrões brasileiros!')
elif n=='ana' or n=='juliana' or n=='joaquina':
    print('Que nome feminino Legal') #Obs: Você pode colocar a condição elif quantas vezes você achar que sejam necessárias.
else: # Obs²: Se você tirar o else dessa condição aninhanda, não terá problema algum
    print('Seu nome é bem normal')
print('Tenha um bom dia {}!'.format(n))