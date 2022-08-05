# Exemplo de como fazer um texto grande em um print:(só usar '''...''', no começo e no final da frase)
# print('''conjunto das palavras escritas, em livro, folheto, documento etc. (p.opos. a
# comentários, aditamentos, sumário etc.); redação original de qualquer obra escrita.
# um t. manuscrito''')

# Um String é imutável, porém se você fizer uma função de trasnformação de string e faça uma atribuição a ela. Ex:
# f='Meu nome é João'
# f= f.replace('João','Matias')
# print(f)

#Se você quiser que só saia uma palavra espcífica da frase, você pode fazer assim:ex:
# f='Olá, meu nome é Zezinho'
# d=f.split()
# print(d[2])

f=' Olá, meu nome é Bruno!  '
print(f)
print(f[2])
print(f[2:10])
print(f[2:10:3])
print(f[2:])
print(f[:20])
print(len(f)) # Pode combinar com o strip (para tirar os espaços do começo e do final).Ex: print(len(f.strip()))
print(f.count('o')) # Ele diferencia letra maiuscula de minuscula
print(f.find('e'))
print('m'in f)
print(f.replace('Bruno','Pomba Gira'))
print(f.upper()) # Dá para você juntar funções.Ex: print(f.upper().count('O')) ->Neste caso ele contará todos os 'O'
# maiusculos em uma frase que só tem letras maiusculas.
print(f.lower())
print(f.capitalize())
print(f.title())
print(f.strip())
print(f.split())
print('*'.join(f))