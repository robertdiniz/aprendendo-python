# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
# verificando qual menor
if n1 < n2 and n1 < n3:
    menorNum = n1

if n2 < n1 and n2 < n3:
    menorNum = n2

if n3 < n1 and n3 < n2:
    menorNum = n3

# verificando qual maior
if n1 > n2 and n1 > n3:
    maiorNum = n1
if n2 > n1 and n2 > n3:
    maiorNum = n2
if n3 > n1 and n3 > n2:
    maiorNum = n3

print(f'O menor valor é {menorNum},\n'
      f'o maior valor é {maiorNum}')