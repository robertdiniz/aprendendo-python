# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e
# escrevendo na tela o nome do escolhido.

from random import choice

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista)

print(f'O nome escolhido foi: {escolhido}')
