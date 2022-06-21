# Questão: Faça um programa que leia algo pelo teclado e mostrena tela o seu tipo primitivo e todas as informa-
# ções possíveis sobre ele.
a=input('Digite algo:')
print('O tipo primitivo desse valor é:',type(a))
print('Tem letras e números?:', a.isalnum())
print('Só tem letras?:', a.isalpha())
print('Só tem números?:', a.isnumeric())
print('Foi digitado somente em caixa alta?:', a.isupper())
print('Foi digitado somente em letras minúsculas? {}'.format(a.islower()))
print('Foi digitado com letras maiúsculas e minúsculas? {}'.format(a.istitle()))


