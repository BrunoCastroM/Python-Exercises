def metade(v=0, formato=False):
    resultado = v / 2
    return resultado if formato is False else moeda(resultado)


def dobro(v=0, formato=False):
    resultado = v * 2
    return resultado if not formato else moeda(resultado)  # Essa sintax é a mesma coisa das outras só que escrita de maneira diferente.


def aumentar(v=0, taxa=0, formato=False):
    resultado = v + (v * taxa/100)
    return resultado if formato is False else moeda(resultado)


def diminuir(v=0, taxa=0, formato=False):
    resultado = v - (v * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')