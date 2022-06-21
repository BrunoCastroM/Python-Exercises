def metade(v=0):
    return v / 2


def dobro(v=0):
    return v * 2


def aumentar(v=0):
    return v * 1.10


def diminuir(v= 0):
    return v * 0.9


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')