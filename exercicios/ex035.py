# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
r1 = float(input('Insira o valor da segmenta 1: '))
r2 = float(input('Insira o valor da segmenta 2: '))
r3 = float(input('Insira o valor da segmenta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um TRIÂNGULO!')
else:
    print('Os segmentos acima NÂO podem formar um TRIÂNGULO!')
