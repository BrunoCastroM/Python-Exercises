'''for c in range(1,4):
    print(c)'''

# Para fazer a mesma coisa de cima na função while eu teria que colocar um contador
# e fazer isso:
# Obs: O while pode ser usado tanto para quando você sabe o limite, tanto para quando
# você não sabe o limite.

c = 1
while c < 4:
    print(c)
    c = c + 1

n = 1
while n != 0: #aqui ele vai ficar perguntando a frase do input até você digitar "0".
    n = int(input('Digite um valor: '))


r = 'S'
while r == 'S': # Aqui ele só vai parar de perguntar quando eu digitar algo que não seja "S".
   n = int(input('Digite um valor: '))
   r =str(input('Você quer continuar: S/N ')).upper()
print('fim')


n=1
par = impar = 0
while n != 0:
   n = int(input('Digite um número: '))
   if n != 0:
      if n % 2 == 0:
         par = par + 1
      else:
         impar = impar + 1
print(' Você digitou {} números pares e {} números ímpares.'.format(par,impar))