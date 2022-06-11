# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
# aparece a letra "A", em que posição ela aparece a primeira vez e em que
# posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip()
print(f'A letra A apareceu {frase.lower().count("a")} vezes na frase.')
print(f'A primeira letra A apareceu na posição {frase.lower().find("a") + 1}')
print(f'A última letra A Aparece na posição {frase.lower().rfind("a") + 1}')
