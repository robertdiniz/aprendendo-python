# Desenvolva um programa que pergunte a distância
# de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

distancia = float(input('Qual foi a distância da viagem? '))
print(f'Você está para começar uma viagem de {distancia}Km.')
precoPrimario = distancia * 0.50
precoSecundario = distancia * 0.45
if distancia <= 200:
    print(f'O valor da passagem é R${precoPrimario:.2f}.')
else:
    print(f'O valor da passagem é de R${precoSecundario:.2f}')

