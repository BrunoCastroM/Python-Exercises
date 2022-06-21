import datetime
d=datetime.date.today().year
soma=0
mih=0
nv=''
qm=0
for c in range(1,5):
    nome=str(input('Nome: '))
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip().lower()
    soma=soma+idade
    if c==1 and sexo=='m':
        mih=idade
        nv=nome
    if sexo=='m' and idade>mih:
        mih=idade
        nv=nome
    if sexo=='f' and idade<20:
        qm=qm+1
media=soma/4
print('A média de idade do  grupo é de {:.2f} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(mih,nv))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qm))