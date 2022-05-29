#  Faça um programa que leia um ângulo qualquer e
#  mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo que deseja: '))
angSin = sin(radians(ang))
angCos = cos(radians(ang))
angTan = tan(radians(ang))

print(f'O ângulo de {ang} tem o SENO de {angSin:.2f} \n'
      f'O ângulo de {ang} tem o COSSENO de {angCos:.2f} \n'
      f'O ângulo de {ang} tem o TANGENTE de {angTan:.2f} ')

