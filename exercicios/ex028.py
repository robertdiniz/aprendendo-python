# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep

n = int(input('Vou pensar em um número de 0 a 5. Tenta adivinhar...\n')) # jogador escolhe o número
numeroAleatorio = randint(0, 5) # gera um número aleatório entre 0 e 5 usando randint
print(f'Processando...')
sleep(3) # sleep pode suspender a operação por algum tempo
if n == numeroAleatorio:
    print(f'Você venceu, o número escolhido foi: {n}')
else:
    print(f'Você perdeu, o número escolhido foi: {numeroAleatorio}')
