# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Insira seu número em metros: '))
print(f'{metros} em quilometros: {metros/1000}km \n'
      f'{metros} em hexâmetros: {metros/100}hm \n'
      f'{metros} em decâmetros: {metros/10}dam\n'
      f'{metros} em metros: {metros}m\n'
      f'{metros} em decímetro: {metros*10}dm\n'
      f'{metros} em centímetros: {metros*100}cm\n'
      f'{metros} em milímetros: {metros*1000}mm.')