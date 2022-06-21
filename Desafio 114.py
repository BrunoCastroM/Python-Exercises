# Questão: Crie um código em Python que teste se o site "pudim.com.br" está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except: # eu posso escrever depois do except "urllib.error.URLError", para especificar o erro.
    print('O site pudim não está acessível no momento')

else:
    print('Consegui acessar o site pudim com sucesso!')
    print(site.read()) # O comando "read()" vali ler todos os códigos do site que está acessando.