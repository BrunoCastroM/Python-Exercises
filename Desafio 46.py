# Questão: Faça um programa que mostre na tela uma contagem regessiva para o estouro
# de fogos de atifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time
for c in range(10,-1,-1): # O -1 na segunda parte serve para ele colocar o 0 na contagem.
    time.sleep(0.5)
    print(c)
print('KABUM!!!')