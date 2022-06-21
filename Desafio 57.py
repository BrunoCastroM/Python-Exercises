# Questão: Faça um programa que leiao sexo de uma pessoa, mas só aceite os valores "M" ou "F.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().lower()[0]
while sexo not in 'mf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: '))
if sexo == 'm':
    print ('Sexo Masculino registrado com sucesso.')
if sexo == 'f':
    print('Sexo Feminino registrado com sucesso.')