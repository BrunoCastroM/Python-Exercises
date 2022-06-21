# [LP-A02]  Andriel criou um programa que recebe a senha que o usuário deseja cadastrar, mas só valida caso ela tenha a partir de 8 caracteres. Selecione a linha de código que completa corretamente o código.
#
# senha = input('Escolha a sua senha: ') (??????????????????)     print('A senha deve conter mais que 8 caracteres')
# else:
#     print('Senha cadastrada com sucesso')
#
# Tipo da Pergunta: Alternativa
# Sua resposta
# B) if len(senha) < 8:
# Outras opções
# A) if senha.len() <= 8:
# C) if senha.len() < 8:
# D) if len(senha) > 8:


# num = int(input('Informe um número para verificação: '))
#
#
# primo = 'sim'
# for i in range(2,num):
#     if num % i == 0:
#         primo = 'não'
#
# if primo == 'sim':
#     print('O número é primo')
# else:
#    print('O número não é primo')
#
# B


# inf = int(input('Informe o intervalo inferior: '))
# sup = int(input('Informe o intervalo superior: '))
#
# if sup < inf:
#     c = sup
#     sup = inf
#     inf = c
#     print(f'Você digitou o intervalo superior menor que o inferior, então os dois {inf} e {sup} foram invertidos')
#
# print('\nOs números pares entre os intervalos dados são: ')
#
# for i in range(inf, sup):
#     if i % 2 == 0:
#         print(f'{i}',end=",")

lista = [5,10,15,25]
print(lista[::-2])