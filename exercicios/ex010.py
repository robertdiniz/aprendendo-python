# Crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dólares ela pode comprar.

money = float(input('Quantos reais você tem na carteira? R$'))
print(f'Com R${money:.2f}, você pode ter US${money/3.27:.2f}')