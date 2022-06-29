# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite o ano que queira saber se é bissexto. Coloque 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 400 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é um ano bissexto.')
else:
    print(f'O ano {ano} não é um ano bissexto.')
