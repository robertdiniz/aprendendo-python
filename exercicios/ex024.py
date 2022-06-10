# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da sua cidade: ')).strip()
separa = cidade.split()
print(f'{"Santos" in separa[0]}')