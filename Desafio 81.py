# Questão: Crie um progama que vai ler vários números  e coloca em uma lista. Depois disso, mostre: 1) Quantos números foram digitados; 2) A lista de valores, ordenada de forma
# decrescente; 3) Se o valor 5 foi digitado e está ou não na lista.
l = []
while True:
    l.append((int(input('Digite um valor: '))))
    p = ' '
    while p not in 'sn':
        p = (str(input('Deseja continuar: [S/N] '))).strip().lower()[0]
    if p == 'n':
        break
print(f'Você digitou {len(l)} elementos')
l.sort(reverse=True)
print(f'Os valores em ordem decressente são: {l}')
if 5 in l:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não foi encontrado na lista')
