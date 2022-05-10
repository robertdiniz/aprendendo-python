n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print(f'A soma entre {n1} + {n2} = {s}')

# 1 - O input ele nos retorna o valor de uma str
#       para resolvermos esse erro e não haver concatenação...
#           deve forçar o tipo de dado para int...
#
# 2 - Para exibir os valores no print podemos fazer de duas formas:
#       usando o .format() ou f antes das aspas.