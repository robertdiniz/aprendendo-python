# Escreva um programa em Python que leia um número
# inteiro qualquer e peça para o usuário escolher
# qual será a base de conversão: 1 para binário, 2
# para octal e 3 para hexadecimal.

num = int(input('\033[1;31mDigite um número inteiro: '))
opcao = int(input('\033[1;31mEscolha a base de conversão: \n'
                  '[1] para BINÁRIO  \n'
                  '[2] para OCTAL  \n'
                  '[3] para HEXADECIMAL \n'))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print(f'Opção inválida tente novamente.')
