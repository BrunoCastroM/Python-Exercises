# Questão: Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final,
# mostre a lista ordenada na tela.
l = []
for c in range(0, 5):
    n = (int(input('Digite um número: ')))
    if c == 0 or n > l[-1]:
        l.append(n)
        print('Adcicionado ao final da lista')
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p,n)
                print(f'Adcionado na posição {p} da lista')
                break
            p += 1
print(f'Os valores digitados em ordem foram {l}')