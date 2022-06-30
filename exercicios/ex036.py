# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual salário do comprodor? R$'))
anos = int(input('Quantos anos você pretende pagar? '))
prestacaoMensal = valorCasa / (anos * 12)
minimo = (salario * 30) / 100
print(f'Para pagar uma casa de R${valorCasa:.2f}, em {anos} anos.\n'
      f'a prestação será de R${prestacaoMensal:.2f}')
if prestacaoMensal <= minimo:
    print(f'Empréstimo pode ser CONCEDIDO!')
else:
    print(f'Empréstimo NEGADO!')
