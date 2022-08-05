for c in range(0,4):
    print('oi')

for a in range (1,4): # Aqui ele irá fazer uma contagem de 1 até 3 (ele ignora o último número)
    print(a)

for e in range (5,0,-1): # Aqui irá fará uma contagem regressiva
    print(e)

for x in range (0,7,2): # Aqui ele irá pular de 2 em 2 números
    print(x)

n=int(input('Digite um número: ')) # Nessa caso ele irá contar até o número que você digitou, porém ele excluirá o último número, para isso você coloca o +1,
for c in range(0, n+1):            # para ele contar até o número digitado mesmo.
    print (c)

i=int(input('Digite um número incial: '))
f=int(input('Digite até onde você quer que ele conte: '))
p=int(input('Digite de quantos em quantos números ele irá pular: '))
for c in range (i,f+1,p):
    print(c)

for c in range(0,5):
    n=int(input('Digite um valor: ')) # Aqui ele irá pedir para digitar uma valor 5 vezes

s=0
for c in range(0,4):
    n=int(input('Digite um valor: '))
    s=s+n # Aqui ele irá somar os 4 números digitados
print('O somatório de todos os valores inseridos será:{}'.format(s))