# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

num1 = float(input('Digite o primeiro valor númerico inteiro: '))
num2 = float(input('Digite o segundo valor númerico inteiro: '))
cor = '\033[4;36m'

if num1 > num2:
    print(f'{cor}{num1}\033[m é o maior valor, e {cor}{num2}\033[m é o menor valor.')
elif num2 > num1:
    print(f'{cor}{num2}\033[m é o maior valor, {cor}{num1}\033[m é o menor valor.')
else:
    print(f'{cor}{num1}\033[m e {cor}{num2}\033[m são iguais.')
