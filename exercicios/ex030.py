# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número inteiro: '))
result = n % 2
if result == 0:
    print(f'PAR')
else:
    print(f'ÍMPAR')
