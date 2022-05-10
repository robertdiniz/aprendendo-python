# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário atual: R$'))
print(f'Seu salário era: R${salario:.2f}, \ncom aumento de 15%, seu salário será: R${salario + (salario*0.15):.2f}')