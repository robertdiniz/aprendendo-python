# Faça um programa que leia o ano de nascimento de um
# jovem e informe, de acordo com a sua idade, se ele
# ainda vai se alistar ao serviço militar, se é a hora
# exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

anoDeNascimento = int(input('Digite o ano de nascimento: '))
ano = date.today().year
alistamento = ano - anoDeNascimento
if alistamento == 18:
    print(f'Quem nasceu em {anoDeNascimento} tem {alistamento} anos, deve se alistar IMEDIATAMENTE!')
elif alistamento > 18:
    print(f'Quem nasceu em {anoDeNascimento} já deveria ter se alistado há {alistamento - 18} anos. \n'
          f'Seu alistamento foi em {anoDeNascimento + 18}.')
else:
    print(f'Quem nasceu em {anoDeNascimento} tem {alistamento} anos, deve se alistar daqui há'
          f' {18 - alistamento} anos. \n'
          f'Seu alistamento será em {anoDeNascimento + 18}.')
