# Questão: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# Cadastrada, o programa deverá perhuntar se o usuário quer ou não continuar. No final
# mostre: 1) Quantas pessoas tem amis de 18 anos; 2) Quantos homens foram cadastrados;
# 3) Quantas mulheres tem menos de 20 anos.
m18 = h = m20 =  0
print('Cadastre uma pessoa')
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'mf':
        s = str(input('Sexo [M/F]: ')).strip().lower()[0]
    q = ' '
    while q not in 'sn':
        q = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if i >= 18:
        m18 = m18 + 1
    if s == 'm':
        h = h + 1
    if i < 20 and s == 'f':
        m20 = m20 + 1
    if q == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todos temos {h} homens cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')


'''Esse exercício também pode ser feito assim:² (Minha resolução)

m18 = h = m20 = 0
print('Cadastre uma pessoa')
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().lower()[0]
    q = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if i >= 18:
        m18 = m18 + 1
    if s == 'm':
        h = h + 1
    if i < 20 and s == 'f':
        m20 = m20 + 1
    if q == 'n':
        break
print(f'Total de pessoas com mais de 18 anos: {m18}')
print(f'Ao todos temos {h} homens cadastrados')
print(f'E temos {m20} mulheres com menos de 20 anos')'''