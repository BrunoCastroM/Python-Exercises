# QuestãoFaça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: 1) Quantidade de notas;
# 2) A maior nota; 3) A menor nota; 4) A média da turma; 5) A situação (opcional).
def notas(*n, sit=False):
    """
    Função para analisar notas e situações de vários alunos.

    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor adicional, indicando se deve ou não adcionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['Total'] = len(n)
    dados['Maior'] = max(n)
    dados['Menor'] = min(n)
    dados['Média'] = sum(n)/dados['Total']  # Eu posso colocar também escrever assim "sum(n)/len(n)"
    if sit:
        if dados['Média'] >= 7:
            dados['Sitação'] = 'Boa'
        elif dados['Média'] >= 5:
            dados['Sitação'] = 'Razoável'
        else:
            dados['Sitação'] = 'Ruim'
    return dados


resposta = notas(6, 5.9, 10, sit=True)
print(resposta)
# help(notas)  # Aqui vai servir para tirar a dúvida sobre o que a função def está fazendo.