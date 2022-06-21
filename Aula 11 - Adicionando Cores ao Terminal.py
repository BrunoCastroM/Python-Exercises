# Código: \033[...;...;...m
# Estilo:                          Texto:            Back(Cores de Fundo): São as mesmas cores do texto
# 0 = Sem estilo nenhum            30 = Preto        40
# 1 = Texto em negrito             31 = Vermelho     41
# 4 = Vai sublinhar o texto        32 = Verde        42
# 7 = Vai inverter as cores        33 = Amarelo      43
#                                  34 = Azul         44
#                                  35 = Magenta      45
#                                  36 = Ciano        46
#                                  37 = Cinza        47
print('\033[31mBruno')
print('\033[1;32mBruno')
print('\033[4;33;44mBruno')
print('\033[4;35;46mBruno\033[m')
print('\033[7;35;46mBruno\033[m')

# Exercício:

a=24
b=29
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m!!!'.format(a,b))

# Colocando a cor dentro do .format:

n=input('Qual seu nome? ')
print('Olá, {}{}{}, tudo bem com você?'.format('\033[34m',n,'\033[m'))