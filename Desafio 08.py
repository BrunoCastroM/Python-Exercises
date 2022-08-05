# Questão": Escreva um programa que leia um valor em metros todos os valores de sua conversão.

m = float(input('Digite sua medida em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'Sua medida em quilômetros é: {km}km\nSua medida em hectômetros é: {hm}hm\nSua medida em decâmetros é: {dam:.0f}dam\nSua medida em decímetros é: {dm:.0f}dm\nSua medida em centímetros é: {cm:.0f}cm\nSua medida em milímetros é: {mm:.0f}mm')
