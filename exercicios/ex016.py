# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

from math import trunc
valor = float(input('Digite um número real para arredondar: '))
print(f'O valor digitado foi {valor}, sua porção inteira é: {trunc(valor)}')


'''Outra forma de responder é:
colocando o valor como int.'''