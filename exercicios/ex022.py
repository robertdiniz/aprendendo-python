#  Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome com letras maiúsculas: {nome.upper()}.')
print(f'Seu nome com letras minúsculas: {nome.lower()}.')
print(f'Seu nome ao todo tem {len(nome) - nome.count(" ")}.')
print(f'Seu primeiro nome é: {nome.split()[0]}, e tem {len(nome.split()[0])} letras.')
