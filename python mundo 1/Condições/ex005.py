from datetime import date
ano = int(input('Qual ano deseja analisar ? Coloque 0 caso queira o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(F'O ano de {ano} é bissexto!')
else:
    print(F'O ano de {ano} não é bissexto')

    