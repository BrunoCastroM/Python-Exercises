import math
# ou pode fazer a importação específica com : 'from math import sqrt, floor, ceil', por exemplo.
n=int(input('Digite um número: '))
r=math.sqrt(n)
print('A raiz de {} é = {:.2f}'.format(n,math.ceil(r)))#posso escrever também math.floor para arre-
# dondar para baixo.