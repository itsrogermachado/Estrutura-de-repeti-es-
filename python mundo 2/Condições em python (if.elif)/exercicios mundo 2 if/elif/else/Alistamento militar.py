from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}. '.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar este ano! ')
elif idade > 18:
    saldo = idade - 18
    print('Você ja passou dos 18 ano. Você deveria ter se alistado a {} anos atrás '.format(saldo))
    ano = atual - saldo
    print('seu alistamento foi em {}...'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Faltam {} anos para você se alistar, aproveite bem! '.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
