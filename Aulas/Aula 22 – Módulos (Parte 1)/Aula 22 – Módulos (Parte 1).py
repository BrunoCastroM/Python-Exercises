############################# Módulo #############################


# A modularização tem foco em dividir um programa grande. Assim, seria possível aumentar a facilidade de legibilidade e a manutenção dele.

import defs_modulo  # Para chamar um módulo que eu fiz ou baixei é só colocar o "import "nome do arquivo". Nesse caso o meu arquivo se chamava defs_modulo, e vai começa a funcionar como um módulo.

num = int(input('Digite um valor: '))
fat = defs_modulo.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {defs.dobro(num)}')
print(f'O triplo de {num} é {defs.triplo(num)}')


from defs_modulo import fatorial, dobro, triplo  # Posso fazer assim também. Nesse caso eu não preciso mais chamar "defs.fatorial()", "defs.dobro(num)" e o "defs.triplo(num)", só preciso escrever
                                                 # o nome da função que eu quero.
num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro(num)}')
print(f'O triplo de {num} é {triplo(num)}')
