# A Confederação Nacional de Natação precisa de um
# programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date

anoDeNascimento = int(input('Digite o ano de nascimento: '))
categoria = date.today().year - anoDeNascimento # idade
if categoria > 0 and categoria <= 9:
    print(f'O atleta tem {categoria} anos.\n'
          f'Sua categoria é MIRIM!')
elif categoria > 9 and categoria <= 14:
    print(f'O atleta tem {categoria} anos.\n'
          f'Sua categoria é INFANTIL!')
elif categoria > 14 and categoria <= 19:
    print(f'O atleta tem {categoria} anos.\n'
          f'Sua categoria é JÚNIOR')
elif categoria > 19 and categoria <= 25:
    print(f'O atleta tem {categoria} anos.\n'
          f'Sua categoria é SÊNIOR')
else:
    print(f'O atleta tem {categoria} anos.\n'
          f'Sua categoria é MASTER')
