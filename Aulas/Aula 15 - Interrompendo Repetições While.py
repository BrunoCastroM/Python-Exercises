n = s = c = 0
while True:
    n = float(input('Digite um número: '))
    if n == 999:
        break # Eu uso o break para se eu digitar o número 999 (neste caso) para ele interromper o laço de repetição,
              # e ao mesmo tempo ele não irá contar o 999 e nem somar o 999.
    c = c + 1
    s = s + n
print(f'Foram {c} números e a soma vale {s:.2f}') # Em vez do .format() eu posso colocar so o f antes das "" da string, e colocar a variáveis dentro das chaves.