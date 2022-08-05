############################# Pacotes (Bibliotecas) #############################


# Pacote é uma pasta que contém módulos

# Neste caso eu criei um pacote com nome "pacote_utilidades" e criei outro pacote para números dentro dele (eu poderia fazer outras def para outras coisas,
# por exemplo, para manipular strings e criaria outro pacote dentro de "pacote_utilidades" para manipulá-las.

from pacote_utilidades import numeros  # Para chamar o pacote eu pedi que dentro do "pacote_utilidades" importesse o pacote "numeros".

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')