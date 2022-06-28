# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada
# Km acima do limite.

velocidade = float(input('Digite a velocidade do seu carro por Km/h: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Você foi multado!'
          f'O valor da multa: R${multa:.2f}.')
else:
    print(f'Muito bem, dirija sempre com segurança!')