frase = 'Por favor pilota Shinji'
print(frase[5]) # Mostrar o 5° elemento
print(frase[4:16]) # Começar do 4° elemento e ir até o 16°
print(frase[0::2]) # Começar do elemento 0 e ir até o final, pulando de 2 em 2.
print(frase.count('o')) # contar quantos o's existe na string.
print(frase.upper().count('O')) # transformei em upper e contei O's maiúsculos.
print(len(frase)) # conta quantos caracteres tem na string.
print(frase.replace('Shinji', 'Asuka')) # recorte Shinji por Asuka.
print('Shinji' in frase) # existe a palavra Shinji na frase?
print(frase.find('pilota')) # encontre a palavra 'pilota'
print(frase.split()) # dividir os elementos entre espaços

# Dica do Guanabara:
# Se quiser mostrar um texto enorme...
print("""Texto muito enorme
Texto muito enorme
Texto muito enorme
Texto muito enorme
Texto muito enorme""")
