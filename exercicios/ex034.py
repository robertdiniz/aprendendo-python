# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a
# R$1250,00, calcule um aumento de 10%. Para os inferiores ou
# iguais, o aumento é de 15%.

salario = float(input('Digite seu salário: R$'))
if salario >= 1250:
    aumentoSalarial = (((salario * 10) / 100) + salario)
else:
    aumentoSalarial = (((salario * 15) / 100) + salario)
print(f'Quem ganhava R${salario:.2f}, passará a ganhar R${aumentoSalarial:.2f} agora. ')