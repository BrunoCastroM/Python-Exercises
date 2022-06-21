# Questão: Crie um programa que leia duas notas de um aluno e calcule sua média, mos-
# trando uma mensagem no final, de acordo com a média atingida:
# 1) Média abaixo de 5.0: Reprovado; 2) Média entre 5.0 e 6.9: Recuperação;
# 3) Média 7.0 ou superior: Aprovado.
n1=float(input('Digite sua primeira nota: '))
n2=float(input('Digite sua segunda nota: '))
m=(n1+n2)/2
print('tirando {:.1f} e {:.1F}, a média do aluno é : {:.1f}'.format(n1,n2,m))
if m<5:
    print('O aluno foi reprovado.')
elif 5<=m<=6.9: #Obs: A forma que está a esquerda é a versão simplificada dessa: elif m>=5 and m<=6.9:
    print('O aluno ficou de recuperação.')
elif m>=7.0:
    print('O aluno foi aprovado.')